#zmienne i stale

seats = [None]*10


def add_reservation(seats: list):
    """" Wyświetlanie aktualnego stanu rezerwacji miejsc """
    while True:
        n = input("Podaj numer siedzenia: ")
        if(n.isnumeric() == True):
            if int(n) < len(seats) and int(n)  > 0:
                break
            else:
                print(f"Numer miejsca musi mieścić się między 1 i {len(seats)}.")
        else:
            print("Numer miejsca musi być liczbą")
    numerMiejsca = int(n)
    n = input("Podaj swoje imie: ")       
    imie = n
    if seats[numerMiejsca] ==None:
        seats[numerMiejsca-1] = imie
        print("Pomyslnie dodano rezerwacje")
    else:
        print("Miejsce jest już zajęte przez inną osobę")

def remove_reservation(seats):
    while True:
        n = input("Podaj numer siedzenia: ")
        if(n.isnumeric() == True):
            if(int(n) < len(seats) and int(n)  > 0):
                break
            else:
                print(f"Numer miejsca musi mieścić się między 1 i {len(seats)}.")
        else:
            print("Numer miejsca musi być liczbą")
    numerMiejsca = int(n)
    seats[numerMiejsca-1] = None
    print("Pomyslnie usunieto rezerwacje")

def modify_reservation(seats:list):
    """ Modyfikacje rezerwacji """

    while True:
        n = input("Podaj numer siedzenia: ")
        if(n.isnumeric() == True):
            if(int(n) < len(seats) and int(n)  > 0):
                break
            else:
                print(f"Numer miejsca musi mieścić się między 1 i {len(seats)}.")
        else:
            print("Numer miejsca musi być liczbą")
        zMiejsca = int(n)
        if seats[zMiejsca-1] == None:
            print(f"To miejsce jest puste")

    while True:
        n = input("Podaj nowy numer siedzenia: ")
        if(n.isnumeric() == True):
            if(int(n) < len(seats) and int(n)  > 0):
                break
            else:
                print(f"Numer miejsca musi mieścić się między 1 i {len(seats)}.")
        else:
            print("Numer miejsca musi być liczbą")
        doMiejsca = int(n)
        if seats[doMiejsca-1] != None:
            print(f"To miejsce jest już zajęte")

    seats[doMiejsca-1] =seats[zMiejsca-1]
    seats[zMiejsca-1]= None
    print("Pomyslnie zmodyfikowano rezerwacje")
    


def print_seats(seats: list):
    j=1
    for i in seats:
        if i in seats:
            if i==None:
                print(f"{j} wolne")
            else:
                print(f"{j} jest zajęte przez {i}")
            j+=1

    #for i in range(1,11):
    #    if(seats[i] == "None"):
    #        print(f"{i} -> Wolne")
    #    else:
    #        print(f"{i} -> {seats[i]}")
            
def check_availability(seats):
    while True:
        check_if_numbers = True
        check_if_inRange = True
        n = input("Podaj liste numerow siedzen (numery oddzielone spacja): ")
        n = n.split(" ")
        print(n)
        for i in range(len(n)):
            if(n[i].isnumeric() == False):
                check_if_numbers = False
            elif(int(n[i]) <=0 or int(n[i]) >10):
                check_if_inRange = False
        if(check_if_numbers):
            if(check_if_inRange):
                break
            else:
                print("Numer miejsca musi mieścić się między 1 i 10.")    
        else:
            print("Numer miejsca musi być liczbą") 
    for i in n:
        if(seats[int(i)] == 'None'):
            print(f"{int(i)} -> Wolne")
        else:
            print(f"{int(i)} -> Zajęte")

def add_multiple_reservations(seats):
    while True:
        check_if_numbers = True
        check_if_inRange = True
        seatIsAvailable = True
        n = input("Podaj liste numerow siedzen (numery oddzielone spacja): ")
        n = n.split(" ")
        print(n)
        for i in range(len(n)):
            if(n[i].isnumeric() == False):
                check_if_numbers = False
            elif(int(n[i]) <=0 or int(n[i]) >10):
                check_if_inRange = False
        if(check_if_numbers):
            if(check_if_inRange):
                break
            else:
                print("Numer miejsca musi mieścić się między 1 i 10.")    
        else:
            print("Numer miejsca musi być liczbą")
    imie = input("Podaj swoje imie: ") 
    for i in n:
        if(seats[int(i)] != 'None'):
            seatIsAvailable = False
    if(seatIsAvailable):
        for i in n:
            seats[int(i)] = imie
            print("Pomyslnie dodano rezerwacje")
    else:
        print("Podane miejsca sa juz zajete")

def cancel_all_reservations(seats):
    p = 0
    imie = input("Podaj swoje imie: ") 
    for i in range(1, 11):
        print(seats[i])
        if(seats[i] == imie):
            seats[i] = 'None'
            p = p + 1
    if(p > 0):
        print("Pomysle usunieto rezerwacje")
    else:
        print(f"Nie znaleziono rezerwacji pod imieniem: {imie}")
    
            


seats = {1:"None", 2:"None", 3:"None", 4:"None", 5:"None", 6:"None", 7:"None", 8:"None", 9:"None", 10:"None",}

def main():
    while True:
        print("")
        print("1. Wyświetlanie aktualnego stanu rezerwacji miejsc")
        print("2. Dodawanie nowej rezerwacji")
        print("3. Usuwanie istniejącej rezerwacji")
        print("4. Modyfikacja istniejącej rezerwacji")
        print("5. Wyjście z programu")
        print("6. Sprawdzenie dostępności wielu miejsc")
        print("7. Rezerwacja wielu miejsc naraz")
        print("8. Anulowanie wszystkich rezerwacji")
        print("")
        n = input("") 
        if(n == '1'): 
            print_seats(seats) 
        if(n == '2'): 
            add_reservation(seats) 
        if(n == '3'): 
            remove_reservation(seats) 
        if(n == '4'): 
            modify_reservation(seats) 
        if(n == '5'): 
            break
        if(n == '6'): 
            check_availability(seats)
        if(n == '7'): 
            add_multiple_reservations(seats)
        if(n == '8'): 
            cancel_all_reservations(seats)
main()