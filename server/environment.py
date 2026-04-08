class IncidentEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.state = {
            "incident": "Server Down",
            "severity": None,
            "resolved": False
        }
        return {"message": "Incident started"}

    def step(self, action):
        reward = 0.0

        if action["type"] == "classify_severity":
            if action["value"] == "high":
                self.state["severity"] = "high"
                reward = 0.5

        elif action["type"] == "resolve_incident":
            if self.state["severity"] == "high":
                self.state["resolved"] = True
                reward = 1.0

        return {
            "observation": self.state,
            "reward": reward,
            "done": self.state["resolved"]
        }

    def state_fn(self):
        return self.state
