
#parrot
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


# 1 positional argument
parrot(1000)

# 1 keyword argument
parrot(voltage=1000)

# 2 keyword arguments
parrot(voltage=1000000, action='VOOOOOM')

# 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)

# 3 positional arguments
parrot('a million', 'bereft of life', 'jump')

# 1 positional, 1 keyword
parrot('a thousand', state='pushing up the daisies')

# ask_yn 
def ask_yn(prompt, retries=4, complaint='Enter Y/N!'):
    for i in range(retries):
        ok = input(prompt).strip()
        if ok in ('Y', 'y'):
            return True
        if ok in ('N', 'n'):
            return False
        print(complaint)
    return False
# Call with only the mandatory argument
ask_yn('Really quit?')

# Call with one keyword argument
ask_yn('OK to overwrite the file?', retries=2)

# Call with one keyword argument - in any order!
ask_yn('Update status?', complaint='Just Y/N')

# Call with all of the keyword arguments
ask_yn('Send text?', retries=2, complaint='Y/N please!')

# These can provide variants of a simple idea.
ask_yn("Do you like raindrops on roses?")
ask_yn("How about whiskers on kittens?", retries=10)
ask_yn("Any love for bright copper kettles?", complaint="Yes or no :)")
ask_yn("Would you like warm woolen mittens?", retries=10, complaint="A yes or no shall suffice.")

#print_my_arguments

def print_my_arguments(a, *b, c=1):
    print(f"a={a}, b={b}, c={c}")

print_my_arguments(2)                   # a=2, b=(), c=1
print_my_arguments(2, 7)                # a=2, b=(7,), c=1
print_my_arguments(2, 7, 1)             # a=2, b=(7, 1), c=1
print_my_arguments(2, 7, 1, 8)          # a=2, b=(7, 1, 8), c=1
print_my_arguments(2, 7, 1, 8, 2)       # a=2, b=(7, 1, 8, 2), c=1
print_my_arguments(2, 7, 1, 8, 2, c=8)  # a=2, b=(7, 1, 8, 2), c=8
def test(*args):
    print(args)
test(5, 6, 7, 8)
#output (5, 6, 7, 8) tuple

# product

def product(*nums, start=1):
    running_product = start
    for number in nums:
        running_product *= number
    return running_product
product(3, 5)  # => 15
product(3, 4, 2)  # => 24
product(3, 4, 2, 5)  # => 120
product()  # => 1
product(7, start=15)  # => 105
product(5, 6, start=10)  # => 300

primes = (2, 3, 5, 7, 11)
product(*primes)

authorize(
    "If music be the food of love, play on.",
    playwright="Shakespeare",
    act=1,
    scene=1,
    speaker="Duke Orsino"
)
# > If music be the food of love, play on.
# ----------------------------------------
# playwright: Shakespeare
# act: 1
# scene: 1
def authorize(quote, **speaker_info):
    print(">", quote)
    print("-" * (len(quote) + 2))
    for key, value in speaker_info.items():
        print(key, value, sep=': ')
info = {
    'sonnet': 18,
    'line': 1,
    'author': "Shakespeare"
}
authorize("Shall I compare thee to a summer's day", **info)  # Does the same thing as authorize("Shall I compare thee to a summer's day", sonnet=18, line=1, author='Shakespeare')
# > Shall I compare thee to a summer's day
# ----------------------------------------
# sonnet: 18
# line: 1
# author: Shakespeare
