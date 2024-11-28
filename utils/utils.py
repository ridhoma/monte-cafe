import numpy as np

def count_frequency(states):
    states_count = {}
    for s in states:
        if s in states_count:
            states_count[s] += 1
        else:
            states_count[s] = 1
    return states_count

def split_list_to_batch(lst, batch_size):
    if type(lst) != list:
        lst = list(lst)
    # Split the list into sublists of size K
    batches = [lst[i : i + batch_size] for i in range(0, len(lst), batch_size)]
    return batches
