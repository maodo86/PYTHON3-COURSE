# functions and class (Part 1)

def firstFunc():
    print(f'I am a function')
    pass

def jumpNextLine():
    print('\n')

def upperName():
    name = input('Enter your Name: ')
    print(name.upper())

def simpleUpperName():
    print(str(input('Enter your Name: ')).upper())


if __name__ == '__main__':
    print(f'Begin first function test')
    print(f'-------------------------')
    firstFunc()
    jumpNextLine()
    print(f'Begin second function test')
    print(f'------------------------- ')
    upperName()
    jumpNextLine()
    print(f'Begin third function test')
    print(f'-------------------------')
    simpleUpperName()
