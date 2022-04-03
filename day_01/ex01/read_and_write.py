def read_and_write():
    fp_write = open('ds.tsv', 'w')
    with open('ds.csv') as fp_read:
        for line in fp_read:
            chunks = line.split(',')

#           preprocessing 
            if (len(chunks) > 6):
                for i in range(len(chunks)):
                    if (i > 1 and i < len(chunks) - 4):
                        chunks[2] += (',' + chunks[i+1])
            del chunks[3:len(chunks) - 3]
            for i, chunk in enumerate(chunks):
                fp_write.write(chunk)
                if (i != len(chunks) - 1):
                    fp_write.write("\t")

if __name__ == '__main__':
    read_and_write()