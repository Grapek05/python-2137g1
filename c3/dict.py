tablica = {"klucz": "wartosc"}


osoba = {
    "name" : "Jan",
    "wiek" : 56,
    "miasto": "Warszawa"

}
print(osoba["miasto"])
print(osoba.get("pesel", "Brak peselu"))
osoba['pesel'] = 88121354321
osoba['miasto'] = "Poznań"

print(osoba)

del osoba["miasto"]
print(osoba)

# wiek = osoba.pop("wiek")
# print(wiek)
# print(osoba)
# osoba.clear()
# print(osoba)

osoba1 = osoba.copy()

if "wiek" in osoba:
    print("Klucz wiek istnieje")


for key, value in osoba.items():
    print(value)

osoba = {
    "person1" : {"name":"Jan", "wiek":33},
    "pesrson2" : {"name":"Krzyś", "wiek":23}
}

osoba["person1"]['wiek']

print(osoba.items())

osoba.update({"pesrson3" : {"name":"Józef", "wiek":56}})
print(osoba.items())


czypada = True
czypada = not czypada
if czypada == True:
    print("Pada")
else:
    print("Nie pada")

