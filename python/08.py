# Dict (Part 1)

var = {}
var2 = {}

var3, var4 = {}, {}

if __name__ == '__main__':
    # add value in dict
    var['name'] = 'Ali'
    var['age'] = 18
    var['poids'] = 75.50
    var['country'] = 'SN'

    # display the value of dict
    print(var)

    print('\n')
    print(var['name'])
    print(var['age'])
    print(var['poids'])
    print(var['country'])
    print('\n')

    print(var.get('name'))
    print(var.get('age'))
    print(var.get('poids'))
    print(var.get('country'))
    print('\n')

    # update dict (add new value)
    var.update({'language': 'Wolof',
                'classe': 'DAR-3',
                'tall': 1.78, })

    print(var)
    print('\n')

    # update dict (add new value)
    var2 = {'language': 'Wolof',
            'classe': 'DAR-3',
            'tall': 1.78, }

    var3['date'] = '2012-08-12'
    var3['time'] = '18:01:32'

    var = var2 | var3
    print(var)
    print('\n')

    # update dict (add new value)
    var4['language'] = 'English'
    var4['classe'] = 'LIPMEN-3'

    var = var2 | var4
    print(var)
    print('\n')

