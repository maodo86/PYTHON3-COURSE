# List comprehension (Part 2)
# Acces of list value

var = [x for x in range(4)]


if __name__ == '__main__':
    # display the value by index of list
    print(var[0], var[1], var[2], var[3])
    print('\n')

    # display the value by negative index of list
    print(var[-3], var[-2], var[-1], var[0])
    print('\n')
