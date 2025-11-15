from google.adk.tools import FunctionTool

import requests

# -----------------------------
# Remote Flight API Client
# -----------------------------

def remote_flight_search(source: str, destination: str, date: str):
    """
    name: search_flights
    description: Search for flights from A2A flight server.
    """
    url = "http://localhost:8001/search_flights"
    payload = {
        "source": source,
        "destination": destination,
        "date": date
    }
    res = requests.post(url, json=payload)
    return res.json()


flight_tool = FunctionTool(
    func=remote_flight_search
)

# -----------------------------
# Flights Agent
# -----------------------------
from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini

flights_agent = LlmAgent(
    name="flights_agent",
    model=Gemini(model="gemini-2.5-flash-lite"),
    instruction="""
        You are a flight search assistant.
        Use the search_flights tool to find flights.
        Always return structured flight results.
    """,
    tools=[flight_tool]
)
