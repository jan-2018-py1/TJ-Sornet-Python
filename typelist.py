# Assignment: Type List
# Write a program that takes a list and prints a message for each element in the list, 
# based on that element's data type.

# Your program input will always be a list. For each item in the list, test its data type. 
# If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. 
# At the end of your program print the string, the number and an analysis of what the list contains. 
# If it contains only one type, print that type, otherwise, print 'mixed'.

def typeList(val):
    newString = ''
    stringCount = 0
    sum = 0
    intCount = 0
    count = 0
    while count < len(val):
        if isinstance(val[count], str):
            newString += val[count] + " "
            stringCount += 1
        if isinstance(val[count], int) or isinstance(val[count], float):
            sum += val[count]
            intCount += 1
        count += 1
    if stringCount == 0:
        print "The list you entered is of integer type"
        print "Sum: "+ str(sum)
    if intCount == 0:
        print "The list you entered is of string type"
        print "String: "+newString+" "
    else:
        print "The list you entered is of mixed type"
        print "String: ",newString
        print "Sum: "+str(sum)

l = ['magical unicorns',19,'hello',98.98,'world']
m = [2,3,1,7,4,12]
n = ['magical','unicorns']

typeList(l)
typeList(m)
typeList(n)