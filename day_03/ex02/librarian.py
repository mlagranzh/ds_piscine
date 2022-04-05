#! /usr/bin/python3
import os

def main():
    if (os.environ['VIRTUAL_ENV'].split('/')[-1] != 'celys'):
        raise Exception
    os.system('pip3 install -r requirements.txt')
    os.system("pip3 freeze > requirements.txt")
    os.system("cat requirements.txt")
if __name__ == '__main__':
    try:
        main()
    except Exception:
        print("env wrong")

#virtualenv celys
#deactivate
#source env/celys/bin/activate