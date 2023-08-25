from random import randint


def generate_random_array(length):
  array = []
  
  for _ in range(length):
    array.append(randint(0, 20000))
  
  return array


def generate_sorted_array(length):
  array = generate_random_array(length)
  array.sort()
  
  return array


def generete_reverse_array(length):
  array = generate_sorted_array(length)
  array.reverse()
  
  return array


def generate_nearly_sorted_array(length):
  array = generate_sorted_array(length)

  for _ in range(int(length * 0.1)):
    i = randint(0, length-1)
    j = randint(0, length-1)
    array[i], array[j] = array[j], array[i]
  
  return array