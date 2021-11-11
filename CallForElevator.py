import pandas as pd


class CallForElevator:

    def __init__(self, call: pd.Series):
        self.call = call

    def get_time(self):
        """:returns time call was made"""
        return self.call[1]

    def get_src(self):
        """:returns source floor"""
        return self.call[2]

    def get_dest(self):
        """:returns destination floor"""
        return self.call[3]

    # def get_calls_df(self):
    #     return self.calls
    #
    # def remove_calls(self, indices_lst):  # function deletes used rows from the DataFrame
    #     self.calls.drop(indices_lst, inplace=True)
    #     self.calls.reset_index(inplace=True, drop=True)  # resets index of row

    # def get_next_call(self):  # function returns first call and deletes it from the DataFrame
    #     call = self.calls.iloc[0].copy()
    #     self.calls.drop(0, inplace=True)
    #     return call

    # get calls according to time
    # remove calls that were used from DataFrame
