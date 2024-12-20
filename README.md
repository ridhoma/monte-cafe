# monte-cafe

The repository is a collection of `/notebooks` documenting my process on studying the fundamentals of Markov Chain Monte Carlo for Bayesian Analysis..

# Motivation

Although as a data scientist I have several real-world experience doing statistical analysis using Bayesian frameworks with PyMC, I haven't really gotten time to study about it in a formal and structured way. Sadly, it's not under Physics department curiculum. Therefore, I have commited with this repository to study it from the very basics.

In the real world, implementing MCMC from scratch would be a pain in the bum compared to just using readily available frameworks like PyMC. But recently I feel something is missing, not knowing how it actually works. Beside, when I started diving in, so many elements turns out to be inspired by Physics. I love Physics, so it's an extra motivation for me.

# Table of Contents

All the main contents are under `/notebooks` directory. Each jupyter notebooks is about one particular topic, learnt through interesting cases, with all the conceptual and theoretical explanation, equations, codes (with comments), visualization, and my self reflection on what I learnt through. 

My method is by starting with the very basic exercise, then moving on the the more complex, until finally we reach to the advance topic of Bayesian Inference (regression, classification, maybe some image or signal processing, etc..) Table below summarizes the already-published notebooks and my plan for the next ones

## Published Notebooks
| Notebooks Title | First Published Date | Content  Description | Learning Objectives |
|-----------------|-----------------|-------------|----------|
| [01 The Circle-in-A-Square Model](https://github.com/ridhoma/monte-cafe/blob/main/notebooks/01%20The%20Circle-in-A-Square%20Model.ipynb) |2024-11-27    | Using Monte-Carlo to estimate the value of $\pi$         | Understanding the Law of Large Number and basic intuition of sampling process      |
| [02 Simulated Annealing to Help The Salesman](https://github.com/ridhoma/monte-cafe/blob/main/notebooks/02%20Simulated%20Annealing%20to%20Help%20The%20Salesman.ipynb) |2024-11-27    | Simulated Annealing to estimate optimum route in large Traveling Salesman Problem (TSP, $N \ge 100$)        | Basic intuition of acceptance/rejection which probability can be controlled (e.g. by Temperature parameter), familiarizing with Metropolis-Hasting algorithm    |
| [03 Discrete-Time Markov-Chain](https://github.com/ridhoma/monte-cafe/blob/main/notebooks/03%20Discrete-Time%20Markov%20Chain.ipynb)    | 2024-11-30 | Simulation of Markov Chain as random walk on a graph | What exactly Markov Chain is, and why it is the theoretical requirement for Monte-Carlo to be a valid sampling algorithm at all, and hence the name Markov-Chain Monte Carlo (MCMC) |

## Next Plan / Work in Progress
| Topics | Content Description | Learning Objectives |
|--------|-------------|---------------------|
| Stationary Distribution and Detailed Balance    | Showing a condition of when a Markoc Chain can or cannot reach stationary distribution | What are condition of Markov process that would make it usable for MCMC, deriving the Metropolis-Hasting algorithm from Detailed Balance property of Markov-Chain |
| Metropolis Hasting Algorithm    | Implementation of Metropolis-Hasting algorithm from scratch to sample from a skewed target distribution   | Understand how Metropolis-Hasting algorithm uses the stationary distribution and detailed balance property of Markov-Chain to do sampling |
| Metropolis Adjusted Langevin Algorithm (MALA)    | Race between Monte-Carlo vs Gradient Descent with ADAM optimizer to find minimum value of a non-trivial multi-modals cost function, Rosenbrock "The Banana" Function.        | Familiarize with Hamiltonian Monte Carlo sampling algorithm                 |
|... and more later ...|...|...|



# Collaborations

I really welcome if anyone wants to collaborate and study together with me. If you want to ask any questions, discuss any related topics, or point out my mistakes, it would be amazing if you could raise an Issue. I will engage as much as possoble. 

Not only that I also welcome if anyone wants to contribute with the code. Contact me and I can invite you as collaborators in this repository


# Running The Notebooks Locally

In order run the notebooks on your local machine you need to install all the dependencies listed under `pyproject.toml`. I use Poetry to manage my dependencies

Install latest version of Poetry
```
curl -sSL https://install.python-poetry.org | python3 -
```

Go to this project directory on your local machine and install dependencies
```
cd path/to/project/monte-cafe
poetry install
```

Activate the virtual environment
```
poetry shell
```

Launch Jupyter notebook on browser
```
jupyter notebook
```

Important to note that when new notebooks are published, there might be new dependencies to be installed. So please make sure to be up to date with the `main` branch.


# Contact Me

X (Formerly Twitter): [@rdmakbar](https://x.com/rdmakbar)
