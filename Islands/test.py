from number_of_islands import count_islands,count_islands_without
from random import randint,choice
def generate_random_matrix():
    rows = randint(0, 15)
    cols = randint(0, 15)
    # matrix = [[str(choice([0, 1])) for _ in range(cols)] for _ in range(rows)]
    matrix = [[str(choice([0, 1])) for _ in range(cols)] for _ in range(rows)]
    
    return matrix

def print_matrix(matrix):
    print("[")
    for row in matrix:
        print(f"   {row},")
    print("]")

random_matrix = generate_random_matrix()
print_matrix(random_matrix)
print(f"number of islands: {count_islands(random_matrix)}")
print(f"count_islands_without: {count_islands_without(random_matrix)}")
