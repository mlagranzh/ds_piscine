import sys

def letter_starter():
    if (len(sys.argv) > 2):
        raise Exception('Argument error')
    name = ''
    for i, param in enumerate(sys.argv):
        if (i != 0):
            with open("employees.tsv") as fp_read:
                for line in fp_read:
                    if (param == line.split('\t')[-1].strip()):
                        name = line.split('\t')[0]
            if (name != ''):
                print(f"Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with you. That's a precondition for the professionals that our company hires.")
            else:
                print("e-mail not found")


if __name__ == '__main__':
    letter_starter()