import time
from tqdm import tqdm



def loading_indicator(load_file):  # for lists

    for i in tqdm(load_file):
        time.sleep(1)


def loading_indicator_int(int_load_file):  # for integers

    count_of_iteration_list = []

    # while int_load_file > 0:
    #     count_of_iteration_list.append(1)
    #     int_load_file -= 1

    for i in tqdm(int_load_file):
        time.sleep(1)
