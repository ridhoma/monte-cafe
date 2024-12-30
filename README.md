# monte-cafe

This repository is a documentation my process on studying the fundamentals of Markov-Chain Monte Carlo (MCMC) for Bayesian Analysis. 

# Motivation

MCMC is one of many methods to draw samples from a probability distribution, and is very useful for doing a Bayesian analysis. In the real world, implementing MCMC algorithms from scratch would be a pain in the bum compared to just using readily available frameworks, for example [PyMC](https://www.pymc.io/welcome.html). 

But recently I feel something is missing, not knowing how it actually works behind the curtain despite, as a data scientist, often using it. Sadly, it's not studied very detail in Undergraduate Physics curiculum back in university (or maybe I missed the classes). 

Anyway, I have commited with this repository to study MCMC from the very basics. Moreover, when I started diving in, so many elements turns out to be inspired by Physics. I love Physics, so it's an extra motivation for me.

# Contents

The main contents are under `/notebooks` directory. Each jupyter notebook is about one particular topic, learnt through interesting cases, with all the conceptual and theoretical explanation, equations, codes, visualization, and my self reflection on what I learnt through the process. 

My study method is by writing form scratch some popular MCMC algorithms such as Metropolis-Hastings, Hamiltonican Monte Carlo, NUTS, etc.. By writing the them from scratch, not only will I learn how they work but also tricks or modification to improve the algorithms in difficult cases.

These algorithm implementations are often complicated. So to make the notebooks tidy, some implementation are written separately under `/models` directory.

**Note:** This repository is a work in progress so the content will change (hopefully) frequently.


# Running Locally

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


# Collaborations

I really welcome if anyone wants to collaborate and study together with me. Raise an issue if you want to ask any questions, discuss any related topics, or point out my mistakes. I will engage as much as possoble. 

Not only that I also welcome if anyone wants to contribute with the code. Contact me and I can invite you as collaborators in this repository


# Contact Me

X (Formerly Twitter): [@rdmakbar](https://x.com/rdmakbar)
