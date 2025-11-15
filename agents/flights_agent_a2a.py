from google.adk.tools import FunctionTool
from google.adk.agents.llm_agent import LlmAgent
from google.adk.models.google_llm import Gemini
import requests
import os

FLIGHTS_SERVER_URL = os.getenv("FLIGHTS_SERVER_URL", "http://localhost:8001")

def remote_flight_search(origin: str, destination: str, date: str):
    """Call A2A flights server"""
    payload = {
        "origin": origin,
        "destination": destination,
        "date": date
    }
    res = requests.post(f"{FLIGHTS_SERVER_URL}/tasks/search_flights", json=payload)
    return res.json()

# FIX: remove name=
flight_tool = FunctionTool(remote_flight_search)

flights_agent = LlmAgent(
    name="flights_agent",
    model=Gemini(model="gemini-2.5-flash-lite"),
    instruction="""
    You help with flight search. 
    Always call the remote_flight_search tool to fetch real flight data.
    """,
    tools=[flight_tool],
)
