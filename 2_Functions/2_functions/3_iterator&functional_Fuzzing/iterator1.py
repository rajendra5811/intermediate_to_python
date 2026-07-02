
    # Yield an infinite stream of Tribonacci numbers! The next value of the sequence will be c + b + a.
    #The first three Tribonacci numbers are 0, 0, 1. The next Tribonacci numbers in the sequence are 1, 2, 4, 7, 13, 24, 44, 81, ..
    
def generate_tribonacci_numbers():
    a, b, c = 0, 0, 1
    while True:
        yield a
        a, b, c = b, c, a + b + c

def is_tribonacci(num):
    """Return whether `num` is a Tribonacci number."""
    # Be careful to not loop infinitely!
    for n in generate_tribonacci_numbers():
        if n < num:
            continue
        return n == num
    return False

print(is_tribonacci(7))