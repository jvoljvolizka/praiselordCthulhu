import random
from sys import stdout
from time import sleep

# ------------------------------[Import End]------------------------------#
new_txt_list = []
# ------------------------------[Function End]------------------------------#
def rand2(end):  # <-------------[Create index list]
    lis = []
    end = int(end)
    for i in range(0, end):
        lis.append(i)
    return lis
# print(lis)
# ------------------------------[Function End]------------------------------#
def theanswer(answer, basevar, convar):  # <-------------[Convert the key to base 100]
    table = {"0": 0,
             "1": 1,
             "2": 2,
             "3": 3,
             "4": 4,
             "5": 5,
             "6": 6,
             "7": 7,
             "8": 8,
             "9": 9,
             "A": 10,
             "B": 11,
             "C": 12,
             "D": 13,
             "E": 14,
             "F": 15,
             "G": 16,
             "H": 17,
             "I": 18,
             "J": 19,
             "K": 20,
             "L": 21,
             "M": 22,
             "N": 23,
             "O": 24,
             "P": 25,
             "Q": 26,
             "R": 27,
             "S": 28,
             "T": 29,
             "U": 30,
             "V": 31,
             "W": 32,
             "X": 33,
             "Y": 34,
             "Z": 35,
             "a": 36,
             "b": 37,
             "c": 38,
             "d": 39,
             "e": 40,
             "f": 41,
             "g": 42,
             "h": 43,
             "i": 42,
             "j": 43,
             "k": 44,
             "l": 45,
             "m": 46,
             "n": 47,
             "o": 48,
             "p": 49,
             "q": 50,
             "r": 51,
             "s": 52,
             "t": 53,
             "u": 54,
             "v": 55,
             "w": 56,
             "x": 57,
             "y": 58,
             "z": 59,
             "'": 60,
             "!": 61,
             "^": 62,
             "#": 63,
             "%": 64,
             "&": 65,
             "/": 66,
             "(": 67,
             ")": 68,
             "=": 69,
             "?": 70,
             '"': 71,
             ",": 72,
             ">": 73,
             "£": 74,
             "$": 75,
             "½": 76,
             "¾": 77,
             "{": 78,
             "[": 79,
             "]": 80,
             "}": 81,
             "é": 82,
             "_": 83,
             "-": 84,
             "*": 85,
             "+": 86,
             ".": 87,
             " ": 88,
             "|": 89,
             "@": 90,
             "İ": 91,
             "ğ": 92,
             "Ğ": 93,
             "ş": 94,
             "Ş": 95,
             "ç": 96,
             "Ç": 97,
             "ö": 98,
             "Ö": 99,
             "ı": 100}
    answer

    integer = 0
    # basevar = 10
    # convar = 100
    for char in str(answer):
        value = table[char]
        integer *= basevar
        integer += value
    array = []
    tablesy = dict(map(reversed, table.items()))
    while integer:
        integer, value = divmod(integer, convar)
        array.append(tablesy[value])
    return ''.join(reversed(array))
# ------------------------------[Function End]------------------------------#
def printkey(keyf):  # <-------------[Create a .key file]
    keyfile = open(filenamei + ".key", "w")
    #keyfile.write("#------------------------------[Key Start]------------------------------#\n")
    keyfile.write(keyf)
    keyfile.write("\n")
    #keyfile.write("#------------------------------[Key End]------------------------------#")
# ------------------------------[Function End]------------------------------#
def key_create(keylist):  # <-------------[Create a key]
    keyraw = ''.join(str(e) for e in keylist)
    keyraw = int(keyraw)
    return theanswer(keyraw, 10, 16)
# ------------------------------[Function End]------------------------------#
def randomizer(filename):  # <-------------[Main function]

    # open file and create a shuffled list
    fileopen = open(filename, "r")
    fileread = fileopen.read()
    fileopen.close()
    a = len(fileread)
    len_list = rand2(a)
    random.shuffle(len_list)
    # key create
    if keywant == True:
        key = key_create(len_list)
        # key = key_create_new(len_list)
        printkey(key)
        print(len(key))
    # print(len_list)
    # randomize contents
    for c in range(0, a):
        new_txt_list.append(fileread[len_list.pop()])
        stdout.write("\rprocessing..." + "%d" % c + "/%d" % int(a - 1))
        stdout.flush()

    # sleep(1)
    stdout.write("\n")
    # debug print(new_txt_list)
    new_txt = ''.join(new_txt_list)
    # debug print(new_txt)
    fileopen = open(filename, "w")
    fileopen.write(new_txt)
    fileopen.close()
# print(len_list)
# ------------------------------[Function End]------------------------------#
def key_create_new(key_list):
    return str(key_list)
# ------------------------------[Function End]------------------------------#
print("(1) Encryption mode")
# print("(2) Decyription mode")
print("(3) Exit")
modesel = input()
if modesel == "1":
    filenamei = input("please enter name of the file: \n")
    keyin = input("Do you want a key ? y/n: \n")
    if keyin == "y":
        keywant = True
    else:
        keywant = False
    randomizer(filenamei)

elif modesel == "2":
     #decoder()
    print()
elif modesel == "3":
    exit()
# ------------------------------[Function End]------------------------------#
def exit():
    print("bye")
# ------------------------------[Function End]------------------------------#

