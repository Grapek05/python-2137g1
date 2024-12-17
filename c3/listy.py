#Utwórz zmienną napis i przypisz jej tekst "Witaj w Pythonie!". Wyświetl tekst w całości dużymi literami.

napis = "Witaj w Python!"
print(napis.upper())

print(napis.index("W"))

# print(f"{napis:=23}")


owoce = ["jabłko", "gruszka", "banan"]
print(owoce[0])





ile = int(input("Podaj liczbę: "))
for _ in range(5):
    liczba = int(input("Podaj wartosc liczbowa:"))



owoce.append("pomarańcza")
print(owoce)
owoce.remove("gruszka")
print(owoce)

# owoce.reverse()
# print(owoce)
# owoc = owoce.pop(0)
# print(owoc)
owoce.sort()
print(owoce)
# len(owoce)
# ss = list("Witaj")
# print(ss.reverse)
# 
index = owoce.index("pomarańcza")
print(index)


#krotki / tuple

wspolrzedne = (10,(22,23),"Witaj") # z,y,x
print(wspolrzedne[2])

print(wspolrzedne.count(10))
