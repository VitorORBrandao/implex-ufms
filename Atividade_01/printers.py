from helpers import calculate_execution_time
import sorters


# Esta função imprime uma mensagem no console e ao arquivo
def print_and_save(message):
  # Imprime a mesnagem no console
  print(message)

  with open("results.txt", "a") as f:
    # Escreve a mensagem no arquivo
    f.write(message + "\n")


def output_time_metrics(initial_size, final_size, steps, repetitions, array_generator):
  # Cabeçalho para a saída de dados
  header = "N   \t Selection   \t Insertion   \t Merge   \t Heap   \t Quick   \t Counting"
  print_and_save(header)

  # Loop através de diferentes tamanhos de array
  for array_size in range(initial_size, final_size+1, steps):
    # Listas para armazenar os tempos de execução dos algoritmos
    times_selection = []
    times_insertion = []
    times_merge = []
    times_heap = []
    times_quick = []
    times_counting = []
    
    # Executa os algoritmos repetidas vezes e mede o tempo de execução
    for _ in range(repetitions):
      A = array_generator(array_size)
      times_selection.append(calculate_execution_time(A, sorters.selection_sort))
      times_insertion.append(calculate_execution_time(A, sorters.insertion_sort))
      times_merge.append(calculate_execution_time(A, sorters.merge_sort))
      times_heap.append(calculate_execution_time(A, sorters.heap_sort))
      times_quick.append(calculate_execution_time(A, sorters.quick_sort))
      times_counting.append(calculate_execution_time(A, sorters.counting_sort))

    # Calcula as médias dos tempos de execução e formata os resultados
    result = f"{array_size} \t {sum(times_selection)/repetitions:f} \t {sum(times_insertion)/repetitions:f} \t {sum(times_merge)/repetitions:f} \t {sum(times_heap)/repetitions:f} \t {sum(times_quick)/repetitions:f} \t {sum(times_counting)/repetitions:f}"
    # Imprime e salva os resultados
    print_and_save(result)