class IncidentEnv:
    def __init__(self):
        self.state = {
            "incident": None,
            "status": "initialized",
            "steps": 0
        }

    def reset(self):
        self.state = {
            "incident": "new incident created",
            "status": "reset",
            "steps": 0
        }

        return {
            "observation": self.state,
            "reward": 0,
            "done": False,
            "info": {}
        }

    def step(self, action):
        try:
            # Safe action handling
            action_type = action.get("action", "unknown")

            self.state["last_action"] = action_type
            self.state["steps"] += 1

            return {
                "observation": self.state,
                "reward": 1,
                "done": False,
                "info": {
                    "message": f"Action '{action_type}' executed"
                }
            }

        except Exception as e:
            return {
                "observation": self.state,
                "reward": -1,
                "done": False,
                "info": {
                    "error": str(e)
                }
            }

    def state_fn(self):
        return self.state
