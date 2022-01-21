# Les classes (Part 3)
# Heritage et vérification des attributs


def jumpNextLine():
    print('\n')


def dividerLine():
    print('---------------------------')


class A:
    name = 'Ali'
    sex = 'Masculin'
    age = 28


class B:
    color = 'Blue'
    tall = 1.78
    weight = 180


class C(A, B):
    pass


if __name__ == '__main__':
    # Instancier la classe:
    var_a = A()

    print(var_a.name)
    print(var_a.sex)
    print(var_a.age)

    jumpNextLine()

    dividerLine()
    print(hasattr(C, 'name'))
    dividerLine()
    print(hasattr(C, 'sex'))
    dividerLine()
    print(hasattr(C, 'age'))
    dividerLine()
    print(hasattr(C, 'color'))
    dividerLine()
    print(hasattr(C, 'tall'))
    dividerLine()
    print(hasattr(C, 'weight'))
    dividerLine()
