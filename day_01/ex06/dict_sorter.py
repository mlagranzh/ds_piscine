def dict_sorter():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    dict1 = dict((x, y) for x, y in list_of_tuples)
    sorted_tuples = sorted(dict1.items(), key=lambda item: item[0])
    sorted_dict = {k: v for k, v in sorted_tuples}

    sorted_tuples = sorted(dict1.items(), key=lambda item: -int(item[1]))
    sorted_dict = {k: v for k, v in sorted_tuples}

    for i in sorted_dict :
        print('%s' % i)
    
if __name__ == '__main__':
    dict_sorter()