import os
from time import time
from random import randint


def generate_random_prices(length):
    # Inicializa a lista de preços com 0 para garantir que estamos considerando todos os possíveis tamanhos de haste
    array = []
    array.append(0)
    
    # Loop para gerar os valores aleatórios entre 1 e 10
    for _ in range(length):
        array.append(randint(1, 10))

    return array


def calculate_execution_time_and_result(cutting_function, prices, n):
  initial_time = time() # Registra o tempo inicial
  result = cutting_function(prices, n) # Chama a função de corte e salva na variável "result"
  end_time = time()  # Registra o tempo final
  
  # Retorna o resultado e o tempo de execução em segundos
  return result, end_time - initial_time


def create_empty_file(file_name):
  # Verificar se o arquivo existe
  if os.path.exists(file_name):
    # Se o arquivo existe, deleta ele
    os.remove(file_name)
  
  # Cria um novo arquivo vazio
  with open(file_name, 'w'):
    pass