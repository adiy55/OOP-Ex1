from Building import Building


def filter_df_rows(df, b: Building):
    """
    :param b: Building
    :param df: DataFrame containing elevator calls
    :return: deep copy of DataFrame with calls in building floors range
    """
    calls = df.loc[((df[2] >= b.get_min_floor()) & (df[2] <= b.get_max_floor()) & (df[3] >= b.get_min_floor()) & (
            df[3] <= b.get_max_floor()))].copy()
    return calls


def normalize_speed(lst):
    """
    Calculates and sets the normalized speed attribute for each elevator
    :param lst: list of elevators
    """
    sum_curr = 0
    for i in range(len(lst)):
        sum_curr += lst[i].get_speed()

    for i in range(len(lst)):
        elev_speed = lst[i].get_speed()
        normed = elev_speed / sum_curr
        lst[i].set_norm_speed(normed)
