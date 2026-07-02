import helper

def generate_cases():
    size = 0
    while True:
        yield helper.random_list(size)
        size += 1

def generate_cases_another_alternative():
    return map(helper.random_list, itertools.count())
if __name__ == '__main__':
    for case in generate_cases():
        if len(case) > 10:
            break
        print(case)