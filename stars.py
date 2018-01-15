# Assignment: Stars
# Part I
# Create a function called draw_stars() that takes a list of 
# numbers and prints out *.

def stars(list):
    for val in range(len(list)):
        starString = ''
        for y in range(0, list[val]):
            starString += '*'
        print starString


x = [4, 6, 1, 3, 5, 7, 25]
stars(x)

# Part II
# Modify the function above. Allow a list containing integers 
# and strings to be passed to the draw_stars() function. 
# When a string is passed, instead of displaying *, display the 
# first letter of the string according to the example below. 
# You may use the .lower() string method for this part.

def modifiedStars(list):
    for val in range(len(list)):
        starString = ''
        if isinstance(list[val],int):
            for y in range(0, list[val]):
                starString += '*'
        else:
            for x in range(len(list[val])):
                starString += list[val][0].lower()
        print starString

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
modifiedStars(x)