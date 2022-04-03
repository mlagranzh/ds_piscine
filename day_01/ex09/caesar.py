import sys

def caesar():
    if (len(sys.argv) != 4):
        raise Exception('Argument error')
    kirill_small = ('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    kirill_big = ('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    find_kirill_small = [x for x in kirill_small if x in sys.argv[2].lower()]
    find_kirill_big = [x for x in kirill_big if x in sys.argv[2].lower()]
    if ((len(find_kirill_small) + len(find_kirill_big)) != 0):
        raise Exception('Language error')
    
    res = ''
    type = sys.argv[1]
    words = sys.argv[2]
    number = sys.argv[3]
    alpha_small = 'abcdefghijklmnopqrstuvwxyz'
    alpha_big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if (type == 'encode'):
        res = ''
        for c in words:
            if (c in alpha_small):
                res += alpha_small[(alpha_small.index(c) + int(number)) % len(alpha_small)]
            elif (c in alpha_big):
                res += alpha_big[(alpha_big.index(c) + int(number)) % len(alpha_big)]
            else:
                res += c
    if (type == 'decode'):
        res = ''
        for c in words:
            if (c in alpha_small):
                res += alpha_small[(alpha_small.index(c) - int(number)) % len(alpha_small)]
            elif (c in alpha_big):
                res += alpha_big[(alpha_big.index(c) - int(number)) % len(alpha_big)]
            else:
                res += c
    print(res)

if __name__ == '__main__':
    caesar()