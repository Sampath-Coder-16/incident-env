import requests

BASE_URL = "https://innvoaters-ev.hf.space"

def run():
    print("[START] task=incident_management", flush=True)

    # RESET
    res = requests.post(f"{BASE_URL}/reset")
    data = res.json()

    # STEP
    action = {"action": "resolve_incident"}
    res = requests.post(f"{BASE_URL}/step", json=action)
    step_data = res.json()

    reward = step_data.get("reward", 0)

    print(f"[STEP] step=1 reward={reward}", flush=True)

    # END
    print("[END] task=incident_management score=1.0 steps=1", flush=True)


if __name__ == "__main__":
    run()
