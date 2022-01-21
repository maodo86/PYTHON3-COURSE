# Les classes (Part 2)
# Ajout des attributs aux classes


def jumpNextLine():
    print('\n')


class A:
    name = 'Ali'
    sex = 'Masculin'
    age = 28


class B(A):
    pass


if __name__ == '__main__':
    # Instancier la classe:
    var_a = A()

    print(var_a.name)
    print(var_a.sex)
    print(var_a.age)

    jumpNextLine()

    print(var_a.__getattribute__('name'))
    print(var_a.__getattribute__('sex'))
    print(var_a.__getattribute__('age'))
