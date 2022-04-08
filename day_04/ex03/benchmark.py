#! /usr/bin/python3
import timeit
import sys
from functools import reduce

def loop_iterable(num):
    sum_square = 0
    for i in range(num+1):
        sum_square += i*i

def use_reduce(num):
    sum_square = reduce(lambda y, x: y + x**2, range(num+1))


def first_time(time, num):
    SETUP_CODE = 'from benchmark import use_reduce'
 
    TEST_CODE = 'use_reduce({})'.format(num)
     
    times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          number = time)
 
    return sum(times)     

def second_time(time, num):
    SETUP_CODE = 'from benchmark import loop_iterable'
 
    TEST_CODE = 'loop_iterable({})'.format(num)
     
    times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          number = time)
 
    return sum(times)     


def main(argv=sys.argv):
    time_exec = 0
    if (argv[1] == 'reduce'):
        time_exec = first_time(int(argv[2]), int(argv[3]))
    elif (argv[1] == 'loop'):
        time_exec = second_time(int(argv[2]), int(argv[3]))
    use_reduce(5)
    loop_iterable(5)
    print(time_exec)

if __name__ == '__main__':
    try:
        main()
    except BaseException:
        print("ERROR")