#Part 2
def calculate(a, b):
    perimeter = a + a + b + b
    return perimeter;

def main():
    myPerimeter = calculate(1, 2)
    print(myPerimeter)

main()

#Part 3
myNum = int(input("Enter a number between 1 and 10: "))

if (myNum < 5):
    print("Your number is less than 5")
elif (myNum > 5):
    print("Your number is greater than 5")
else:
    print("Your number is equal to 5")

#Part 4
userNum = int(input("Enter a number between 1 and 10: "))

while userNum <= 50:
    userNum = userNum * 4
    print("Current value:", userNum)

#Part 5
userInt = int(input("Enter an integer: "))

for i in range (0, userInt):
    print("snowman")

#Part 6
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

userNum = int(input("Enter a number between 1 and 10: "))

def multBy4(aNum):
    while aNum <= 50:
        aNum = aNum * 4
        print("Current value:", aNum)
    return;

multBy4(userNum)

userInt = int(input("Enter an integer: "))

def printSnowman(snowmanInt):
    for i in range (0, snowmanInt):
        print("snowman")
    return;

printSnowman(userInt)
