# Strings manipulations

var = 'ecole multinationale des télécomunications'
var2 = 'ecole multinationale, des télécomunications'


if __name__ == '__main__':
    upper = var.upper()
    lower = var.lower()
    capitalize = var.capitalize()
    split = var.split(' ')
    split2 = var2.split(',')
    count = len(split)
    count2 = len(split2)

    print(f'Var Upper is:')
    print(f'{upper}')
    print('\n')

    print(f'Var Lower is:')
    print(f'{lower}')
    print('\n')

    print(f'Var Capitalize is:')
    print(f'{capitalize}')
    print('\n')

    print(f'Var split is:')
    print(type(split))
    print(split)
    print('\n')

    print(f'Var2 split is:')
    print(type(split))
    print(split)
    print('\n')

    print(f'Var split count is:')
    print(count)
    print('\n')

    print(f'Var2 split count is:')
    print(count2)
    print('\n')

    print(f'Var and Var2 split count with __len__:')
    print(split.__len__())
    print(split2.__len__())

    print('\n')
    print(f'Assertions')
    assert split.__len__() == count
    print(f'OK.....................')
    assert split2.__len__() == count2
    print(f'OK.....................')
