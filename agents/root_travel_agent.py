from google.adk.agents import LlmAgent
from google.adk.tools import AgentTool
from google.adk.models.google_llm import Gemini

from agents.flights_agent_a2a import flights_agent
from agents.hotels_agent import hotels_agent
from agents.explorer_agent import explorer_agent
from agents.tools.weather_tool import weather_tool
from agents.tools.booking_tool import booking_tool
from agents.tools.memory_tool import memory_save, memory_read

root_travel_agent = LlmAgent(
    name="TravelConcierge",
    model="gemini-2.5-flash-lite",
    instruction="""
    You are GlobeGuide AI — a travel planning assistant.
    Use sub-agents to fetch flights, hotels, attractions, and weather.
    Use booking_order for final bookings (requires approval for large values).
    """,
    tools=[
        AgentTool(agent=flights_agent),
        AgentTool(agent=hotels_agent),
        AgentTool(agent=explorer_agent),
        weather_tool,
        booking_tool,
        memory_save,
        memory_read
    ]
)
