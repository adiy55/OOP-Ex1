import json
import pandas as pd

import Time
from Building import Building
from CallForElevator import CallForElevator
from Elevator import Elevator

filePath = "Ex1_input/Ex1_Buildings/B2.json"
b = Building(filePath)
calls = pd.read_csv("Ex1_input/Ex1_Calls/Calls_c.csv", index_col=False, header=None)  # DataFrame of calls
elevators = b.get_elevators()

while not calls[calls[5] == -1].empty:
    c = calls[calls[5] == -1].iloc[0]
    call = CallForElevator(c)
    elev_index = 0
    min_time = Time.get_new_call_time(elevators[elev_index], call)
    for i in range(1, len(elevators)):
        tmp_time = Time.get_new_call_time(elevators[i], call)
        if tmp_time < min_time:
            min_time = tmp_time
            elev_index = i
    calls.loc[c.name, 5] = elev_index  # c.name is the row, 5 is the col
    elevators[elev_index].get_call_list().append(call)

    # curr_length = len(elevators[elev_index].get_call_list())

    elevators[elev_index].set_time_to_finish(min_time)
    unanswered_calls = calls[calls[5] == -1]
    for i in range(len(unanswered_calls)):
        curr_call = unanswered_calls.iloc[i]
        call = CallForElevator(curr_call)
        curr_time = Time.call_falls_in_range(elevators[elev_index], call)
        if curr_time:
            calls.loc[curr_call.name, 5] = elev_index
            elevators[elev_index].set_time_to_finish(Time.time_to_stop(elevators[elev_index]))
            elevators[elev_index].get_call_list().insert(0, call)

print(len(calls[calls[5] == 0]))
print(len(calls[calls[5] == 1]))

# -----------------------------------------------------------------------------

# need to add if for checking if each call can be reached (the floors are in range of building)

# f = open(filePath)
#
# building = json.loads(f.read())
#
# print(building)
# print(building["_elevators"])
# print(building["_elevators"][0])
#
# f.close()
