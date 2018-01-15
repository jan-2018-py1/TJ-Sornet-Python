# Assignment: Coin Tosses
# Write a function that simulates tossing a coin 5,000 times. 
# Your function should print how many times the head/tail appears.
import random
def coinTosses():
    head = 0
    tail = 0
    print "Starting the program..."
    for x in range (1, 501):
        randomNum = round(random.random())
        if randomNum == 1:
            head += 1
            print "Attemp #", x,":Throwing a coin... It's a head ... Got", head, "head(s) so far and", tail, "tail(s) so far"
        else:
            tail += 1
            print "Attemp #", x,":Throwing a coin... It's a tail ... Got", head,"head(s) so far and", tail, "tail(s) so far"
    print "Ending the program, thank you!"

coinTosses()