#! /usr/bin/python3
import timeit
import sys

def with_a_filter():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com', 'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com', 'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com', 'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com', 'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    new_emails = list(filter(lambda x: x.split('@')[-1] == 'gmail.com', emails))

def fourth_time():
    SETUP_CODE = 'from benchmark import with_a_filter'
 
    TEST_CODE = 'with_a_filter()'
     
    times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          number = 10**6)
 
    return sum(times)     


def third_time():
    SETUP_CODE = 'from benchmark import with_a_map'
 
    TEST_CODE = 'with_a_map()'
     
    times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          number = 10**6)
 
    return sum(times)     

def with_a_map():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com', 'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com', 'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com', 'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com', 'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    new_emails = map(lambda x: x if (x.split('@')[-1] == 'gmail.com') else None , emails)

def with_a_loop_and_an_append():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com', 'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com', 'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com', 'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com', 'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    new_emails = []
    for element in emails:
        if (element.split('@')[-1] == 'gmail.com'):
            new_emails.append(element)


def list_comprehension_instead():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com', 'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com', 'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com','john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com' ,'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com' ]
    new_emails = [element for element in emails if element.split('@')[-1] == 'gmail.com']


def first_time():
    SETUP_CODE = 'from benchmark import with_a_loop_and_an_append'
 
    TEST_CODE = 'with_a_loop_and_an_append()'
     
    times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          number = 10**6)
 
    return sum(times)     

def second_time():
    SETUP_CODE = 'from benchmark import with_a_loop_and_an_append'
 
    TEST_CODE = 'with_a_loop_and_an_append()'
     
    times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          number = 10**6)
 
    return sum(times)     


def main(argv=sys.argv):
    if (argv[1] == 'loop'):
        time = first_time(argv[2])
    if (argv[1] == 'list comprehension'):
        time = second_time()
    if (argv[1] == 'map'):
        time = third_time()
    if (argv[1] == 'filter'):
        time = fourth_time()
    print(time)

if __name__ == '__main__':
    main()