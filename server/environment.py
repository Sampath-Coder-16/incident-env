class IncidentEnv:
    def __init__(self):
        self.state = {"status": "initialized"}

    def reset(self):
        self.state = {"status": "reset"}
        return self.state

    def step(self, action):
        return {
            "received_action": action,
            "status": "ok"
        }

    def state_fn(self):
        return self.state
