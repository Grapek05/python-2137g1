def print_seats(seats):
    """Funkcja wyświetla aktualny stan rezerwacji miejsc."""
    for idx, seat in enumerate(seats, start=1):
        if seat is None:
            print(f"Miejsce {idx}: Wolne")
        else:
            print(f"Miejsce {idx}: Zarezerwowane przez {seat}")

def add_reservation(seats):
    """Funkcja dodaje rezerwację pojedynczego miejsca."""
    try:
        name = input("Podaj swoje imię: ")
        seat_number = int(input("Podaj numer miejsca do rezerwacji (1-10): "))
        if seat_number < 1 or seat_number > 10:
            print("Numer miejsca jest poza zakresem (dostępne miejsca to 1-10).")
            return
        if seats[seat_number - 1] is not None:
            print(f"Miejsce {seat_number} jest już zarezerwowane.")
        else:
            seats[seat_number - 1] = name
            print(f"Miejsce {seat_number} zostało zarezerwowane na nazwisko {name}.")
    except ValueError:
        print("Podano nieprawidłowy numer miejsca.")

def remove_reservation(seats):
    """Funkcja usuwa rezerwację miejsca."""
    try:
        seat_number = int(input("Podaj numer miejsca do zwolnienia (1-10): "))
        if seat_number < 1 or seat_number > 10:
            print("Numer miejsca jest poza zakresem (dostępne miejsca to 1-10).")
            return
        if seats[seat_number - 1] is None:
            print(f"Miejsce {seat_number} nie jest zarezerwowane.")
        else:
            print(f"Rezerwacja na miejscu {seat_number} została anulowana.")
            seats[seat_number - 1] = None
    except ValueError:
        print("Podano nieprawidłowy numer miejsca.")

def modify_reservation(seats):
    """Funkcja modyfikuje istniejącą rezerwację."""
    try:
        seat_number = int(input("Podaj numer miejsca, które chcesz zmienić (1-10): "))
        if seat_number < 1 or seat_number > 10:
            print("Numer miejsca jest poza zakresem (dostępne miejsca to 1-10).")
            return
        if seats[seat_number - 1] is None:
            print(f"Miejsce {seat_number} nie jest zarezerwowane.")
            return
        
        old_name = seats[seat_number - 1]
        new_seat_number = int(input("Podaj nowy numer miejsca do przeniesienia rezerwacji (1-10): "))
        if new_seat_number < 1 or new_seat_number > 10:
            print("Numer nowego miejsca jest poza zakresem (dostępne miejsca to 1-10).")
            return
        if seats[new_seat_number - 1] is not None:
            print(f"Miejsce {new_seat_number} jest już zarezerwowane.")
        else:
            seats[seat_number - 1] = None
            seats[new_seat_number - 1] = old_name
            print(f"Rezerwacja na miejscu {seat_number} została przeniesiona na miejsce {new_seat_number}.")
    except ValueError:
        print("Podano nieprawidłowy numer miejsca.")

def check_availability(seats):
    """Funkcja sprawdza dostępność wielu miejsc."""
    try:
        seat_numbers = input("Podaj numery miejsc do sprawdzenia dostępności (oddzielone przecinkami): ")
        seat_numbers = [int(x) for x in seat_numbers.split(",")]
        for seat_number in seat_numbers:
            if seat_number < 1 or seat_number > 10:
                print(f"Numer miejsca {seat_number} jest poza zakresem (dostępne miejsca to 1-10).")
                continue
            if seats[seat_number - 1] is None:
                print(f"Miejsce {seat_number} jest wolne.")
            else:
                print(f"Miejsce {seat_number} jest zarezerwowane przez {seats[seat_number - 1]}.")
    except ValueError:
        print("Podano nieprawidłowy format numerów miejsc.")

def add_multiple_reservations(seats):
    """Funkcja dodaje rezerwacje wielu miejsc naraz."""
    try:
        name = input("Podaj swoje imię: ")
        seat_numbers = input("Podaj numery miejsc do rezerwacji (oddzielone przecinkami): ")
        seat_numbers = [int(x) for x in seat_numbers.split(",")]
        
        # Sprawdzamy dostępność wszystkich miejsc
        available = all(seats[seat_number - 1] is None for seat_number in seat_numbers)
        
        if available:
            for seat_number in seat_numbers:
                if seat_number < 1 or seat_number > 10:
                    print(f"Numer miejsca {seat_number} jest poza zakresem (dostępne miejsca to 1-10).")
                    continue
                seats[seat_number - 1] = name
            print(f"Miejsca {', '.join(map(str, seat_numbers))} zostały zarezerwowane na nazwisko {name}.")
        else:
            print("Niektóre z wybranych miejsc są już zarezerwowane.")
    except ValueError:
        print("Podano nieprawidłowy format numerów miejsc.")

def cancel_all_reservations(seats):
    """Funkcja usuwa wszystkie rezerwacje danego użytkownika."""
    name = input("Podaj swoje imię, aby anulować wszystkie rezerwacje: ")
    for idx, seat in enumerate(seats):
        if seat == name:
            seats[idx] = None
    print(f"Wszystkie rezerwacje na nazwisko {name} zostały anulowane.")

def main():
    """Główna funkcja programu, która umożliwia wybór opcji przez użytkownika."""
    seats = [None] * 10  # Inicjalizacja listy 10 miejsc
    while True:
        print("\nMenu:")
        print("1. Wyświetl stan rezerwacji")
        print("2. Dodaj rezerwację")
        print("3. Usuń rezerwację")
        print("4. Modyfikuj rezerwację")
        print("5. Wyjście")
        print("6. Sprawdź dostępność miejsc")
        print("7. Rezerwacja wielu miejsc")
        print("8. Anulowanie wszystkich rezerwacji")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            print_seats(seats)
        elif choice == "2":
            add_reservation(seats)
        elif choice == "3":
            remove_reservation(seats)
        elif choice == "4":
            modify_reservation(seats)
        elif choice == "5":
            print("Do widzenia!")
            break
        elif choice == "6":
            check_availability(seats)
        elif choice == "7":
            add_multiple_reservations(seats)
        elif choice == "8":
            cancel_all_reservations(seats)
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")

if __name__ == "__main__":
    main()
