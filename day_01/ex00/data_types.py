def data_types():
    print("[", end='')
    if (isinstance(1, int)):
        print("int,", end=' ')
    if (isinstance("", str)):
        print("str,", end=' ')
    if (isinstance(1.1, float)):
        print("float,", end=' ')
    if (isinstance(True, bool)):
        print("bool,", end=' ')
    if (isinstance([], list)):
        print("list,", end=' ')
    if (isinstance({}, dict)):
        print("dict,", end=' ')
    if (isinstance((), tuple)):
        print("tuple,", end=' ')
    if (isinstance(set(), set)):
        print("set", end='')
    print("]", end='')

if __name__ == '__main__':
    data_types()