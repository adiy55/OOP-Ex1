import sys

import pandas as pd

import Time
from Building import Building
from CallForElevator import CallForElevator

inp = sys.argv
b_path, i_path, o_path = inp[1], inp[2], inp[3]


def main(building_path, input_path, output_path):
    b = Building(building_path)
    elevators = b.get_elevators()
    df = pd.read_csv(input_path, index_col=False, header=None)  # DataFrame of calls

    # copy of DataFrame with calls in building floors range
    calls = df.loc[((df[2] >= b.get_min_floor()) & (df[2] <= b.get_max_floor()) & (df[3] >= b.get_min_floor()) & (
            df[3] <= b.get_max_floor()))].copy()
    print(len(calls))

    while not calls[calls[5] == -1].empty:
        c = calls[calls[5] == -1].iloc[0]
        curr_first_call = CallForElevator(c)
        elev_index = 0
        min_time = Time.get_new_call_time(elevators[elev_index], curr_first_call)
        for i in range(1, len(elevators)):
            tmp_time = Time.get_new_call_time(elevators[i], curr_first_call)
            if tmp_time < min_time:
                min_time = tmp_time
                elev_index = i
        calls.loc[c.name, 5] = elev_index  # c.name is the row, 5 is the col
        df.loc[c.name, 5] = elev_index
        elevators[elev_index].get_call_list().append(curr_first_call)

        curr_length = len(elevators[elev_index].get_call_list())

    elevators[elev_index].set_time_to_finish(min_time)
    unanswered_calls = calls[calls[5] == -1]

    for i in range(len(unanswered_calls)):
        curr_call = unanswered_calls.loc[i]
        call = CallForElevator(curr_call)
        curr_time = Time.call_falls_in_range(elevators[elev_index], call)
        if curr_time and (
                (curr_first_call.get_src() <= call.get_src() <= curr_first_call.get_dest()) or (
                curr_first_call.get_src() >= call.get_src() >= curr_first_call.get_dest())):
            calls.loc[curr_call.name, 5] = elev_index
            df.loc[curr_call.name, 5] = elev_index
            elevators[elev_index].set_time_to_finish(Time.time_to_stop(elevators[elev_index]))
            elevators[elev_index].get_call_list().insert(curr_length, call)
            curr_length += 1

    for i in range(len(elevators)):
        print(len(calls[calls[5] == i]))

    df.to_csv(output_path, index=False, header=False)  # todo: how to move last line in csv


main(b_path, i_path, o_path)
# main("Ex1_input/Ex1_Buildings/B2.json", "Ex1_input/Ex1_Calls/Calls_c.csv", "Ex1_input/output.csv")

# -----------------------------------------------------------------------------

# f = open(filePath)
#
# building = json.loads(f.read())
#
# print(building)
# print(building["_elevators"])
# print(building["_elevators"][0])
#
# f.close()
