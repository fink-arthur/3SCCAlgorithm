import utils


class Kosaraju:
    """
    A class to compute the scc in a graph with Kosaraju's algorithm
    """

    def __init__(self, graph):
        """
        Initialize all the class variable to launch Kosaraju's algorithm on a graph
        :param graph: the graph on which we want to launch Kosaraju's algorithm
        :return: all the class variables are initialized for the graph
        """
        self.graph = graph
        self.visited = [0 for i in self.graph.keys()]

    def reset(self, graph):
        """
        Resets all the class variable to launch Kosaraju's algorithm on a new graph
        :param graph: the graph on which we want to launch Kosaraju's algorithm
        :return: all the class variables are initialized for the new graph
        """
        self.graph = graph
        self.visited = [0 for i in self.graph.keys()]

    def launching_kosaraju(self):
        """
        Launches Kosaraju on the graph stored
        :return: an array of the scc contained in the graph
        """
        # we launch the first dfs on the graph and then we reverse the graph
        dfs_result = utils.full_dfs(self.graph)
        reverse_graph = utils.reverse_succ(self.graph)
        scc = []

        # while we haven't visited every node from the dfs result we launch a dfs on the inversed graph
        # starting from the node at the top of the stack (the dfs result) and we create a scc from all
        # nodes visited
        while (len(dfs_result) > 0):
            node = dfs_result.pop()
            (res, self.visited) = utils.dfs(reverse_graph, node, self.visited, [])
            current_scc = ""
            for i in res:
                current_scc += str(i) + " "
                # current_scc += chr(i + 97) # results as char from a-z
                if (node != i):
                    # complexity in O(n) could cost some performance loss for remove
                    # but both remove and pop give the same results on my small test cases
                    # and when plotting complexity both take the same time
                    dfs_result.remove(i)
                    # dfs_result.pop()

            scc.append(current_scc.rstrip())

        return scc