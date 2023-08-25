from helpers import heapify


# Função de ordenação Selection Sort
def selection_sort(arr):
  
  for i in range(len(arr)):
    minIndex = i
  
    for j in range(i+1,len(arr)):
  
      if arr[j] < arr[minIndex]:
        minIndex = j
    arr[i],arr[minIndex] = arr[minIndex],arr[i] # Troca o elemento mínimo encontrado com o elemento na posição 'i'

# Função de ordenação Insertion Sort
def insertion_sort(arr):

  for i in range(1,len(arr)):
    key = arr[i]
    j = i-1

    while j >= 0 and key < arr[j]:
      arr[j+1] = arr[j]
      j-=1
    arr[j+1] = key

# Função de ordenação Merge Sort
def merge_sort(arr):

  if len(arr) > 1:
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    i = j = k = 0

    while i < len(left) and j < len(right):

      if left[i] < right[j]:
        arr[k] = left[i]
        i+=1

      else:
        arr[k] = right[j]
        j+=1
      k+=1

    while i < len(left):
      arr[k] = left[i]
      i+=1
      k+=1

    while j < len(right):
      arr[k] = right[j]
      j+=1
      k+=1

# Função de ordenação Heap Sort
def heap_sort(arr):
  n = len(arr)
  # Converte o array em um heap máximo
  for i in range(n//2-1,-1,-1):
    heapify(arr,n,i)
  # Extrai elementos do heap um por um
  for i in range(n-1,0,-1):
    arr[i],arr[0] = arr[0],arr[i] # Troca o primeiro elemento com o último
    heapify(arr,i,0) # Recria o heap máximo para o restante do array

# Função de ordenação Quick Sort
def quick_sort(arr):
    
    if len(arr) <= 1:
      return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    # Recursivamente ordena as partes esquerda e direita e combina com o elemento pivot
    return quick_sort(left) + middle + quick_sort(right)

# Função de ordenação Counting Sort
def counting_sort(arr):
  maxElement = max(arr)
  countArr = [0]*(maxElement+1)

  # Conta a ocorrência de cada elemento no array
  for i in range(len(arr)):
    countArr[arr[i]]+=1
  
  # Calcula as posições finais dos elementos ordenados
  for i in range(1,len(countArr)):
    countArr[i]+=countArr[i-1]
  output = [0]*len(arr)
  
  # Constrói o array ordenado usando o countArr
  for i in range(len(arr)-1,-1,-1):
    output[countArr[arr[i]]-1] = arr[i]
    countArr[arr[i]]-=1
  
  # Atualiza o array original com o array ordenado
  for i in range(len(arr)):
    arr[i] = output[i]