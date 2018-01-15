# Assignment: Making and Reading from Dictionaries
# Create a dictionary containing some information about yourself. 
# The keys should include name, age, country of birth, favorite 
# language.

# There are two steps to this process, building a dictionary 
# and then gathering all the data from it. Write a function that 
# can take in and print out any dictionary keys and values.


myDictionary = {
    "name": "TJ Sornet",
    "age": 35,
    "country of birth": "Philippines",
    "favorite language": "Python"
}

def printDictionary(dict):
    for key, value in dict.iteritems():
        print "My", key, "is", value

printDictionary(myDictionary)

def getKeysValues(dict, key):
    print "Key:", key 
    print "Value:", dict.get(key)

getKeysValues(myDictionary, "name")



