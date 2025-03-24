# Algorytm Euklidesa

# funkcja Euk (a,b)
# jezeli liczba a jest rozna od b
# jezeli a > b to od a odejmujemy b
# jezeli b > a to od b odejmujemy a
# zwracamy liczbe a

# def nwd(a, b):
#    while a!= b:
#        if a > b:
#            a -= b
#        else:
#            b -= a
#    return a
# a = int(input("Podaj pierwszą liczbę: "))
# b = int(input("Podaj drugą liczbę: "))
# print(f"Największy wspólny dzielnik liczb {a} i {b} wynosi",nwd(a, b))


def euk(a,b):
    while a!=b:
        if a >b:
            a -=b
        else:
            b-=a

    return a

print ("NWD - odejmowanie iteracyjne 315,504:", euk (315,504) )

def euk_rek(a,b):
    if a == b:
        return a
    if a > b: 
        return euk_rek(a-b, b)
    else:
        return euk_rek(a, b-a)
    
print("NWD - odejmowanie rekurencyjne:", euk_rek(315,504))


# metoda przez dzielenie (modulo)

# Wersja Iteracyjna:

def nwd_mod_iter(a,b):
    #dopoki b nie jest rowne 0
    while b:
        a,b = b,a % b

    return a

print ("NWD mod:", nwd_mod_iter(315,504))

#dodomu:
# wersja rekurencyjna


# test szybkosci wykonywania dzialan dla wszystkich 4 funkcji

test_values = [
    (315, 504),
    (1230, 528),
    (28, 8),
    (12, 18),
    (10000, 1)
]