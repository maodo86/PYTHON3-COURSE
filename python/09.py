# Dict (Part 2)
# usual functions of dict

var = {}
var2 = [(1, 3), ('name', 'Ali')]


if __name__ == '__main__':
    # add value in dict
    var['name'] = 'Ismael'
    var['age'] = 28
    var['poids'] = 85.50
    var['country'] = 'AL'

    print(var)
    print('\n')

    print('All keys of dict:')
    print(var.keys())
    print(list(var.keys()))
    print('\n')

    print('All values of dict:')
    print(var.values())
    print(list(var.values()))
    print('\n')

    print('All items of dict:')
    print(var.items())
    print(list(var.items()))
    print('\n')

    print('New dict from list of tuple:')
    print(dict(var2))
    print('\n')
