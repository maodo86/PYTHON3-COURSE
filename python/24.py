# Les classes (Part 1)
# Creation de classe


def jumpNextLine():
    print('\n')


class A:
    pass


class B(A):
    pass


class C(B):
    pass


if __name__ == '__main__':
    # Instancier la classe:
    var_a = A()
    var_b = B()
    var_c = C()

    print(var_a)
    jumpNextLine()
    print(var_b)
    jumpNextLine()
    print(var_c)
