import numpy as np


def normalize_speed(lst):
    sum_curr = 0
    for i in range(len(lst)):
        sum_curr += lst[i].get_speed()

    for i in range(len(lst)):
        elev_speed = lst[i].get_speed()
        normed = elev_speed/sum_curr
        lst[i].set_norm_speed(normed)
