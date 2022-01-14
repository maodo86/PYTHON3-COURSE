# Strings manipulations

if __name__ == '__main__':
    name1 = input('Enter your first_name: ')
    name2 = input('Enter your last_name: ')
    country = input('Enter your country: ')

    # name1 = str(input('Enter your first_name: '))
    # name2 = str(input('Enter your last_name: '))
    # country = str(input('Enter your country: '))

    print('\n')
    print('Your First Name is: ', name1)
    print('Your Last Name is: ', name2)
    print('Your country is: ', country)

    print('\n')
    print(f'Your First Name is: {name1}')
    print(f'Your Last Name is: {name2}')
    print(f'Your country is: {country}')

    print('\n')
    print('Your First Name is: '.format(name1))
    print('Your Last Name is: '.format(name2))
    print('Your country is: '.format(country))

    print('\n')
    print('Your First Name is: %s' % name1)
    print('Your Last Name is: %s' % name2)
    print('Your country is: %s' % country)
