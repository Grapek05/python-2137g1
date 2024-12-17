print("Witaj na PW - zajęcia 2")


# Zadanie 1: Napisz program, który przypisze do zmiennych liczbę całkowitą i tekst, a następnie wypisze te dane na ekran.

liczba = 10
tekst = "Hello, Python"

print("Liczba", liczba)
print("Tekst", tekst, liczba)

# Zadanie 2: Zadeklaruj zmienną z liczbą zmiennoprzecinkową i tekstem a następnie wypisz oba elementy w jednym ciągu zdaniowym.

liczba_zmiennoprzecinkowa = 3.14
tekst = "Wartość liczby pi to:"
print(f"{tekst} {liczba_zmiennoprzecinkowa}")

# Zadanie 3: Wypisz na ekranie sumę dwóch liczb oraz komunikat z wynikiem w formie: "Suma liczb 5 i 10 wynosi 15".
liczba1 = 15
liczba2 = 40
suma = liczba1 + liczba2
print(f"Suma liczb {liczba1} i {liczba2} wynosi {suma}")

# Zadanie 4: Wczytaj od użytkownika dwie liczby i oblicz ich iloczyn, róźnicę oraz iloraz.

liczba1 = float(input("Podaj pierwsza liczba: "))
liczba2 = float(input("Podaj druga liczba: "))

iloczyn = liczba1 * liczba2

roznica = liczba1 - liczba2

iloraz = liczba1 / liczba2 if liczba2 !=0 else "Dzielenie przez zero"

#if liczba2 !=0:
#    iloraz = liczba / liczba2
#else:
#    iloraz = "Dzielenie przez zero"

print(f"Iloraz: {iloraz}")

# Zadanie 5: Wczytaj ciąg znaków, który reprezentuje liczbę zmiennoprzecinkową, przekonwertuj go i oblicz pierwiastek kwadratowy z tej liczby.
import math

# Zadanie: Napisz program, który wczyta od użytkownika tekst, a następnie wypisze długość tego tekstu.


# Zadanie: Wczytaj od użytkownika słowo oraz literę, a następnie znajdź pozycję tej litery w podanym słowie. Jeśli litery nie ma, poinformuj o tym użytkownika