# List comprehension (Part 3)
# Add, remove, pop, extend, insert, remove value

var = []


if __name__ == '__main__':
    # add new value
    var.append(1)
    var.append(2)
    var.append(28.88)
    var.append('Ali')
    var.append('Sarr')
    var.append(['Ali', 18, [-155.88, 68.78]])
    print(var)
    print('\n')

    # remove value out list
    del var[0]
    del var[1]
    print(var)
    print('\n')

    # pop element out list
    var.pop()
    var.pop(1)
    print(var)
    print('\n')

    # extend element for list
    var.extend([201, 202, 203])
    var.extend([301, 302, 303])
    print(var)
    print('\n')

    # insert element in list
    var.insert(-1, 555)
    var.insert(-1, 665)
    var.insert(3, 888)
    print(var)
    print('\n')

    # remove element out of list
    var.remove('Sarr')
    var.remove(665)
    print(var)
    print('\n')
