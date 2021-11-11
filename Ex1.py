import json
import pandas as pd

import Time
from Building import Building
from CallForElevator import CallForElevator
from Elevator import Elevator

filePath = "Ex1_input/Ex1_Buildings/B1.json"
b = Building(filePath)
e = b.get_elevators()[0]

print(e.get_speed())

# f = open(filePath)
#
# building = json.loads(f.read())
#
# print(building)
# print(building["_elevators"])
# print(building["_elevators"][0])
#
# f.close()


calls = pd.read_csv("Ex1_input/Ex1_Calls/Calls_a.csv", index_col=False, header=None)  # DataFrame of calls

# calls[calls[5] == -1]

# while len(calls) > 0:
#     first_call = CallForElevator.__init__(calls.iloc[0])
#     first_call_duration = Time.time_for_call(first_call)
# calls[calls[1] < first_call.get_time]

# first_call = CallForElevator(calls.iloc[0])
#
# print(first_call.get_src())

elevators = b.get_elevators()
while not calls[calls["5"] == -1].empty:
    min_time = Time.get_new_call_time(elevators[0])
    for i in range(1, len(elevators)):
        curr_time = Time.get_new_call_time(elevators[i])
        if curr_time < min_time:
            min_time = curr_time
            

# print((calls.iloc[0]).to_list())
# need to add if for checking if each call can be reached (the floors are in range of building)


print(calls.head())
calls.iloc[0, 5] = 2
print(calls.head())
print(calls[calls[5] == -1])
