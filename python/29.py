# Les classes (Part 6)
# Ajout de fonctions dans une classe


def jumpNextLine():
    print('\n')


def dividerLine():
    print('---------------------------')


class A:
    name = 'Ali'
    sex = 'Masculin'
    age = 28

    def getName(self) -> str:
        return self.name

    def getSex(self) -> str:
        return self.sex

    def getAge(self) -> int:
        return self.age

    def setName(self, newName: str) -> str:
        self.name = newName

    def setSex(self, newSex: str) -> str:
        self.sex = newSex

    def setAge(self, newAge: int) -> int:
        self.age = newAge


class B(A):
    pass


if __name__ == '__main__':
    # Instancier la classe:
    var_a = A()
    var_b = B()

    dividerLine()
    print(var_a.name)
    print(var_a.sex)
    print(var_a.age)
    dividerLine()

    jumpNextLine()
    dividerLine()
    print(var_b.name)
    print(var_b.sex)
    print(var_b.age)
    dividerLine()

    jumpNextLine()
    dividerLine()
    # Modify values of attributs
    var_b.setName('Sarr')
    var_b.setSex('Masculin')
    var_b.setAge(38)
    print(var_b.name)
    print(var_b.sex)
    print(var_b.age)
    dividerLine()

    jumpNextLine()
    dividerLine()
    # Modify values of attributs
    var_a.setName('FALLOU')
    var_a.setSex('Masculin')
    var_a.setAge(18)
    print(var_a.name)
    print(var_a.sex)
    print(var_a.age)

    dividerLine()
    print(var_b.name)
    print(var_b.sex)
    print(var_b.age)
    dividerLine()
