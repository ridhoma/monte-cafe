import numpy as np

def euclidean_distance(p1, p2):
    """
    Calculate euclidean distance between point p1 and point p2
    p1: array/list/tuple with 2 elements [x1, y1]
    p2: array/list/tuple with 2 elements [x2, y2]
    """
    p1, p2 = np.array(p1), np.array(p2)
    return np.sqrt(np.sum((p1 - p2)**2))


def generate_random_points_around_center(xy, radius=0.3):
    """
    Given list/array of center points xy, generate random points located inside a circle with radius from xt
    xy: list/array of center points xy.shape[0] is number of points to be generated
    radius: float. Radius from center point xy
    """
    xy = np.array(xy)
    N = xy.shape[0]
    r = np.random.uniform(0, radius, N) 
    theta = np.random.uniform(0, 2*np.pi, N)
    x = xy[:,0] + r*np.cos(theta)
    y = xy[:,1] + r*np.sin(theta)
    return np.stack([x, y], axis=1)


def calculate_linear_path(r0, r1, t):
    """
    generate straight line passing through r0 and r1 splitted into t segments 
    r0: tuple/list/array of x and y coordinate. E.g. [0,0]
    r1: tuple/list/array of x and y coordinate. E.g. [0,0]
    t: integer, number of split between r0 and r1
    """
    return np.linspace(r0, r1, t)


def calculate_parabola_path(r0, r1, t, upward=True):
    """
    generate parabola path passing through r0 and r1 with stationary of the parabola in the middle
    r0: tuple/list/array of x and y coordinate. E.g. [0,0]
    r1: tuple/list/array of x and y coordinate. E.g. [0,0]
    t: integer, number of split between r0 and r1
    
    """
    x0, y0 = r0
    x1, y1 = r1
    xM = ((x0 + x1) / 2)
    if upward:
        sign = -1
    else:
        sign = 1
        
    yM =  sign * (0.55 + 0.02*np.random.randn())
    # left hand side
    X = np.array([
        [x0**2, x0, 1],   # Equation for initial position
        [x1**2, x1, 1],   # Equation for final position
        [xM**2, xM, 1]    # Equation for stationary point
    ])
    # right hand side
    y = np.array([y0, y1, yM])
    
    a, b, c = np.linalg.solve(X, y)
    x = np.linspace(x0, x1, t)
    y = a*x**2 + b*x + c
    return np.stack([x,y], axis=1)