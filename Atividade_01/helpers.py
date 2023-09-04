from time import time


def merge(left, right, arr):
    i = j = k = 0

    # Enquanto houver elementos nas duas listas 'left' e 'right'
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Adiciona quaisquer elementos restantes da lista 'left', se houver
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # Adiciona quaisquer elementos restantes da lista 'right', se houver
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def heapify(arr, n, i):
    largest = i # Inicializa o maior como a raiz
    left = 2 * i + 1 # Índice do filho esquerdo
    right = 2 * i + 2 # Índice do filho direito
    
    # Compara o valor da raiz com o valor do filho esquerdo
    if left < n and arr[largest] < arr[left]:
        largest = left
    
    # Compara o valor da raiz com o valor do filho direito
    if right < n and arr[largest] < arr[right]:
        largest = right
    
    # Se o maior valor não for a raiz, troca-os
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Chama heapify recursivamente na subárvore afetada
        heapify(arr, n, largest)


def calculate_execution_time(list, function_sorter):
  # Cria uma cópia da lista para não modificar a lista original
  new_list = list.copy()
  
  initial_time = time() # Registra o tempo inicial
  function_sorter(new_list) # Chama a função de ordenação para ordenar a cópia da lista
  end_time = time()  # Registra o tempo final
  
  # Calcula e retorna o tempo de execução em segundos
  return end_time - initial_time