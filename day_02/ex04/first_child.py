import sys
from random import randint

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

    def file_reader(self, has_header=True):
        output = []
        with open(self.file_name) as fp_read:
            for i, line in enumerate(fp_read):
                if (has_header and i == 0):
                    continue
                first_num = int(line.split(',')[0])
                second_num = int(line.split(',')[1])
                output.append([first_num,second_num])
        return output


    class Calculations:
        def __init__(self, list_of_element):
            self.list_of_element = list_of_element

        def counts(self):
            count_heads = sum([x for x,y in [element for element in self.list_of_element]])
            count_tails = sum([y for x,y in [element for element in self.list_of_element]])
            return count_heads, count_tails
        def fractions(self, count_heads, count_tails):
            heads_percents = float(count_heads)/(count_heads + count_tails)
            tails_percents = float(count_tails)/(count_heads + count_tails)
            return heads_percents * 100, tails_percents * 100

    class Analytics(Calculations):
        def predict_random(self, count_predict):
            output = []
            for i in range(count_predict):
                heads = randint(0, 1)
                tails = 0 if (heads == 1) else 1
                output.append([heads, tails])
            return output

        def predict_last(self):
            return self.list_of_element[-1]




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
    calculation_class = class_object.Calculations(output)
    count_heads, count_tails = calculation_class.counts()
    heads_percents, tails_percents = calculation_class.fractions(count_heads, count_tails)
    list_predict_random = class_object.Analytics(output).predict_random(3)
    list_predict_last= class_object.Analytics(output).predict_last()
    print(output)
    print(count_heads, count_tails)
    print(heads_percents, tails_percents)
    print(list_predict_random)
    print(list_predict_last)

if __name__ == '__main__':
    research()