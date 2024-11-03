import argparse
import json
import matplotlib.pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-b", "--benchmark", type=str,
	help="benchmark json filename")
ap.add_argument("-l", "--log", type=int,
	help="logorithmic scaling: 1=yes, 0=no")
args = vars(ap.parse_args())

with open(args["benchmark"], 'r') as file:
    json_data = file.read()

data = json.loads(json_data)

indices = [entry["Index"] for entry in data]
player_count = [entry["PlayerCount"] for entry in data]
memory_load = [entry["SystemMemoryUsage"] for entry in data]
heap_size = [entry["LocalHeapSize"] for entry in data]
total_committed = [entry["TotalLocalCommitted"] for entry in data]

plt.plot(indices, player_count, marker='v', linestyle='-', color='b', label="Player Count")
plt.plot(indices, memory_load, marker='o', linestyle='-', color='b', label="System Memory Usage (GB)")
plt.plot(indices, heap_size, marker='s', linestyle='--', color='g', label="CS# Heap Size (MB)")
plt.plot(indices, total_committed, marker='^', linestyle='-.', color='r', label="CS# Total Committed (MB)")
if(args["log"] == 1):
    plt.yscale('log')

plt.xlabel("Index")
plt.ylabel("Values")
plt.title("Server Metrics over Time")
plt.legend()

plt.show()