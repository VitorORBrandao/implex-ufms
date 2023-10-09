# Alunos:
# Vítor Oliveira Resende Brandão
# Caue Maldonado Lima

import generators
import printers
import os


def create_empty_file(file_name):
    # Verificar se o arquivo existe
    if os.path.exists(file_name):
        # Se o arquivo existe, deleta ele
        os.remove(file_name)
    
    # Cria um novo arquivo vazio
    with open(file_name, 'w'):
        pass


def main():
  file_name = "results.txt"
  create_empty_file(file_name)
  
  # inc = int(input("Initial size: "))
  # fim = int(input("Final size: "))
  # stp = int(input("Step: "))
  # rpt = int(input("Repeat: "))

  # Define os valores iniciais para as variáveis
  inc, fim, stp, rpt = 2000, 20000, 2000, 5

  # Imprime e escreve os resultados para diferentes tipos de arrays
  printers.print_and_save("[[RANDOM]]") 
  # Lista com valores aleatórios
  printers.output_time_metrics(inc, fim, stp, rpt, generators.generate_random_array)
  
  printers.print_and_save("\n[[REVERSE]]") 
  # Lista com valores ordenados inversamente
  printers.output_time_metrics(inc, fim, stp, 1, generators.generete_reverse_array)
  
  printers.print_and_save("\n[[SORTED]]")
  # Lista com valores ordenados
  printers.output_time_metrics(inc, fim, stp, 1, generators.generate_sorted_array)
  
  printers.print_and_save("\n[[NEARLY SORTED]]")
  # Lista com valores quase ordenados
  printers.output_time_metrics(inc, fim, stp, 1, generators.generate_nearly_sorted_array)


if __name__ == '__main__':
  main()