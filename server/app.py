from fastapi import FastAPI
from environment import IncidentEnv

app = FastAPI()
env = IncidentEnv()

@app.post("/reset")
def reset():
    try:
        return env.reset()
    except Exception as e:
        return {"error": str(e)}

@app.post("/step")
def step(action: dict):
    try:
        return env.step(action)
    except Exception as e:
        return {"error": str(e)}
# ✅ REQUIRED FOR VALIDATOR
def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)

# ✅ REQUIRED
if __name__ == "__main__":
    main()
