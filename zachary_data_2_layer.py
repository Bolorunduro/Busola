# -*- coding: utf-8 -*-
"""Zachary  Data 2 Layer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HACMN16ObIKN0OnOwGerzGHScYfc0qef
"""

import numpy as np
import random
import networkx as nx
from IPython.display import Image
import matplotlib.pyplot as plt

pip install networkx

n=34
m = 78
G_karate = nx.karate_club_graph()

pos = nx.spring_layout(G_karate)
nx.draw(G_karate, cmap = plt.get_cmap('CMRmap_r'), with_labels=True, pos=pos)

import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.community import kernighan_lin_bisection


def draw_spring(G, com):
    """
    G: Figure
         COM: Divided community
         Node_size represents the node size
         Node_color Represents Node Colors
         Node_shape indicates node shape
    with_labels=TRUE indicates whether the node is tagged
    """
    pos = nx.spring_layout(G)  #
    NodeId = list(G.nodes())
    node_size = [G.degree(i) ** 1.2 * 90 for i in NodeId]  # Node size

    plt.figure(figsize=(8, 6))  # size of the photo
    nx.draw(G, pos, with_labels=True, node_size=node_size, node_color='w', node_shape='.')

    color_list = ['pink', 'orange', 'r', 'g', 'b', 'y', 'm', 'gray', 'black', 'c', 'brown']
    # node_shape = ['s','o','H','D']

    for i in range(len(com)):
        nx.draw_networkx_nodes(G, pos, nodelist=com[i], node_color=color_list[i])
    plt.show()


if __name__ == "__main__":
    G = nx.karate_club_graph()  #

    # Kl algorithm
    com = list(kernighan_lin_bisection(G))
    print('Community Quantity', len(com))
    print(com)
    draw_spring(G, com)