from google.adk.tools.function_tool import FunctionTool
from google.adk.tools.tool_context import ToolContext

THRESHOLD = 1000  # approval needed

def booking_order(amount: int, city: str, tool_context: ToolContext):

    # Small bookings auto-approved
    if amount <= THRESHOLD:
        return {"status": "approved", "message": f"Booked for {amount} in {city}"}

    # First call → request confirmation
    if not tool_context.tool_confirmation:
        tool_context.request_confirmation(
            hint=f"Booking for {amount} USD in {city}. Approve?",
            payload={"amount": amount, "city": city}
        )
        return {"status": "pending"}

    # Resumed → decision available
    if tool_context.tool_confirmation.confirmed:
        return {"status": "approved", "message": "Booking completed with approval!"}
    else:
        return {"status": "rejected", "message": "Booking cancelled"}

booking_tool = FunctionTool(booking_order, name="booking_order")
