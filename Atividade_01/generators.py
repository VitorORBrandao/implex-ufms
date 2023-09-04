from random import randint


def generate_random_array(length):
  # Cria uma lista vazia para armazenar os números aleatórios
  array = []
  
  # Loop para gerar N números aleatórios entre 0 e 20000
  for _ in range(length):
    array.append(randint(0, 20000))
  
  return array


def generate_sorted_array(length):
  # Gera um array aleatório de inteiros usando a função generate_random_array
  array = generate_random_array(length)
  # Ordena o array em ordem crescente
  array.sort()
  
  return array


def generete_reverse_array(length):
  # Gera um array ordenado em ordem crescente usando a função generate_sorted_array
  array = generate_sorted_array(length)
  # Inverte o array para ordem decrescente
  array.reverse()
  
  return array


def generate_nearly_sorted_array(length):
  # Gera um array ordenado em ordem crescente usando a função generate_sorted_array
  array = generate_sorted_array(length)

  # Troca aleatoriamente 10% dos elementos do array
  for _ in range(int(length * 0.1)):
    i = randint(0, length-1)
    j = randint(0, length-1)
    array[i], array[j] = array[j], array[i]
  
  return array