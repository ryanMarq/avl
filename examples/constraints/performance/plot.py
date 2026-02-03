import matplotlib.pyplot as plt
import json
from pprint import pp

with open("times.json", "r") as f:
    json_string = f.read()

times: dict = json.loads(json_string)
times = {int(k): float(v) for k, v in times.items()}

pp(times)

plt.figure(1)
plt.plot(list(times.keys()), list(times.values()))

#plt.xscale("log")
#plt.yscale("log")

plt.xlabel("Vars Randomized")
plt.ylabel("Time (seconds)")

plt.title("Time for AVL to a Single Object Depending on the Number of Vars")

plt.savefig("random_time_linear.png")