# Les exceptions

def jumpNextLine():
    print('\n')


# (EXO): Réecrire cette fonction de manière plus ergonomique
#
# def div2Number(num1: float,
#                num2: float,
#                mode: str = '/'):
#     if mode == '/':
#         div = num1 / num2
#         return div
#     div = num1 // num2
#     return div


def div2Number(num1: float,
               num2: float,
               mode: str = '/'):
    if mode == '/':
        div = num1 / num2
        return div
    div = num1 // num2
    return div


def div2NumberExc(num1: float,
                  num2: float,
                  mode: str = '/'):
    try:
        if mode == '/':
            div = num1 / num2
            return div
        div = num1 // num2
        return div
    except ZeroDivisionError as Exc:
        return 0


def div2NumberExc2(num1: float,
                   num2: float,
                   mode: str = '/'):
    try:
        if mode == '/':
            div = num1 / num2
            return div
        div = num1 // num2
        return div
    except Exception as Exc:
        print(type(Exc))
        return 0


if __name__ == '__main__':
    # print(div2Number(1, 2))
    # jumpNextLine()

    # print(div2Number(1, 0))
    # jumpNextLine()

    # print(div2NumberExc(1, 0))
    # jumpNextLine()

    print(type(div2NumberExc2(1, 0)))
    jumpNextLine()
