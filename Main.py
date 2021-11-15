import sys
import pandas as pd
import Time
import Utilities
from Building import Building
from CallForElevator import CallForElevator

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
    b = Building(building_path)
    elevators = b.get_elevators()
    df = pd.read_csv(input_path, index_col=False, header=None)  # DataFrame of calls
    Utilities.normalize_speed(elevators)
    calls = filter_df_rows(df, b)
    l = len(calls)
    print(l)
    # while not calls[calls[5] == -1].empty:
    for elev_index in range(len(elevators)):
        num_calls = int(elevators[elev_index].get_norm_speed() * l)
        call_jump = int(l / num_calls)
        for i in range(num_calls):
            while calls.iloc[i, 5] != -1:
                i += 1
            if i * call_jump < l:
                # calls[calls[5] == -1]
                c = calls.iloc[i * call_jump]
                calls.loc[c.name, 5] = elev_index  # c.name is the row, 5 is the col
    unanswered_calls = calls[calls[5] == -1]
    elev_index = 0
    for i in range(len(unanswered_calls)):
        c = unanswered_calls.iloc[i]
        calls.loc[c.name, 5] = elev_index
        if elev_index < len(elevators) - 1:
            elev_index += 1
        else:
            elev_index = 0

    for i in range(len(elevators)):
        print(len(calls[calls[5] == i]))

    calls.to_csv(output_path, index=False, header=False)


main(b_path, i_path, o_path)
