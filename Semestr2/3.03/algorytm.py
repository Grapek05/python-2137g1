#  Przykład: Znalezienie najwiekszego elementu w liście
#  Poniżej przedstawiam prosty algorytm, który znajduje największy element w zadanej liście liczb:

liczby = [3, 5, 2, 8, 1]

#FUNKCJA znajdzmax(lista):
#    jezeli lista jest pusta to:
#        ustawiamy max [] lub None


#    Dla kazdego elementu z listy
#        jezeli element jest wiekszy od max
#            ustaw max na element
#        zwroc max


def znajdzmax(lista:list[int]) -> int:
    """
    Funkcja przyjmuje liste liczb i zwraca największy element.
    Jesli jest pusta to zwraca None.
    """
    if lista == None:
        return None
    
    max_lista = lista[0]
    for i in lista:
        if i > max_lista:
            max_lista = i

    return max_lista

print("Największa liczba to:", znajdzmax(liczby))
    