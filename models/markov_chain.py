import numpy as np


def random_walks(Q, max_steps):
    n_states = Q.shape[0]
    current_state = np.random.choice(n_states) # start at random node
    states = [] # list to keep track the visited states in each iteration
    freq = [] # list to keep track how many times each states has been visited. Initial value is 1 for state-A
    for step in range(max_steps + 1):
        states.append(current_state) # keep track of the current state
        # count the frequency of visit of each state
        f_ = count_states_frequency(states)
        f = np.zeros(n_states)
        for k,v in f_.items():
            f[k] = v  
        freq.append(f)
        #  random walk to next node according to Q, and update current_state
        current_state = np.random.choice(n_states, p=Q[current_state])
    
    # return as numpy array
    return np.array(freq), np.array(states)


def random_particle_migrations(Q, particles_dist, max_steps):
    n_states = Q.shape[0]
    s1 = np.zeros(particles_dist[0]).astype(int)
    s2 = np.ones(particles_dist[1]).astype(int)
    current_states = np.concatenate([s1,s2])
    particle_counts, states = [], []
    for step in range(max_steps + 1):
        c = count_states_particles(current_states, n_states)
        particle_counts.append(c)
        states.append(current_states)
        # move particles randomly according to Q
        current_states = np.array([np.random.choice(n_states, p=Q[s]) for s in current_states])

    return np.array(particle_counts), np.array(states)


def count_states_particles(states, n_states):
    particles_count = np.zeros(n_states).astype(int)
    count_ = count_states_frequency(states)
    for k,v in count_.items():
        particles_count[k] = v  
    return particles_count


def count_states_frequency(states):
    states_count = {}
    for s in states:
        if s in states_count:
            states_count[s] += 1
        else:
            states_count[s] = 1
    return states_count


def calculate_stationary_distribution(Q):
    # system of linear equations A.x = b, solve for x
    A = Q.T - np.eye(Q.shape[0])
    A = np.vstack((A, np.ones(Q.shape[0])))
    b = np.zeros(Q.shape[0])
    b = np.append(b, 1)
    pi = np.linalg.lstsq(A, b, rcond=None)[0]
    return pi

