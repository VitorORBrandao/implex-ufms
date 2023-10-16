def bottom_up_cut_rod(prices, n):
    # Inicialize um array para armazenar os valores máximos
    max_values = [0] * (n + 1)
    
    for i in range(1, n + 1):
        max_value = -float("inf")  # Inicialize o valor máximo com negativo infinito
        
        for j in range(1, i + 1):
            # Para cada pedaço de tamanho j, calcule o valor da tora cortada
            # adicionando o preço do pedaço j ao valor máximo dos pedaços restantes.
            max_value = max(max_value, prices[j] + max_values[i - j])
        
        max_values[i] = max_value  # Armazene o valor máximo calculado para a tora de tamanho i
    
    return max_values[n]  # Retorne o valor máximo obtido para a tora de tamanho n


def greedy_cut_rod(prices, n):
    total_value = 0  # Inicializa o valor total como zero

    while n > 0:
        max_density = -1  # Inicializa a máxima densidade com -1
        best_length = -1  # Inicializa o melhor comprimento com -1

        for length in range(1, n + 1):
            if length <= len(prices):
                density = prices[length] / length  # Calcula a densidade do corte
                if density > max_density:
                    max_density = density  # Atualiza a máxima densidade
                    best_length = length  # Atualiza o melhor comprimento

        if best_length == -1:
            # Se não encontrar um corte válido, sai do loop
            break

        total_value += prices[best_length]  # Adiciona o valor do melhor corte ao valor total
        n -= best_length  # Reduz o tamanho da tora pelo comprimento do melhor corte

    return total_value  # Retorna o valor total obtido com os cortes