import numpy as np
from scipy import stats

def normal_step_method(mu, s):
    return stats.norm.rvs(loc=mu, scale=s)