# Les classes (Part 8)
# Constructeur des classes


def jumpNextLine():
    print('\n')


def dividerLine():
    print('---------------------------')


class A:
    def __init__(self,
                 name: str,
                 sex: str,
                 age: int):
        self.name = name
        self.sex = sex
        self.age = age

    def __repr__(self):
        return f"Personne -> \n\
        ----------------------------\n\
        De Nom: {self.getName()} \n\
        De sexe: {self.getSex()}\n\
        Et d'age': {self.getAge()}\n\
        ----------------------------"

    def __len__(self):
        return 1

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.__dict__ == other.__dict__:
                return True
        return False

    def getName(self) -> str:
        return self.name

    def getSex(self) -> str:
        return self.sex

    def getAge(self) -> int:
        return self.age


if __name__ == '__main__':
    # Instancier la classe:
    var_a = A(
        'Fall',
        'Masculin',
        28
    )

    print(var_a)
