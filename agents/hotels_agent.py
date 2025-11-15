from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool

HOTELS = [
    {"name": "Grand Plaza", "city": "London", "price": 120},
    {"name": "CozyStay", "city": "London", "price": 95},
]

def search_hotel(city: str, budget: int = 200):
    return {
        "hotels": [h for h in HOTELS if h["city"] == city and h["price"] <= budget]
    }

hotel_tool = FunctionTool(search_hotel, name="search_hotels")

hotels_agent = LlmAgent(
    name="HotelsAgent",
    model="gemini-2.5-flash-lite",
    instruction="Return hotel recommendations.",
    tools=[hotel_tool],
)
