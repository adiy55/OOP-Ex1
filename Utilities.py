def normalize_speed(lst):
    """
    Calculates the normalized speed of every elevator and saves it accordingly
    :param lst:
    :return: void: only updates every Elevator object in lst
    """
    sum_curr = 0
    for i in range(len(lst)):
        sum_curr += lst[i].get_speed()

    for i in range(len(lst)):
        elev_speed = lst[i].get_speed()
        normed = elev_speed / sum_curr
        lst[i].set_norm_speed(normed)
