import sys

def extractor():
    if (len(sys.argv) > 2):
        raise Exception('Argument error')
    fp_write = open('employees.tsv', 'w')
    for i, param in enumerate(sys.argv):
        if (i != 0):
            fp_write.write("Name\tSurname\tE-mail\n")
            with open(param) as fp_read:
                for line in fp_read:
                    name_surname = line.split('@')
                    name = name_surname[0].split('.')[0]
                    surname = name_surname[0].split('.')[1]
                    fp_write.write('%s\t%s\t%s' % (name.capitalize(), surname.capitalize(), line))

if __name__ == '__main__':
    extractor()