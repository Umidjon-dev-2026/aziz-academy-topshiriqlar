# choice
# start -> "Started"
# stop -> "Stopped"
# pause -> "Paused"
# aks holda "Unknown command"
c = input().strip().lower()
if c == "start":
    print("Started")
elif c == "stop":
    print("Stopped")
elif c == "pause":
    print("Paused")
else:
    print("Unknown command")