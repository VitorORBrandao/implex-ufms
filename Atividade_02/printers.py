from cutting_functions import bottom_up_cut_rod, greedy_cut_rod
from helpers import generate_random_prices, calculate_execution_time_and_result


def print_and_save(message):
  # Imprime a mesnagem no console
  print(message)

  with open("results.txt", "a") as f:
    # Escreve a mensagem no arquivo
    f.write(message + "\n")


def output_metrics(initial_size, final_size, steps):
  # Cabeçalho para a saída de dados
  header = "N \t vDP \t\t tDP \t\t vGreedy \t tGreedy \t %"
  print_and_save(header)

  # Loop através de diferentes tamanhos de array (hastes)
  for rod_length in range(initial_size, final_size + 1, steps):
    # Gera a lista de preços para esse determinado tamanho de haste
    prices_by_length = generate_random_prices(rod_length)

    # variáveis para armazenar os valores obtidos dos algoritmos
    dp_result, time_dp = calculate_execution_time_and_result(bottom_up_cut_rod, prices_by_length, rod_length)
    greedy_result, time_greedy = calculate_execution_time_and_result(greedy_cut_rod, prices_by_length, rod_length)

    # Apresenta os valores obtidos e calcula a porcentagem de diferença entre as abordagens
    print_and_save(f"{rod_length} \t {dp_result} \t\t {time_dp:.4f} \t {greedy_result} \t\t {time_greedy:.4f} \t {(greedy_result / dp_result) * 100:.2f}%")