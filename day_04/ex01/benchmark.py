#! /usr/bin/python3
import timeit

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



if __name__ == '__main__':
    time_1 = first_time()
    time_2 = second_time()
    time_3 = third_time()
    sort_list = [time_1, time_2, time_3]
    sort_list.sort()
    if (time_2 == sort_list[0]):
        print('it is better to use a list comprehension')
    elif (time_3 == sort_list[0]):
        print('it is better to use a map')
    else:
        print('it is better to use a loop')
    print(sort_list[0], 'vs', sort_list[1], 'vs', sort_list[2])