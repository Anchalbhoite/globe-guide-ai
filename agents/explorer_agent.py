from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool

def explore_city(city: str):
    return {
        "attractions": [
            {"name": "City Museum", "type": "museum"},
            {"name": "Skyline Point", "type": "viewpoint"},
        ]
    }

explore_tool = FunctionTool(explore_city, name="explore_city")

explorer_agent = LlmAgent(
    name="ExplorerAgent",
    model="gemini-2.5-flash-lite",
    instruction="Get attractions for the city.",
    tools=[explore_tool],
)
