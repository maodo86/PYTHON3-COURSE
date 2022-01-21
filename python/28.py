# Les classes (Part 5)
# Surchage d'attributs dans une classe


def jumpNextLine():
    print('\n')


def dividerLine():
    print('---------------------------')


class A:
    name = 'Ali'
    sex = 'Masculin'
    age = 28


class B(A):
    name = 'Julie'
    sex = 'Feminin'
    age = 22

class C(A):
    pass


if __name__ == '__main__':
    # Instancier la classe:
    var_a = A()
    var_b = B()

    print(var_a.name)
    print(var_a.sex)
    print(var_a.age)

    jumpNextLine()
    dividerLine()

    print(var_b.name)
    print(var_b.sex)
    print(var_b.age)

    jumpNextLine()
    dividerLine()

    print(C.name)
    print(C.sex)
    print(C.age)


