# Znajdowanie dzielników i sprawdzanie pierwszości liczby
# znajdowanie dzielników
# cel: znajeźć wszystkie liczby, które dzielą się przez n, bez reszty

#import timeit
#import math

#def znajdz_dzielnik1(n:int):
#    table = []
#    for i in range(1, n + 1):
#        if n % i == 0:
#            table.append(i)
#    return table

#def znajdz_dzielnik2(n:int):
#    return [i for i in range(1, n + 1) if n % i == 0]

#def znajdz_dzielnik3(n: int):
#    table = set()
#    for i in range(1, int(math.sqrt(n)) + 1):
#        if n % i == 0:
#            table.add(i)
#            table.add(n // i)
#    return sorted(table)

# drugi największy element
#def znajdz_dzielnik4(n: int):
#    for i in range(n // 2, 0, -1):
#        if n % i == 0:
#            return i

# print(znajdz_dzielnik1(100))
# print(znajdz_dzielnik2(100))
#print(znajdz_dzielnik3(100))
#print(znajdz_dzielnik4(12))

#n = 10**6
#print(f"Czas wykonania funkcji #1: {timeit.timeit(lambda: znajdz_dzielnik1(n), number=10)}s")
#print(f"Czas wykonania funkcji #2: {timeit.timeit(lambda: znajdz_dzielnik2(n), number=10)}s")
#print(f"Czas wykonania funkcji #3: {timeit.timeit(lambda: znajdz_dzielnik3(n), number=10)}s")
#print(f"Czas wykonania funkcji #4: {timeit.timeit(lambda: znajdz_dzielnik4(n), number=10)}s")

# pseudokod

