import requests

BASE = "https://innvoaters-ev.hf.space"

print("[START]")

# Reset
res = requests.post(f"{BASE}/reset")
print("[STEP]", res.json())

# Step 1
action = {"type": "classify_severity", "value": "high"}
res = requests.post(f"{BASE}/step", json=action)
print("[STEP]", res.json())

# Step 2
action = {"type": "resolve_incident"}
res = requests.post(f"{BASE}/step", json=action)
print("[STEP]", res.json())

print("[END]")
