import random
dictout = open("dict.txt", "r")
list_dict = [(line.strip()).split() for line in dictout]
dictout.close()

def menuvalid(input):
    try:
        val = int(input)
    except ValueError:
        print("input numbers only")
        
def check(attempt_break, y): 
    # returns a list of booleans
    result = [characters in y for characters in attempt_break]
    return result
print("***************WELCOME TO WORDLE***************")
    
def menu():
    menuinput = int(input("Enter 1 to start or 2 to Exit"))#Menu point
    menuvalid(menuinput)
    while menuinput != 2:
        if menuinput == 3:
            print("***************TROUBLESHOOT SCREEN***************")
            print("Printing Dictionary")
            print(list_dict) #Print dictionary in one array
            rand_dict = random.choice(list_dict) # Test random point in array
            print("RANDOM WORD FROM LIST ", rand_dict)
            print("TOTAL AMOUNT OF WORDS IN DICTIONARY IS ", len(list_dict))
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
