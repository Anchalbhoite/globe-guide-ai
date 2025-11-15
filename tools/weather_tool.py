from google.adk.tools import FunctionTool

def get_weather(city: str):
    return {
        "weather": f"Sunny day expected in {city} with 24°C temperature."
    }

weather_tool = FunctionTool(get_weather, name="get_weather")
