import helpers


# Função de ordenação Selection Sort
def selection_sort(arr):
  # Percorre a lista 
  for i in range(len(arr)):
    # Assume que o índice atual é o mínimo
    min_index = i
  
    # Itera através dos elementos restantes para encontrar o mínimo
    for j in range(i+1, len(arr)):
      if arr[j] < arr[min_index]:
        min_index = j

    # Troca o elemento mínimo encontrado com o elemento na posição 'i'
    arr[i], arr[min_index] = arr[min_index], arr[i]
 

# Função de ordenação Insertion Sort
def insertion_sort(arr):
  # Itera através dos elementos da lista, começando do segundo elemento
  for i in range(1, len(arr)):
    # Elemento atual a ser inserido na posição correta
    key = arr[i]
    j = i - 1

    # Move os elementos maiores para a direita para abrir espaço para o elemento 'key'
    while j >= 0 and key < arr[j]:
      arr[j+1] = arr[j]
      j = j - 1

    # Insere 'key' na posição correta
    arr[j+1] = key


# Função de ordenação Merge Sort
def merge_sort(arr):
  # Verifica se a lista tem mais de um elemento (caso base da recursão)
  if len(arr) > 1:
    # Divide a lista ao meio
    mid = len(arr) // 2
    left = arr[:mid] # Sublista da esquerda
    right = arr[mid:] # Sublista da direita
    
    # Chama recursivamente o merge_sort para ambas as sublistas
    merge_sort(left)
    merge_sort(right)
    
    # Mescla (merge) as sublistas ordenadas de volta na lista original 'arr'
    helpers.merge(left, right, arr)


# Função de ordenação Heap Sort
def heap_sort(arr):
  length = len(arr)

  # Converte o array em uma Max-Heap
  for i in range(length // 2 - 1, -1, -1):
    helpers.heapify(arr, length, i)

  # Extrai elementos do heap um por um
  for i in range(length - 1, 0, -1):
    arr[i],arr[0] = arr[0],arr[i] # Troca o primeiro elemento com o último
    helpers.heapify(arr, i, 0) # Recria o heap máximo para o restante do array


# Função de ordenação Quick Sort
def quick_sort(arr):
  # Se a lista tiver 0 ou 1 elemento, ela já está ordenada
  if len(arr) <= 1:
    return arr
  
  # Divide a lista em três partes: elementos menores, iguais e maiores que o pivot
  pivot = arr[len(arr) // 2]
  left = [x for x in arr if x < pivot]
  middle = [x for x in arr if x == pivot]
  right = [x for x in arr if x > pivot]

  # Recursivamente ordena as partes esquerda e direita e combina com o elemento pivot
  return quick_sort(left) + middle + quick_sort(right)


# Função de ordenação Counting Sort
def counting_sort(arr):
  max_element = max(arr) # Encontra o maior elemento na lista
  count_arr = [0] * (max_element + 1)  # Cria uma lista de contagem com base no valor máximo encontrado

  # Conta a ocorrência de cada elemento no array
  for i in range(len(arr)):
    count_arr[arr[i]] += 1
  
  # Calcula as posições finais dos elementos ordenados
  for i in range(1, len(count_arr)):
    count_arr[i] += count_arr[i - 1]

  output = [0] * len(arr)
  
  # Constrói o array ordenado usando o count_arr
  for i in range(len(arr) - 1, -1, -1):
    output[count_arr[arr[i]] - 1] = arr[i]
    count_arr[arr[i]] -= 1
  
  # Atualiza o array original com o array ordenado
  for i in range(len(arr)):
    arr[i] = output[i]