
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
values = [60, 100, 120] # wartosci
weights = [10, 20, 30] # wagi
capacity = 50 # pojemnosc plecaka

# Wywołanie funkcji
max_value = knapsack(values, weights, capacity)
print("Maksymalna wartość, którą można umieścić w plecaku:" , max_value)