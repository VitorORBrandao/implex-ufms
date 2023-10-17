# Alunos:
# Vítor Oliveira Resende Brandão
# Caue Maldonado Lima


from printers import output_metrics
from helpers import create_empty_file


def main():
  # Cria um novo arquivo para o armazenamento dos resultados
  file_name = "results.txt"
  create_empty_file(file_name)

  # Permite que o usuário defina os valores iniciais para as variáveis
  # inc = int(input("Initial size: "))
  # fim = int(input("Final size: "))
  # stp = int(input("Step: "))

  # Define os valores iniciais para as variáveis
  inc, fim, stp = 100, 2000, 100

  # Imprime e escreve os resultados para diferentes tipos de preços
  output_metrics(inc, fim, stp)


if __name__ == '__main__':
  main()