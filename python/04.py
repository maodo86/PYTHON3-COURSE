# List comprehension (Part 1)

var1 = []   # list()
var2 = [1, 2, 3, 4, 5]
var3 = [x for x in var2]
var4 = [x for x in var2]
var5 = [x for x in range(6)]
var6 = [x for x in range(10)]

# zip function take 2 list and add them
var7 = list(zip(var3, var4))
var8 = [(x, y) for x, y in zip(var3, var4)]
var9 = [[x, y] for x, y in zip(var3, var4)]


if __name__ == '__main__':
    print(var1)
    print('\n')
    print(var2)
    print('\n')
    print(var3)
    print('\n')
    print(var4)
    print('\n')
    print(var5)
    print('\n')
    print(var6)
    print('\n')
    print(var7)
    print('\n')
    print(var8)
    print('\n')
    print(var9)
