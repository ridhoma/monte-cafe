# monte-cafe

This repository is a documentation my process on studying the fundamentals of Markov-Chain Monte Carlo (MCMC) for Bayesian Analysis. 

# Motivation

As a data scientist, every know and then I would be faced with the needs to do Bayesian Analysis. MCMC, being one of the most popular sampling method always comes in handy. Despite it's effectiveness, in practice, implementing MCMC algorithms from scratch would be a pain in the one's bum for which one would most likely resort to using readily available frameworks, for example [PyMC](https://www.pymc.io/welcome.html). 

However recently I feel something is missing, using MCMC (via PyMC) without knowing how it actually works under the hood. Unfortunately, the topic was not discussed thoroughly during my Physics undergraduate years in university. Therefore, I have commited with this repository to study MCMC from the basics. Moreover, when I started diving in, so many elements turns out to be inspired by Physics. I love Physics, so it's an extra motivation for me.

# Contents

The main contents are under `/notebooks` directory. Each jupyter notebook is about one particular topic, trying to peel the layers of mathematical foundation under MCMC. I try to be as precise as possoble with my explanations, equations, codes, visualization. In addition, I also add my self reflection on what I have learned through the process. 

I approach this study by writing form scratch some popular MCMC algorithms such as Metropolis-Hastings, Hamiltonican Monte Carlo, NUTS, etc.. By writing the them from scratch, not only will I learn how they work but also tricks or modification to improve the algorithms in difficult cases.

These algorithm implementations are often complicated. So to make the notebooks tidy, some implementations are written separately under `/models` or `/utils` directories.

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
