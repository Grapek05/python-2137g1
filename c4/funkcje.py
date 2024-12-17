

def suma(x, y):
    return(x+y)

#print (suma(2,3))

#x=10
#PI = 3.14
# Oblicz pole koła pi*r^2 pi*r*r
#def pole_kola(r:float) -> float:
#    """
#     Funkcja licząca pole koła
#    """
#    x=15
#    return PI *r**2


#print(f"Pole koła wynosi : {pole_kola(5)}")
#print(f"Pole koła wynosi : {pole_kola(5.1)}")
#print(f"Pole koła wynosi : {pole_kola(5.2)}")
# print(f"Pole koła wynosi : {pole_kola(rrr)}")
#print(x)



def witaj(imie:str, powitanie:str = "Cześć")->str:
    if suma(5,4):
        return "Jesteś pełnoletni"
    else:
        return f"{powitanie}, {imie} jesteś na PW."

print(witaj(powitanie ="Hej" ,imie="Kubulek"))


def silnia(n:int)->int:
    if n==0:
        return 1
    return n * silnia(n-1)

print(silnia(5))



def pi()->float:
    return 3.14

print(pi())


def suma_wielu(*args)->int:
    return sum(args)

print(suma_wielu(5,6,32,4545,356))
print(suma_wielu(5,6))


# funkcja filtrująca liczby parzyste (we:listam wy:lista)

def filtruj_parzyste(liczby:list[int]) -> list[int]:
    return [num for num in liczby if num%2 == 0]
    #wynik = []
    #for liczba in liczby:
    #    if liczba % 2 == 0:
    #        wynik.append(liczba)

    #return wynik

print(filtruj_parzyste([10,11,12,13,14]))