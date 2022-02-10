
def get_next_collatz(n):
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    return n


def print_collatz(n):
    while n > 1:
        print(n)
        n = get_next_collatz(n)
    print(1)
    
#print_collatz(15)


def count_collatz(n):
    counter = 0
    while n > 1:
        counter += 1
        n = get_next_collatz(n)
    return counter
"""
c = count_collatz(15)
print("chain length", c)
"""
def colatz_count_under(limit):
    n = 1
    while n <= limit:
        c = count_collatz(n)
        print(n, "->", c)
        n += 1

colatz_count_under(100)
