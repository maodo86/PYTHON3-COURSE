# Lecture / Ecriture dans les fichiers (Part 1)
#
# with open('filename', 'r') as f: # able to read data from file ( also is the default mode when opening a file in python)

# with open('filename', 'x') as f: # Creates new file, if it already exists it will cause it to fail

# with open('filename', 't') as f: # opens the file in text mode (also is defualt)

# with open('filename', 'b') as f: # Use if your file will contain binary data

# with open('filename', 'w') as f: # Open file with ability to write, will also create the file if it does not exist (if it exists will cause it to fail)

# with open('filename', '+') as f: # Opens file with reading and writing


def jumpNextLine():
    print('\n')


def openFile(filename: str):
    with open(filename, 'r') as f:
        print(f.read())
        f.close()


# def openFile(filename: str):
#     with open(filename, 'r') as f:
#         print(f.read(10))
#         f.close()


# def openFile(filename: str):
#     with open(filename, 'r') as f:
#         print(f.readlines())
#         f.close()


# def openFile(filename: str):
#     with open(filename, 'r') as f:
#         for line in f.readlines()
#             print(line)
#         f.close()


if __name__ == '__main__':
    jumpNextLine()
    openFile('files/file1.txt')
