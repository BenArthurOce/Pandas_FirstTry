from random import randrange
import random

def fDynamicTable_Favourte_Colour_and_Animal():

    #Data to be in table
    rPerson_Name = ["Ben","Sarah","Jimmy","Andrew","Rhys","Rhyn","Max","Boris","Pete","Marvin","Larry","Gary","Ollie","John","David","Stannis","Ethan","Lisa","Lucy","Raj","Tammy"]
    rPerson_Age = []
    rPerson_Colour = []
    rPerson_Animal = []
    rTable = [rPerson_Name, rPerson_Age, rPerson_Colour, rPerson_Animal]

    #Options to be randomized
    rOptions_Colour = ["Red","Blue","Green"]
    rOptions_Animal = ["Dog","Cat","Fish","Bird"]

    for a in range(len(rPerson_Name)):
        b = randrange(19)
        rPerson_Age.append(b)

        c = random.choice(rOptions_Colour)
        rPerson_Colour.append(c)

        d = random.choice(rOptions_Animal)
        rPerson_Animal.append(d)

    return rTable


def fStaticTable_Favourte_Colour_and_Animal():
    rPerson_Name = ["Ben","Sarah","Jimmy","Andrew","Rhys","Rhyn","Max","Boris","Pete","Marvin","Larry","Gary","Ollie","John","David","Stannis","Ethan","Lisa","Lucy","Raj","Tammy"]
    rPerson_Age = [18, 14, 2, 1, 11, 6, 14, 15, 8, 4, 4, 15, 12, 0, 2, 5, 17, 2, 8, 0, 10]
    rPerson_Colour = ['Green', 'Blue', 'Green', 'Green', 'Blue', 'Red', 'Blue', 'Green', 'Red', 'Blue', 'Blue', 'Green', 'Green', 'Red', 'Green', 'Blue', 'Blue', 'Green', 'Green', 'Blue', 'Green']
    rPerson_Animal = ['Bird', 'Fish', 'Dog', 'Dog', 'Dog', 'Bird', 'Bird', 'Dog', 'Bird', 'Cat', 'Cat', 'Bird', 'Bird', 'Fish', 'Dog', 'Fish', 'Cat', 'Fish', 'Fish', 'Fish', 'Bird']
    rTable = [rPerson_Name, rPerson_Age, rPerson_Colour, rPerson_Animal]
    return rTable


def fDynamicTable_Coordinates():
    rDataDim01 = []
    for a in range(4):
        rDataDim02 = []
        rDataDim01.append(rDataDim02)
        for b in range(6):
            z = "|Col{0}Row{1}|".format(a,b)
            rDataDim02.append(z)
    return rDataDim01



