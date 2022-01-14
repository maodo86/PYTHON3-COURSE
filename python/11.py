# Tuple (Part 2)
# Acces of list value

var = (x for x in range(4))
var2 = (1, 2, 3, (4,5))


if __name__ == '__main__':
    # display the value by index of tuple
    print(var[0], var[1], var[2], var[3])
    print('\n')

    # display the value by negative index of tuple
    print(var[-3], var[-2], var[-1], var[0])
    print('\n')

    # display the value by index of tuple
    print(var2[0], var2[1], var2[2], var2[3])
    print('\n')

    # display the value by negative index of tuple
    print(var2[-3], var2[-2], var2[-1], var2[0])
    print('\n')
