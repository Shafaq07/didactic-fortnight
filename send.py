import json, os, time, urllib.request
msgs = json.load(open("messages.json", encoding="utf-8"))
slot = int(time.time() // 43200)  # changes every 12 hours
text = msgs[slot % len(msgs)]
topic = os.environ.get("NTFY_TOPIC", "").strip()
if not topic: raise SystemExit("Add the NTFY_TOPIC secret first.")
req = urllib.request.Request("https://ntfy.sh/" + topic, data=text.encode(), headers={"Title": "Stay Here"})
urllib.request.urlopen(req, timeout=30)
print("Sent")
