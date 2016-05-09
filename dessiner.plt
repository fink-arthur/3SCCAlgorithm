set terminal postscript
set output '|ps2pdf - exo2.pdf'
set title "Comparaison d'algorithme de CFC sur graphe quelconque"
set xlabel "V + E"
set ylabel "t (s)"
set key left top
plot "res.txt" using 1:2 with linespoints linecolor 1 title "Tarjan",\
    "res.txt" using 1:3 with linespoints linecolor 2 title "Kosaraju",\
    "res.txt" using 1:4 with linespoints linecolor 3 title "Gabow"
