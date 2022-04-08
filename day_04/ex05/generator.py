#! /usr/bin/python3

# os.system('curl -o myfile.zip http://files.grouplens.org/datasets/movielens/ml-25m.zip')
# os.system('unzip myfile.zip -d dir && rm -f myfile.zip')
import sys
import psutil

def generator():
    file = sys.argv[1]
    with open(file) as f:
        for line in f:
            yield line


def main():
    for el in generator():
        pass
    mem = psutil.Process().memory_info().vms/(10**9)
    cpu = psutil.Process().cpu_times()
    print(f'Peak Memory Usage = {mem} Gb')
    print(f'User Time + System Time = {cpu.user + cpu.system}s')

if __name__ == '__main__':
    try:
        main()
    except BaseException:
        print("ERROR")