import utils
import kosaraju
import tarjan
import gabow
import time
import sys

if '__main__' == __name__:

    sys.setrecursionlimit(1500)

    graph = dict()

    t = tarjan.Tarjan(graph)
    k = kosaraju.Kosaraju(graph)
    g = gabow.Gabow(graph)

    for i in range(10, 1000, 10):
        repetitions = 10
        t_counter = 0
        k_counter = 0
        g_counter = 0

        # generator for a graph with a fixed number of vertex per node
        nodes = i
        vertex_per_nodes = i * 0.8
        total = nodes + (nodes * vertex_per_nodes)
        gr = utils.generate(nodes, vertex_per_nodes)

        # generator for a graph with a random of vertex per node
        # nodes = i
        # gr, v = utils.random_generate(i)
        # total = nodes + v

        for j in range(repetitions):
            t.reset(gr)
            k.reset(gr)
            g.reset(gr)

            t_start = time.perf_counter()
            t.launching_tarjan()
            t_stop = time.perf_counter()

            k_start = time.perf_counter()
            k.launching_kosaraju()
            k_stop = time.perf_counter()

            g_start = time.perf_counter()
            g.launching_gabow()
            g_stop = time.perf_counter()

            t_counter = t_stop - t_start
            k_counter = k_stop - k_start
            g_counter = g_stop - g_start

        print('{} {} {} {}'.format(total, t_counter / repetitions, k_counter / repetitions, g_counter / repetitions))
