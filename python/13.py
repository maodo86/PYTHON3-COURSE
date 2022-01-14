# Structure conditionnelle if

var = 19


if __name__ == '__main__':
    # if is greater than var
    if var > 18:
        res = 1
    else:
        res = 0

    print(res)
    print('\n')

    res = 1 if var > 18 else 0
    print(res)
    print('\n')

    # if is equal than var
    if var == 18:
        res = 1
    elif var == 19:
        res = 1.5
    else:
        res = 0

    print(res)
    print('\n')
