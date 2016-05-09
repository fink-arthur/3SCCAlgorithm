import random


def dfs(graph, start, visited, path):
    """
    Launches only one dfs from the start node in the graph
    :param graph: the graph in which you want to launch a dfs
    :param start: the starting node
    :param visited: the nodes already visited by the dfs
    :param path: the path the dfs has taken
    :return: a path taken in the graph by a dfs starting from a certain node
    """
    visited[start] = 1
    for i in graph[start]:
        if (visited[i] == 0):
            dfs(graph, i, visited, path)
    path.append(start)
    return path, visited


def full_dfs(graph):
    """
    Launches a full dfs in the graph visiting every node
    :param graph: the graph in which you want to launch a dfs
    :return: a path taken in the graph by a dfs from a certain node visiting every nodes
    """
    visit = [0 for i in graph.keys()]
    res = []

    for i in graph.keys():
        if (visit[i] == 0):
            (res, visit) = dfs(graph, i, visit, res)

    return res


def reverse_succ(succ):
    """
    Reverses a graph
    :param succ: a graph represented using a dictionary
    :return: the inverse graph represented using a dictionary
    """
    size = len(succ.keys())
    res = {x: [] for x in range(size)}
    for i in succ.keys():
        for j in succ[i]:
            res[j].append(i)

    return res


def generate(nodes, vertex):
    """
    Generates graph with a certain number of nodes and vertex from each node
    :param nodes: the number of nodes the generated graph will have
    :param vertex: the number of vertex each node will have in the generated graph
    :return: a graph represented using a dictionary
    """
    g = {key: [] for key in range(nodes)}
    for i in range(nodes):
        l = [j for j in range(nodes)]
        neighbors = []
        while (len(neighbors) < vertex):
            neighbors.append(l.pop(random.randint(0, len(l) - 1)))

        g[i].extend(neighbors)

    return g


def random_generate(nodes):
    """
    Generates a graph with a certain number of nodes and a random of vertex per nodes
    :param nodes: the number of nodes the generated graph will have
    :return: a graph represented using a dictionary
    """
    g = {key: [] for key in range(nodes)}
    v = 0
    for i in range(nodes):
        l = [j for j in range(nodes)]
        neighbors = []
        r = random.randint(0.1 * nodes, 0.8 * nodes)
        v += r
        while (len(neighbors) < r):
            neighbors.append(l.pop(random.randint(0, len(l) - 1)))

        g[i].extend(neighbors)

    return g, v