class Research:
    def file_reader(self, file_name):
        output = ''
        with open(file_name) as fp_read:
            for line in fp_read:
                output += line
        return output

def research():
    class_object = Research()
    output = class_object.file_reader("data.csv")
    print(output)

if __name__ == '__main__':
    research()