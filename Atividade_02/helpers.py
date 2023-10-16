from random import randint

def generate_random_prices(length):
    array = []
    
    for _ in range(length):
        array.append(randint(1, 10))

    return array