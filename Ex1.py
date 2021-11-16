import sys
import pandas as pd
import Utilities
from Building import Building

inp = sys.argv
b_path, i_path, o_path = inp[1], inp[2], inp[3]


def filter_df_rows(df, b: Building):
    """
    :param b:
    :param df:
    :return:
    copy of DataFrame with calls in building floors range """
    calls = df.loc[((df[2] >= b.get_min_floor()) & (df[2] <= b.get_max_floor()) & (df[3] >= b.get_min_floor()) & (
            df[3] <= b.get_max_floor()))].copy()
    return calls


def main(building_path, input_path, output_path):
    """
    Main function of the program.
    :param building_path:
    :param input_path:
    :param output_path:
    :return: outputs a csv file as expected to the output_path
    """
    b = Building(building_path)
    elevators = b.get_elevators()
    df = pd.read_csv(input_path, index_col=False, header=None)  # DataFrame of calls
    Utilities.normalize_speed(elevators)
    calls = filter_df_rows(df, b)
    calls_length = len(calls)

    for elev_index in range(len(elevators)):  # Iterating over Elevators
        num_calls = int(elevators[elev_index].get_norm_speed() * calls_length)  # Number of calls each elevator should
        # receive
        call_jump = int(calls_length / num_calls)  # which interval is the most optimal according to the
        # number of calls.
        for i in range(num_calls):
            while calls.iloc[i, 5] != -1:  # If the call was already allocated to another elevator,
                # choose the next unallocated call
                i += 1
            if i * call_jump < calls_length:  # If falls in range of calls, allocate call
                c = calls.iloc[i * call_jump]
                calls.loc[c.name, 5] = elevators[elev_index].get_id()  # c.name is the row, 5 is the col
    unanswered_calls = calls[calls[5] == -1]  # If any calls remain unallocated, allocate them by iterating over the
    # elevators and assigning each elevator a call until all are assigned
    elev_index = 0
    for i in range(len(unanswered_calls)):
        c = unanswered_calls.iloc[i]
        calls.loc[c.name, 5] = elevators[elev_index].get_id()
        if elev_index < len(elevators) - 1:  # If reached the end of elevators, revert to first elevator
            elev_index += 1
        else:
            elev_index = 0

    calls.to_csv(output_path, index=False, header=False)


    main(b_path, i_path, o_path)  # calling the main func

# todo: unit testing: 1. check utility function ratios 2. check if number of allocated calls is correct by ratios and
#  total number of calls
