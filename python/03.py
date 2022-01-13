# List, tuple, dict

var1 = []   # list()
var2 = ()   # tuple()
var3 = {}   # dict()

var4 = [(), (), [], {}]
var5 = ([], [], {}, ())

if __name__ == '__main__':
    print(type(var1))
    print(type(var2))
    print(type(var3))

    print('\n')
    print(type(var4))
    print(type(var5))

    print('\n')
    print('The types of var4 elements:')
    print('-----------------------------------------')
    print(type(var4[0]), type(var4[2]), type(var4[3]))
    print('-----------------------------------------')

    print('\n')
    print('The types of var4 elements:')
    print('-----------------------------------------')
    print(type(var5[0]), type(var5[2]), type(var5[3]))
    print('-----------------------------------------')
