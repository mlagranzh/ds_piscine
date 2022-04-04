import sys

class Research:

    def __init__(self, file_name):
        self.file_name = file_name

    def parsing(self):
        with open(self.file_name) as fp_read:
            for i, line in enumerate(fp_read):
                if (len(line.split(',')) != 2):
                    raise Exception
                if (i != 0 and (line.split(',')[0] not in ('0', '1') or line.split(',')[1].strip() not in ('0', '1'))):
                    raise Exception

    def file_reader(self):
        output = ''
        with open(self.file_name) as fp_read:
            for line in fp_read:
                output += line
        return output

def research():
    if (len(sys.argv) != 2):
        exit(1)
    try:
        file = open(sys.argv[1])
    except BaseException:
        print("File not found")
        exit(1)
    class_object = Research(sys.argv[1])
    try:
        class_object.parsing()
    except Exception:
        print("Parsing Error")
        exit(1)
    output = class_object.file_reader()
    print(output)

if __name__ == '__main__':
    research()