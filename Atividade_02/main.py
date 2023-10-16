# Alunos:
# Vítor Oliveira Resende Brandão
# Caue Maldonado Lima


from printers import output_metrics
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