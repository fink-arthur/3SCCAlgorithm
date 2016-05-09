class Tarjan:
    """
    A class to compute the scc in a graph using Tarjan's algorithm
    """

    def __init__(self, graph):
        """
        Initialize all the class variable to launch Tarjan's algorithm on a graph
        :param graph: the graph on which we want to launch Tarjan's algorithm
        :return: all the class variables are initialized for the graph
        """
        self.graph = graph
        self.size = len(self.graph.keys())
        self.preorder = [-1 for i in range(self.size)]
        self.low = [-1 for i in range(self.size)]
        self.P = []
        self.in_P = [0 for i in range(self.size)]
        self.preorder_number = 0
        self.scc = []

    def reset(self, graph):
        """
        Resets all the class variable to launch Tarjan's algorithm on a new graph
        :param graph: the graph on which we want to launch Tarjan's algorithm
        :return: all the class variables are initialized for the new graph
        """
        self.graph = graph
        self.size = len(self.graph.keys())
        self.preorder = [-1 for i in range(self.size)]
        self.low = [-1 for i in range(self.size)]
        self.P = []
        self.in_P = [0 for i in range(self.size)]
        self.preorder_number = 0
        self.scc = []

    def launching_tarjan(self):
        """
        Launches Tarjan's algorithm on the graph stored
        :return: an array of the scc contained in the graph
        """
        for i in range(self.size):
            if (self.preorder[i] == -1):
                self.visit(i)
        return self.scc

    def visit(self, node):
        """
        Recursive function used to visit each node of the graph (just like a dfs)
        :param node: the node that we are currently visiting
        :return: an updated array of the preordered and low number of each node stored and possibly a scc
        """
        # we update the preodrder and low number fro the node and add it to the P stack
        self.preorder[node] = self.preorder_number
        self.low[node] = self.preorder_number
        self.preorder_number += 1
        self.P.append(node)
        self.in_P[node] = 1
        for i in self.graph[node]:
            # for each neighboring node we visit it if it hasn't been already
            # and we update the low if the neighboring node has a smaller one
            if (self.preorder[i] == -1):
                self.visit(i)
                self.low[node] = min(self.low[i], self.low[node])
            # otherwise if it isn't in a scc we update the low of the current node
            # with the preorder of the neighbor if it's smaller
            elif (self.in_P[i] == 1):
                self.low[node] = min(self.low[node], self.preorder[i])

        # we create the scc if a nodes preorder is equal to its low after visiting all its neighbors
        if (self.preorder[node] == self.low[node]):
            current_scc = ""
            w = -1
            while (w != node):
                w = self.P.pop()
                self.in_P[w] = 0
                # current_scc += chr(w + 97) # results as char from a-z
                current_scc += " " + str(w)
            self.scc.append(current_scc.lstrip())