import sys
import pandas as pd
import Utilities
from Building import Building


def main(building_path, input_path, output_path):
    """
    Main function of the program.
    :param building_path: JSON Building file path
    :param input_path: input calls csv file path
    :param output_path: path to save output
    """
    b = Building(building_path)
    elevators = b.get_elevators()
    df = pd.read_csv(input_path, index_col=False, header=None)  # DataFrame of calls
    Utilities.normalize_speed(elevators)
    calls = Utilities.filter_df_rows(df, b)
    calls_length = len(calls)

    for elev_index in range(len(elevators)):  # iterate elevators
        num_calls = int(
            elevators[elev_index].get_norm_speed() * calls_length)  # number of calls to assign to the current elevator
        call_jump = int(calls_length / num_calls)  # optimal interval according to the number of calls
        for i in range(num_calls):
            while calls.iloc[i, 5] != -1:  # skips allocated calls
                i += 1
            if i * call_jump < calls_length:  # allocate call if in range (of total number of calls)
                c = calls.iloc[i * call_jump]
                calls.loc[c.name, 5] = elevators[elev_index].get_id()  # c.name is the row, 5 is the col
    unanswered_calls = calls[calls[5] == -1]
    elev_index = 0
    for i in range(len(unanswered_calls)):  # allocate any unassigned calls left by assigning one call per elevator,
        # alternate between elevators
        c = unanswered_calls.iloc[i]
        calls.loc[c.name, 5] = elevators[elev_index].get_id()
        if elev_index < len(elevators) - 1:  # if reached the end of elevators revert to the first elevator
            elev_index += 1
        else:
            elev_index = 0

    calls.to_csv(output_path, index=False, header=False)


inp = sys.argv  # read input from command line
if len(inp) > 3:
    b_path, i_path, o_path = inp[1], inp[2], inp[3]

    main(b_path, i_path, o_path)  # calling the main function
