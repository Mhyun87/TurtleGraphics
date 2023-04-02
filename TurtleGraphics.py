from turtle import Turtle

#Turtle Graphics Programming
#Marlon Hyun

#function to let user select drawing command
def showMainMenu() :
    print("")
    print("What do you want to do ?")
    print("     Enter F to move Forward")
    print("     Enter L to move Left")
    print("     Enter R to move Right")
    print("     Enter C to Select Color")
    print("     Enter Q to Quit")

#function to let user select color
def showColorMenu():
    print("")
    print("What color do you want?")
    print("     Enter R for Red")
    print("     Enter G for Green")
    print("     Enter B for Blue")

#function to return user choice
def getChoice():
    choice = input("Enter you choice : ")
    choice = choice.upper()
    return choice

#main program starts here
print("Turtle graphics")

#create a turtle object and initialize its state
t = Turtle()
t.shape("turtle")
t.down()
t.width(3)
t.pencolor("red")

#this is how far the turtle moves for each step
stepsize = 10
showMainMenu()
choice = getChoice()

#process user main menu choice

while choice != "Q" :
    #process user main menu chioce
    if choice == 'F' :
        t.fd(stepsize)
    elif choice == 'L' :
        t.left(90)
        t.fd(stepsize)
    elif choice == 'R' :
        t.right(90)
        t.fd(stepsize)
    elif choice == 'C' :
        # get user cholor choice
        showColorMenu()
        choice = getChoice()
        # process user color choice
        if choice == 'R' :
            color = "red"
        elif choice == 'B':
            color = "blue"
        elif choice == 'G':
            color = "green"
        else :
            color = "red"
        t.pencolor(color)
        showMainMenu()
    choice = getChoice()
