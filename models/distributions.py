import numpy as np
from scipy import stats
from utils.utils import to_numpy_array

def normal_pdf(x, mu, s):
    return stats.norm.pdf(x, loc=mu, scale=s)

    
def gmm_pdf(x, weights, mu, sigma):
    x, is_iterable = to_numpy_array(x)    
    weights, _ = to_numpy_array(weights)
    mu, _ = to_numpy_array(mu)
    sigma, _ = to_numpy_array(sigma)
    gaussians = stats.norm.pdf(x[:, np.newaxis], loc=mu, scale=sigma)
    f = np.dot(gaussians, weights)
    if is_iterable:
        return f
    else:
        return f[0]

