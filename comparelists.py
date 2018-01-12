# Assignment: Compare Lists
# Write a program that compares two lists and prints a message depending on if the inputs are identical or not.

# Your program should be able to accept and compare two lists: list_one and list_two. 
# If both lists are identical print "The lists are the same". 
# If they are not identical print "The lists are not the same." 

def compareLists(list_one, list_two):
    count = 0
    max = 0
    compareCount = 0
    if len(list_one) != len(list_two):
        print "The lists are not the same."
    else:
        while count < len(list_one):
            if list_one[count] != list_two[count]:
                compareCount += 1
            count += 1
        if compareCount == 0:
            print "The lists are the same."
        else:
            print "The lists are not the same."


listOne = [1,2,5,6,2]
listTwo = [1,2,5,6,2]

list_three = [1,2,5,6,5]
list_four = [1,2,5,6,5,3]

list_five = [1,2,5,6,5,16]
list_six = [1,2,5,6,5]

list_seven = ['celery','carrots','bread','milk']
list_eight = ['celery','carrots','bread','cream']

compareLists(listOne, listTwo)
compareLists(list_three, list_four)
compareLists(list_five, list_six)
compareLists(list_seven, list_eight)