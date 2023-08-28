from helpers import calculate_execution_time
import sorters


def print_and_save(message):
  print(message)

  with open("results.txt", "a") as f:
    f.write(message + "\n")
    f.close()


def output_time_metrics(initial_size, final_size, steps, repetitions, array_generator):
  
  for array_size in range(initial_size, final_size+1, steps):
    times_selection = []
    times_insertion = []
    times_merge = []
    times_heap = []
    times_quick = []
    times_counting = []
    
    for _ in range(repetitions):
      A = array_generator(array_size)
      print(A)
      times_selection.append(calculate_execution_time(A, sorters.selection_sort))
      times_insertion.append(calculate_execution_time(A, sorters.insertion_sort))
      times_merge.append(calculate_execution_time(A, sorters.merge_sort))
      times_heap.append(calculate_execution_time(A, sorters.heap_sort))
      times_quick.append(calculate_execution_time(A, sorters.quick_sort))
      times_counting.append(calculate_execution_time(A, sorters.counting_sort))

    result = f"{array_size} \t {sum(times_selection)/repetitions:f} \t {sum(times_insertion)/repetitions:f} \t {sum(times_merge)/repetitions:f} \t {sum(times_heap)/repetitions:f} \t {sum(times_quick)/repetitions:f} \t {sum(times_counting)/repetitions:f}"
    print_and_save(result)