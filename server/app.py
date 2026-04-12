from fastapi import FastAPI
from server.environment import IncidentEnv  # ✅ CORRECT IMPORT

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

@app.get("/state")
def state():
    try:
        return env.state_fn()
    except Exception as e:
        return {"error": str(e)}

# ✅ REQUIRED FOR OPENENV VALIDATOR
def main():
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)

# ✅ REQUIRED FOR DIRECT RUN
if __name__ == "__main__":
    main()
