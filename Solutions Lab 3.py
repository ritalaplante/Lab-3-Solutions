#Rita LaPlante
#My Solutions to lab 1

#Part 1: see other document in Lab 3 solutions

#Part 2: Write the perimeter example using two functions
#one function should calculate the perimeter and the other should
#be a main function

#This is how you define a function
#calculate is the function name and a and b
#are the arguments of this function
def calculate(a, b):
    #here the function calculates the perimeter using the values
    #provided as the argument when the functionis called
    perimeter = a + a + b + b
    #the function returns the value of the perimeter
    return perimeter;

#main function: here is where I make my function calls and print statements
#Here I define a variable called myPerimeter and I assign its value to the value
#returned by calculate with arguments 1 for a and 2 for b
myPerimeter = calculate(1, 2)
print(myPerimeter)

#Part 3 if statements
#write a program between 1 and 10, report back
#whether that number is less than or more than 10

myNum = int(input("Enter a number between 1 and 10: "))

#Here python checks the first condition and if the number you
#input is less than 5 python will execute the print statement associated
#with the if statement
if (myNum < 5):
    print("Your number is less than 5")
#Here is the elif statement (else if) this, like the if statement will check
#if the number you inputed is greater than 5 and if this condition is satisfied
#python will print the value associated with this statement.
elif (myNum > 5):
    print("Your number is greater than 5")
#Here is the else statement. This is the catch all statement it will catch any
#other instance that is not captured by the if or elif statements
#in this case the only outstanding condition is myNum = 5
else:
    print("Your number is equal to 5")

#part 4 while loop
#write a program that asks the user to enter int btwn 1 and 10
#mutliply that number by 4 until it is greater than 50
#report the value after each multiplication
  
userNum = int(input("Enter a number between 1 and 10: "))

#This while loop will execute while the userNum variable is less than or equal
#to 50
while userNum <= 50:
    #realize that the while loop increases the value after each loop to ensure
    #that you don't get stuck in the dreaded infinite loop
    userNum = userNum * 4
    print("Current value:", userNum)

#part 5 for loop
#write a program that asks the user to enter an integer
#print out the word snowman that many times

userInt = int(input("Enter an integer: "))

#The range function tells python to execute the for loop for each value
#specified in the range. NOTE: the range function is NOT inclusive, for instance
#the for loop which iterates through range (1, 5) will execute 4 times not 5 times
#range (0, 5) will execute 5 times (for vales 0-4)
#in more complicated functions deciding what to use as your range vales is
#extremely important. Also not that by default python increments by 1 with every
#iteration of the for loop
for i in range (0, userInt):
    print("snowman")

#part 6 do parts 3, 4, and 5, but using functions
#part 3 as function:

#This is the same general idea, but now they are functions. Unlike the caclulate
#function above these functions do not return anything instead they only print
#values
myNum = int(input("Enter a number between 1 and 10: "))

def isLessThan5(userNum):
    if (userNum < 5):
        print("Your number is less than 5")
    elif (userNum > 5):
        print("Your number is greater than 5")
    else:
        print("Your number is equal to 5")
    return;

isLessThan5(myNum)

#part 4 as a function
userNum = int(input("Enter a number between 1 and 10: "))

def multBy4(aNum):
    while aNum <= 50:
        aNum = aNum * 4
        print("Current value:", aNum)
    return;

multBy4(userNum)

#part 5 as a function

userInt = int(input("Enter an integer: "))

def printSnowman(snowmanInt):
    for i in range (0, snowmanInt):
        print("snowman")
    return;

printSnowman(userInt)
    
