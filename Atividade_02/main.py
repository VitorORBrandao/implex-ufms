# Alunos:
# Vítor Oliveira Resende Brandão
# Caue Maldonado Lima

import cutting_functions


def main():
  # inc = int(input("Initial size: "))
  # fim = int(input("Final size: "))
  # stp = int(input("Step: "))

  # Define os valores iniciais para as variáveis
  inc, fim, stp = 100, 2000, 100

  prices_by_length = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

  n = 10
  result = cutting_functions.bottom_up_cut_rod(prices_by_length, n)
  print(f"O valor máximo obtido para uma haste de comprimento {n} é {result}.")


if __name__ == '__main__':
  main()