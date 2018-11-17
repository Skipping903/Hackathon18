# TEMP: 100, 8, Prime, notPrime
import random

myArray = []
myArrayBin = []

bits_num = 4

def genDataset(myArray):
    for n in range(0, 11):
        for i in range(0, 9):
            num = random.randint(0,51)
            myArray.append(num)
            myArrayBin.append(format(num, '08b'))
            # "{0:b}".format(myArray[i])
            transDataset(myArray)
    print(myArray)
    print(myArrayBin)
        # myArray = []


def transDataset(myArray):
    for i in range(0, len(myArray)):
        if myArray[i] == 0:
            myArray[i] = 0.1
        elif myArray[i] == 1:
            myArray[i] = 0.9

genDataset(myArray)
