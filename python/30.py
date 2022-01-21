# Les classes (Part 7)
# Ecriture des fonctions de bases (fonction magiques)


def jumpNextLine():
    print('\n')


def dividerLine():
    print('---------------------------')


class A:
    name = 'Ali'
    sex = 'Masculin'
    age = 28

    def __repr__(self):
        return f"Personne -> \n\
        ----------------------------\n\
        De Nom: {self.getName()} \n\
        De sexe: {self.getSex()}\n\
        Et d'age': {self.getAge()}\n\
        ----------------------------"

    def __len__(self):
        return 1

    # naive method
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.getName() == other.getName() \
                    and self.getSex() == other.getSex() \
                    and self.getAge() == other.getAge():
                return True
        return False

    # Proper way to __eq__
    # def __eq__(self, other):
    #     if isinstance(other, self.__class__):
    #         if self.__dict__ == other.__dict__:
    #             return True
    #     return False

    def getName(self) -> str:
        return self.name

    def getSex(self) -> str:
        return self.sex

    def getAge(self) -> int:
        return self.age


if __name__ == '__main__':
    # Instancier la classe:
    var_a1 = A()
    var_a2 = A()
    var_a3 = list()

    print(var_a1)

    jumpNextLine()
    dividerLine()
    print(f'Longeur est: {len(var_a1)}')
    dividerLine()

    jumpNextLine()
    dividerLine()
    print(var_a1 == var_a2)
    dividerLine()

    jumpNextLine()
    dividerLine()
    print(var_a1 == var_a3)
    dividerLine()
