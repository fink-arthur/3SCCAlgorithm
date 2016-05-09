import kosaraju
import tarjan
import gabow

if '__main__' == __name__:

    ######################
    # Test n. 1          #
    ######################

    print("Test n.1")
    print("scc = {[0 4 1], [3 7 2], [5 6]}")
    # scc = {aeb, dhc, fg}
    graph = {
        0: [1],
        1: [2, 4, 5],
        2: [3, 6],
        3: [2, 7],
        4: [0, 5],
        5: [6],
        6: [5],
        7: [3, 6]
    }

    t = tarjan.Tarjan(graph)
    print("Tarjan: ", end="")
    print(t.launching_tarjan())

    k = kosaraju.Kosaraju(graph)
    print("Kosaraju: ", end="")
    print(k.launching_kosaraju())

    g = gabow.Gabow(graph)
    print("Gabow: ", end="")
    print(g.launching_gabow())
    print()

    ######################
    # Test n. 2          #
    ######################

    print("Test n.2")
    print("scc = {[0], [5 2], [6 4 3 1]}")
    # scc = {a, fc, gedb}
    graph2 = {
        0: [1],
        1: [2,3,6],
        2: [5],
        3: [1,4],
        4: [5,6],
        5: [2],
        6: [3]
    }

    t2 = tarjan.Tarjan(graph2)
    print("Tarjan: ", end="")
    print(t2.launching_tarjan())

    k2 = kosaraju.Kosaraju(graph2)
    print("Kosaraju: ", end="")
    print(k2.launching_kosaraju())

    g2 = gabow.Gabow(graph2)
    print("Gabow: ", end="")
    print(g2.launching_gabow())
    print()

    ######################
    # Test n. 3          #
    ######################

    print("Test n.3")
    print("scc = {[0], [1 2 3 4], [5 6 7]}")
    # cfc = {a, bcde, fgh}
    graph3 = {
        0: [1],
        1: [2,3],
        2: [3,5],
        3: [4],
        4: [1,5],
        5: [6],
        6: [7],
        7: [5]
    }

    t3 = tarjan.Tarjan(graph3)
    print("Tarjan: ", end="")
    print(t3.launching_tarjan())

    k3 = kosaraju.Kosaraju(graph3)
    print("Kosaraju: ", end="")
    print(k3.launching_kosaraju())

    g3 = gabow.Gabow(graph3)
    print("Gabow: ", end="")
    print(g3.launching_gabow())
