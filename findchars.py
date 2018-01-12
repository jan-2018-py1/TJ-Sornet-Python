# Assignment: Find Characters
# Write a program that takes a list of strings and a string containing a single character, 
# and prints a new list of all the strings containing that character.

def findChars(myList, char):
    newList = []
    for val in myList:
        if val.find(char) != -1:
            newList.append(val)
    print newList

word_list = ['hello','world','my','name','is','Anna']
char = 'm'

findChars(word_list, char)