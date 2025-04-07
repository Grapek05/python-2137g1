graph = {
    'A':{'B': 4, 'C': 2},
    'B':{'D': 1, 'C': 5},
    'C':{'D': 8, 'F': 2},
    'D':{'F': 2},
    'F':{}
}

def dijkstra():
#ustawiamy wierzchołki na nieskonczoność
# pierwszy (start) jest równy 0

# petla dla nie odwiedzonych wierzcholkow

    # wybieramy wierzcholek o najmniejszej wartosci

    # jezeli nie ma innych wierzcholkow to wychodzimy



    # sprawdzamy sasiadów wybranego wierzchołka

        # jesli trasa jest któtsza to aktualizujemy

    # zaznaczamy wierzchołek odwiedzony

    # zwroc dystans
    return

#wywolanie

short_path = dijkstra(graph, 'A')
print (short_path)