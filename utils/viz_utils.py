import numpy as np
import networkx as nx
from matplotlib import pyplot as plt


def draw_equilateral_triangle_markov_chain_graph(
    P, node_labels, node_colors=None, ax=None
):
    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes
    G.add_nodes_from(node_labels[:3])

    # Manually set the position of the nodes so it creates a equilateral triangle, for aesthetic purpose
    tilt_pos = np.pi / 3  # set the tilt of the triangle
    pos = {
        node_labels[0]: [0, 0],
        node_labels[1]: [np.cos(tilt_pos), np.sin(tilt_pos)],
        node_labels[2]: [np.cos(np.pi / 3 + tilt_pos), np.sin(np.pi / 3 + tilt_pos)],
    }

    edge_label_annotations = []
    for i, node_i in enumerate(G):
        for j, node_j in enumerate(G):
            pij = P[i, j]
            G.add_edge(node_i, node_j, weight=pij)
            pos_i, pos_j = np.array(pos[node_i]), np.array(pos[node_j])
            x, y = (pos_i + pos_j) / 2
            if i == j:
                y += 0.11
                x = x + (x - 0.5) * 0.1
            else:
                x = x + 0.1 * np.sign(j - i)
                y = y - 0.05 * np.sign(j - i)
            edge_label_annotations.append(([node_i, node_j], np.array([x, y]), pij))

    if ax is None:
        fig, ax = plt.subplots()

    if node_colors is None:
        node_colors = "skyblue"

    nodes = nx.draw_networkx_nodes(
        G, pos, node_color=node_colors, node_size=[700] * 3, ax=ax
    )
    edges = nx.draw_networkx_edges(
        G, pos, edge_color="gray", arrows=True, connectionstyle="arc3, rad=0.12", ax=ax
    )
    labels = {p: f"{p}" for p, _ in pos.items()}
    nx.draw_networkx_labels(
        G, pos, labels=labels, font_size=9, font_color="gray", ax=ax
    )
    ax.set_aspect("equal")
    ax.axis("off")

    for ann in edge_label_annotations:
        [node_i, node_j], pos, pij = ann
        ax.annotate(
            f"{node_i}{node_j}={pij}",
            xy=pos,
            fontsize=9,
            horizontalalignment="center",
            verticalalignment="bottom",
        )

    return [nodes, edges]


def get_particles_state_locations(pi):   
    def get_partcile_position(center_point, N):
        r, theta = np.random.uniform(0, 0.3, N), np.random.uniform(0, 2*np.pi, N)
        x = center_point[0] + r*np.cos(theta)
        y = center_point[1] + r*np.sin(theta)
        return np.stack([x, y], axis=1)

    xy, states = [], []
    for i in range(len(pi)):
        xy.append(get_partcile_position(center_point=(2*i,0), N=pi[i]))
        states.extend([i]*pi[i])
        
    return np.concatenate(xy), np.array(states)


def plot_particles(xy, states, ax=None):
    if ax is None:
        fig, ax = plt.subplots()
        fig.dpi=150
    unique_states = set(states)
    for s in unique_states:
        xy_ = xy[states==s]
        ax.scatter(xy_[:,0], xy_[:,1], s=10)
    pad = 0.4
    ax.set_xlim([xy[:,0].min() - pad, xy[:,0].max() + 1.5*pad])
    ax.set_ylim([xy[:,1].min()- pad, xy[:,1].max() + pad])
    ax.set_aspect('equal')
    ax.axis("off")
    if ax is None:
        return fig, ax