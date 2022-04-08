from collections import Counter
from email.policy import default
import timeit, random

def my_top(list):
    top_10 = {}
    dictionary = {}
    for element in list:
        if element not in dictionary:
            dictionary[element] = 1
        else:
            dictionary[element] += 1
    
    top_10 = dict(x for i, x in enumerate(sorted(dictionary.items(), key=lambda item: -item[1])) if i < 10)
    return top_10

def top_10_most(list):
    cnt = Counter(list)
    return cnt.most_common(10)

def create_dict(list):
    cnt = Counter(list)
    dictionary = dict(cnt)
    return dictionary

def my_function(list):
    dictionary = {}
    for element in list:
        if element not in dictionary:
            dictionary[element] = 1
        else:
            dictionary[element] += 1
    return dictionary

def main():
    my_list = [random.randint(0, 100) for i in range(1000000)]
    print('my function:', timeit.timeit(f'my_function({my_list})',
                        number=1,
                        setup='from __main__ import my_function'))

    print('Counter:', timeit.timeit(f'create_dict({my_list})',
                        number=1,
                        setup='from __main__ import create_dict'))

    print('my top:', timeit.timeit(f'my_top({my_list})',
                        number=1,
                        setup='from __main__ import my_top'))

    print("Counter's top:", timeit.timeit(f'top_10_most({my_list})',
                        number=1,
                        setup='from __main__ import top_10_most'))

if __name__ == '__main__':
    try:
        main()
    except BaseException:
        print("ERROR")