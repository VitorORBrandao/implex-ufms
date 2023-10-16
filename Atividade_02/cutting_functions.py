def bottom_up_cut_rod(prices, n):
    # Inicialize um array para armazenar os valores máximos
    max_values = [0] * (n + 1)
    
    for i in range(1, n + 1):
        max_value = -float("inf")
        for j in range(1, i + 1):
            max_value = max(max_value, prices[j] + max_values[i - j])
        max_values[i] = max_value
    
    return max_values[n]


def greedy_cut_rod(prices, n):
    if n <= 0:
        return 0
    
    max_value = -float("inf")
    for i in range(1, n + 1):
        max_value = max(max_value, prices[i] + greedy_cut_rod(prices, n - i))
    
    return max_value