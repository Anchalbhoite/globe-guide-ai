import requests
from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool

def remote_flight_search(origin: str, destination: str, date: str):
    res = requests.post("http://localhost:8001/tasks", json={
        "task": {
            "tool": "search_flights",
            "arguments": {"origin": origin, "destination": destination, "date": date}
        }
    })
    return res.json()

flight_tool = FunctionTool(
    func=remote_flight_search,
    name="search_flights"
)

flights_agent = LlmAgent(
    name="FlightsAgent",
    model="gemini-2.5-flash-lite",
    instruction="Search flights using the remote A2A flights server.",
    tools=[flight_tool],
)
