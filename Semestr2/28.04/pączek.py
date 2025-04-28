
def knapsack(values, weights, capacity):
    # Liczba przedmiotów
    n = len(values)
    # Tworzenie tablicy DP z zerami
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]


    # Wypełnianie tablicy DP
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                # Maksymalna wartość "nie biorąc" bieżącego przedmiotu i "biorąc" bieżący przedmiot
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                # Przeniesienie poprzedniej wartości, jeśli waga bięzącego przedmiotu jest za duża
                dp[i][w] = dp[i-1][w]


    # Maksymalna wartość, która może być przeniesiona w plecaku
    return dp[n][capacity]


# Dane wejściowe
values = [126, 252, 441, 315, 630, 205] # wartosci
weights = [50, 100, 100, 150, 150, 200] # wagi
capacity = 500 # pojemnosc plecaka

# Wywołanie funkcji
max_value = knapsack(values, weights, capacity)
print("Maksymalna wartość, którą można umieścić w plecaku:" , max_value)


#pączki = ["paczek wiśniowy ok.100g, fit paczek gryczany ze sliwkami ok.200g, paczek z czekolada ok.150g, paczek z karmelowo-orzechowy ok.100g, oreo donut, ok.150g mini paczek z budyniem ok.50g"]

#def paczus_sort(arr, min_val, max_val):
#    count = [0] * (max_val - min_val + 1)
#    for paczus in arr:
#        count[paczus - min_val] += 1
#    sorted_paczus = []
#    for i in range(len(count)):
#        sorted_paczus.extend([i + min_val] * count[i])
#    return sorted_paczus

#sorted_oceny = paczus_sort(pączki, 0, 100)
#print(sorted_oceny)

