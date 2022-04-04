class Must_read:
    with open("data.csv") as fp_read:
        for line in fp_read:
            print(line, end='')



def must_read():
    Must_read()

if __name__ == '__main__':
    must_read()