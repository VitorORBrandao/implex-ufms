import generators
import printers


def main():
  # inc = int(input("Initial size: "))
  # fim = int(input("Final size: "))
  # stp = int(input("Step: "))
  # rpt = int(input("Repeat: "))
  
  # Define os valores iniciais para as variáveis
  inc, fim, stp, rpt = 10, 20, 5, 3

  # Imprime e escreve os resultados para diferentes tipos de arrays
  printers.print_and_save("[[RANDOM]]")
  printers.output_time_metrics(inc, fim, stp, rpt, generators.generate_random_array)
  
  printers.print_and_save("\n[[REVERSE]]")
  printers.output_time_metrics(inc, fim, stp, rpt, generators.generete_reverse_array)
  
  printers.print_and_save("\n[[SORTED]]")
  printers.output_time_metrics(inc, fim, stp, rpt, generators.generate_sorted_array)
  
  printers.print_and_save("\n[[NEARLY SORTED]]")
  printers.output_time_metrics(inc, fim, stp, rpt, generators.generate_nearly_sorted_array)


if __name__ == '__main__':
  main()