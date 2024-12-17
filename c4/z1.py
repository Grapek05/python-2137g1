# Przechodzimy po wszystkich liczbach w zakresie od 100 do 999
for num in range(100, 1000):
    # Rozdzielamy liczbę na cyfry
    a = num // 100       # Pierwsza cyfra (setki)
    b = (num // 10) % 10 # Druga cyfra (dziesiątki)
    c = num % 10         # Trzecia cyfra (jedności)
    
    # Sprawdzamy, czy liczba jest liczbą Armstronga
    if a**3 + b**3 + c**3 == num:
        print(num)
