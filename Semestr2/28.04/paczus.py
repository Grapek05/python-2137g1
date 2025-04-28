def paczkiCzwartkowe(values, weights, capacity, names):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Wypełnianie tablicy DP
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    w = capacity
    selected = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected.append(i-1)
            w -= weights[i-1]

    # Tworzymy tablicę dla pączków, które zostały wybrane
    print("Są to pączki:")
    for paczek in selected:
        print(f"    {names[paczek]}")

    return dp[n][capacity]

names = ["Pączek wiśniowy", "Fit pączek gryczany ze śliwkami", "Pączek z czekoladą", "Pączek karmelowo-orzechowy", "Oreo donut", "Mini pączek z budyniem"]
values = [252, 205, 315, 441, 630, 126]
weights = [100, 200, 150, 100, 150, 50]
capacity = 500

max_value = paczkiCzwartkowe(values, weights, capacity, names)
print("Maksymalna wartość kalorii:", max_value)
