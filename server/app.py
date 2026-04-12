from fastapi import FastAPI
from environment import IncidentEnv

app = FastAPI()
env = IncidentEnv()

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: dict):
    return env.step(action)

@app.get("/state")
def state():
    return env.state_fn()


# REQUIRED
def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)


# VERY IMPORTANT
if __name__ == "__main__":
    main()
