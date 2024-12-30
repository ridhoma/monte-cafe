import numpy as np
from functools import wraps

def split_list_to_batch(lst, batch_size):
    if type(lst) != list:
        lst = list(lst)
    # Split the list into sublists of size K
    batches = [lst[i : i + batch_size] for i in range(0, len(lst), batch_size)]
    return batches

def sanitize_variable_before_convert_to_numpy_array(func):
    """
    A decorator to preprocess input for a function.
    Converts input to a NumPy array and identifies if it was iterable.
    """
    @wraps(func)
    def wrapper(x, *args, **kwargs):
        if hasattr(x, '__iter__') and not isinstance(x, (str, bytes)):
            x, is_iterable = np.array(x), True
        elif isinstance(x, (int, float, complex)):
            x, is_iterable = np.array([x]), False
        else:
            raise TypeError("Unsupported type for x.")
        return func(x, *args, **kwargs), is_iterable
    return wrapper

@sanitize_variable_before_convert_to_numpy_array
def to_numpy_array(x):
    return x



    
