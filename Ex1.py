import json
import pandas as pd

import Time
from Building import Building
from CallForElevator import CallForElevator
from Elevator import Elevator

filePath = "Ex1_input/Ex1_Buildings/B1.json"
b = Building(filePath)
# e = b.get_elevators()[0]

# print(e.get_speed())

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
elevators = b.get_elevators()
while not calls[calls[5] == -1].empty:
    c = CallForElevator(calls[calls[5] == -1].iloc[0])
    elev_idx = 0
    min_time = Time.get_new_call_time(elevators[elev_idx], c)
    for i in range(1, len(elevators)):
        curr_time = Time.get_new_call_time(elevators[i], c)
        if curr_time < min_time:
            min_time = curr_time
            elev_idx = i
    curr_c = calls[calls[5] == -1].iloc[0]
    calls.iloc[curr_c.name, 5] = elev_idx
    calls = calls[calls[5] == -1]
    # break
    elevators[elev_idx].get_call_list().append(c)
    # print(len(calls.loc[calls[5] == -1]))
    curr_calls = calls.loc[(calls[1] <= min_time) & (calls[5] == -1)]
    # print(len(curr_calls))

    # pd.options.mode.chained_assignment = None  # default='warn'
    for i in range(len(curr_calls)):
        curr_c = CallForElevator(curr_calls.iloc[i])
        curr_t = Time.call_falls_in_range(elevators[elev_idx], curr_c)
        if curr_t:
            calls.loc[curr_calls.iloc[i].name, 5] = elev_idx
            elevators[elev_idx].get_call_list().append(curr_c)

# print((calls.iloc[0]).to_list())
# need to add if for checking if each call can be reached (the floors are in range of building)


# print(calls.head())
# calls.iloc[0, 5] = 2
# print(calls.head())
# print(calls[calls[5] == -1])
