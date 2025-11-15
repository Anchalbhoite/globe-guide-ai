from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.post("/tasks")
async def tasks(req: dict):
    task = req.get("task", {})
    tool = task.get("tool")
    args = task.get("arguments", {})

    if tool == "search_flights":
        origin = args.get("origin", "")
        dest = args.get("destination", "")
        date = args.get("date", "")

        return {
            "status": "success",
            "result": {
                "flights": [
                    {"airline": "SkyJet", "price": 320, "time": "10:30 AM"},
                    {"airline": "BlueAir", "price": 350, "time": "02:05 PM"},
                ],
                "origin": origin,
                "destination": dest,
                "date": date,
            }
        }

    return {"status": "error", "message": "Unknown tool"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
