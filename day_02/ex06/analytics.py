import sys
from random import randint
import logging

class Research:
    
    def __init__(self, file_name):
        self.file_name = file_name

    def parsing(self):
        logging.info("Research.parsing()")
        with open(self.file_name) as fp_read:
            for i, line in enumerate(fp_read):
                if (len(line.split(',')) != 2):
                    raise Exception
                if (i != 0 and (line.split(',')[0] not in ('0', '1') or line.split(',')[1].strip() not in ('0', '1'))):
                    raise Exception

    def file_reader(self, has_header=True):
        logging.info("Research.file_reader()")
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
            logging.info("Calculating.counts()")
            count_heads = sum([x for x,y in [element for element in self.list_of_element]])
            count_tails = sum([y for x,y in [element for element in self.list_of_element]])
            return count_heads, count_tails
        def fractions(self, count_heads, count_tails):
            logging.info("Calculating.fractions()")
            heads_percents = float(count_heads)/(count_heads + count_tails)
            tails_percents = float(count_tails)/(count_heads + count_tails)
            return heads_percents, tails_percents

    class Analytics(Calculations):
        def predict_random(self, count_predict):
            logging.info("Analytics.predict_random()")
            output = []
            for i in range(count_predict):
                heads = randint(0, 1)
                tails = 0 if (heads == 1) else 1
                output.append([heads, tails])
            return output

        def predict_last(self):
            return self.list_of_element[-1]
        #where self????
        def save_file(data, name_of_file, type_of_file):
            logging.info("Analytics.save_file()")
            file_write = open(name_of_file + '.' + type_of_file, 'w')
            file_write.write(data)
            
