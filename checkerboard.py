# Assignment: Checkerboard
# Write a program that prints a 'checkerboard' pattern to the console.

def checkerboard():
    switch = 0
    string = ''
    for i in range (0,8):
        for j in range (0,8):
            if switch == 0:
                string += "*"
                switch = 1
            else:
                string += " "
                switch = 0
        print string
        if i%2 == 0:
            string = ' '
        else:
            string = ''
        

checkerboard()