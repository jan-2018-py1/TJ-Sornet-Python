# Odd/Even:
# Create a function called odd_even that counts from 1 to 2000. 
# As your loop executes have your program print the number of that 
# iteration and specify whether it's an odd or even number.

def odd_even():
    for x in range(1, 2001):
        if(x % 2 == 0):
            print "Number is", x, ". This number is an even number."
        else:
            print "Number is", x, ". This number is an odd number."

odd_even()


# Multiply:
# Create a function called 'multiply' that iterates through each 
# value in a list (e.g. a = [2, 4, 10, 16]) and returns a list 
# where each value has been multiplied by 5.

def multiply(myList, mult):
    for val in range(len(myList)):
        myList[val] = myList[val]* mult
    return myList

a = [2, 4, 10, 16]
b = multiply(a, 5)
print b


# Hacker Challenge:
# Write a function that takes the multiply function call as an argument. 
# Your new function should return the multiplied list as a 
# two-dimensional list. Each internal list should contain the 
# 1's times the number in the original list. 

def layered_multiples(arr):
    new_array = []
    for x in range(len(arr)):
        newList = []
        for y in range(0, arr[x]):
            newList.append(1)
        new_array.append(newList)
    return new_array


x = layered_multiples(multiply([2,4,5],3))
print x

    
