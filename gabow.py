class Gabow:
    """
    A class to compute scc in a graph using Gabow's algorithm
    """

    def __init__(self, graph):
        """
        Initialize all the class variable to launch Gabow's algorithm on a graph
        :param graph: the graph on which we want to launch Gabow's algorithm
        :return: all the class variables are initialized for the graph
        """
        self.graph = graph
        self.S = []
        self.P = []
        self.preorder = [-1 for i in graph.keys()]
        self.in_scc = [0 for i in graph.keys()]
        self.scc = []
        self.preorder_number = 0

    def reset(self, graph):
        """
        Resets all the class variable to launch Gabow's algorithm on a new graph
        :param graph: the graph on which we want to launch Gabow's algorithm
        :return: all the class variables are initialized for the new graph
        """
        self.graph = graph
        self.S = []
        self.P = []
        self.preorder = [-1 for i in graph.keys()]
        self.in_scc = [0 for i in graph.keys()]
        self.scc = []
        self.preorder_number = 0

    def launching_gabow(self):
        """
        Launches Gabow's algorithm on the graph stored
        :return: an array of the scc contained in the graph
        """
        for i in self.graph.keys():
            if (self.preorder[i] == -1):
                self.visit(i)
        return self.scc

    def visit(self, node):
        """
        Recursive function used to visit each node of the graph (just like a dfs)
        :param node: the node that we are currently visiting
        :return: an updated P and S stack, and an array for the preorder of each node stored and possibly a scc
        """
        # we update the preorder number on the node and add it to both the P and S stack
        self.preorder[node] = self.preorder_number
        self.preorder_number += 1
        self.P.append(node)
        self.S.append(node)
        for i in self.graph[node]:
            # for each neighbor node, we visit it if it hasn't been already
            if (self.preorder[i] == -1):
                self.visit(i)
            # or if it isn't in a scc and it has smaller preorder number than the top of the stack P
            # we pop elements until it isn't the case anymore
            elif (self.in_scc[i] == 0):
                while self.preorder[self.P[-1]] > self.preorder[i]:
                    self.P.pop()

        # we simply create the scc from the two stacks that we have
        # we pop elements from the stack S until we find the one that's equal to the top of P
        if (node == self.P[-1]):
            current_scc = ""
            w = -1
            while (w != node):
                w = self.S.pop()
                self.in_scc[w] = 1
                # current_scc += chr(w + 97) # results as char from a-z
                current_scc += " " + str(w)
            self.scc.append(current_scc.lstrip())
            self.P.pop()