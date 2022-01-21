# Les classes (Part 4)
# Ajout des attributs à une instance


def jumpNextLine():
    print('\n')


def dividerLine():
    print('---------------------------')


class A:
    name = 'Ali'
    sex = 'Masculin'
    age = 28


class B(A):
    pass


if __name__ == '__main__':
    # Instancier la classe:
    var_a = A()
    var_a.color = 'Blue'
    var_a.tall = 1.89
    var_a.weight = 188

    print(var_a.name)
    print(var_a.sex)
    print(var_a.age)
    print(var_a.color)
    print(var_a.tall)
    print(var_a.weight)

    jumpNextLine()
    dividerLine()
    print(hasattr(var_a, 'color'))
    print(hasattr(var_a, 'tall'))
    print(hasattr(var_a, 'weight'))
    dividerLine()

    dividerLine()
    print(hasattr(A, 'color'))
    print(hasattr(A, 'tall'))
    print(hasattr(A, 'weight'))
    dividerLine()

    dividerLine()
    print(hasattr(B, 'color'))
    print(hasattr(B, 'tall'))
    print(hasattr(B, 'weight'))
    dividerLine()

    # print(vars(A))
