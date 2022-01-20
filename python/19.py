# functions (Part 1)

def jumpNextLine():
    print('\n')


def checkAge(age):
    if age > 18:
        print('Majeur')
    else:
        print('Mineur')


def checkAge2(age):
    if isinstance(age, int):
        if age > 18:
            print('Majeur')
        else:
            print('Mineur')
    else:
        print(f'{age} is not a integer')


def checkAge3(age: int):
    if age > 18:
        print('Majeur')
    else:
        print('Mineur')


if __name__ == '__main__':
    age = input('Enter your age: ')

    checkAge(age)
    # checkAge2(age)
    # checkAge3(age)

    # age = int(input('Enter your age: '))

    # checkAge(age)
    # checkAge2(age)
    # checkAge3(age)
