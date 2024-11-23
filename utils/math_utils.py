import numpy as np

def euclidean_distance(p1, p2):
    """
    Calculate euclidean distance between point p1 and point p2
    p1: array/list/tuple with 2 elements [x1, y1]
    p2: array/list/tuple with 2 elements [x2, y2]
    """
    p1, p2 = np.array(p1), np.array(p2)
    return np.sqrt(np.sum((p1 - p2)**2))