class IncidentEnv:
    def __init__(self):
        self.state = {
            "incident": "Server CPU usage high",
            "severity": None,
            "resolved": False
        }

    def reset(self):
        self.state = {
            "incident": "Server CPU usage high",
            "severity": None,
            "resolved": False
        }
        return {
            "observation": self.state
        }

    def step(self, action):
        reward = 0.0

        # SAFE ACCESS (NO CRASH)
        action_type = action.get("type")
        action_value = action.get("value", None)

        # STEP LOGIC
        if action_type == "classify_severity":
            if action_value == "high":
                self.state["severity"] = "high"
                reward = 0.5
            else:
                self.state["severity"] = "low"
                reward = 0.2

        elif action_type == "resolve_incident":
            if self.state.get("severity") == "high":
                self.state["resolved"] = True
                reward = 1.0
            else:
                reward = -0.5

        return {
            "observation": self.state,
            "reward": reward,
            "done": self.state.get("resolved", False)
        }

    def state_fn(self):
        return self.state
