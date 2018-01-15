# Assignment: Making Dictionaries
# Create a function that takes in two lists and creates a single 
# dictionary. The first list contains keys and the second list 
# contains the values. Assume the lists will be of equal length.

# Your first function will take in two lists containing some strings. 
# Here are two example lists:

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(list1, list2):
    new_dict = {}
    # your code here
    if len(list1) >= len(list2):
        animals = zip(list1, list2)
        new_dict = dict(animals)
    else:
        animals = zip(list2, list1)
        new_dict = dict(animals)
    return new_dict

print make_dict(name,favorite_animal)
