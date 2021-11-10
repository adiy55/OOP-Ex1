import json
import pandas as pd

filePath = "Ex1_input/Ex1_Buildings/B1.json"

f = open(filePath)

building = json.loads(f.read())

print(building)
print(building["_elevators"])
print(building["_elevators"][0])

f.close()

calls = pd.read_csv("Ex1_input/Ex1_Calls/Calls_a.csv", index_col=False, header=None)

print(calls)
