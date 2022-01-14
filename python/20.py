# functions and class (Part 2)

def jumpNextLine():
    print('\n')


def transformStringInList(string: str,
                          specialCharacter: str,
                          treat: bool = True):
    def getListFromString():
        rect = []
        data = string.split(specialCharacter)
        if isinstance(data, list):
            return data
        return rect.append(data)

    def capitalizeWorld():
        data = getListFromString()
        data = [x.capitalize() for x in data]
        return data

    def main():
        if treat:
            return capitalizeWorld(), 'Treatment is done.'
        return data, 'Treatment is abort.'

    return main()


if __name__ == '__main__':
    res = transformStringInList('You and I', ' ')
    jumpNextLine()
    print(res)
    jumpNextLine()
    print(res[0])
    jumpNextLine()
    print(res[1])
    jumpNextLine()
