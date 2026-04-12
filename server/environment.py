def step(self, action):
    reward = 0.0

    action_type = action.get("type")
    action_value = action.get("value", None)

    if action_type == "classify_severity":
        if action_value == "high":
            self.state["severity"] = "high"
            reward = 0.5

    elif action_type == "resolve_incident":
        if self.state.get("severity") == "high":
            self.state["resolved"] = True
            reward = 1.0

    return {
        "observation": self.state,
        "reward": reward,
        "done": self.state.get("resolved", False)
    }
