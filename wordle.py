import random
dictout = open("dict.txt", "r")
list_dict = [(line.strip()).split() for line in dictout]
dictout.close()
def check(attempt_break, y): 
    # returns a list of booleans
    result = [characters in y for characters in attempt_break]
    return result
def menu():
    print("Welcome to wordle")
    menuinput = int(input("Enter 1 to start or 2 to Exit")) #Menu point
    while menuinput != 2:
        if menuinput == 3:
            print("TROUBLESHOOT SCREEN")
            print("Ready to print dictionary")
            print(list_dict) #Print dictionary in one array
            x = random.choice(list_dict) # Test random point in array
            print(x)
            y = list(x)
            print (y)
            menu()
        if menuinput == 1:
            maindef() #start main game after pressing 1
        elif menuinput != 1 or 3:
            print("wrong input")
            menuinput = int(input("Enter 1 to start or 2 to Exit"))
    if menuinput == 2:
        quit()
def maindef():
    print("Begin game")
    rand_dict = random.choice(list_dict)
    y = list(rand_dict)
    counter = 1
    while counter != 6:
        attempt = str(input("Enter your guess")).upper()
        attempt_break = list(attempt)
        if attempt_break == y:
            print(check(attempt_break,y))
            print("Correct! You've got in", counter, "Attempts")
        else:
            print("wrong")
            print(check(attempt_break,y))
        counter += 1
    menu()
###Main running code###
menu()




