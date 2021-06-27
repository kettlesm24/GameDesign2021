#Max Kettles 6-10
#In this program I will make menu for the many functions of a list
import random
import time
numbers = []
x = 10
while x == 10:
    print("***********************") #menu
    print("*  Number Adventure   *")
    print("*        Menu         *")
    print("*                     *")
    print("*   1.-Input List     *")
    print("*   2.-Remove Element *")
    print("*   3.-Find Element   *")
    print("*   4.-Random Element *")
    print("*   5.-Reverse list    *")
    print("*   6.-Exit            *")
    print("***********************")
    answ = int(input("Which option do you chose? (1-5): "))
    if answ == 1:#this first part gives the user a chance to put their own values in the list
        num1 = input("What is the first number?")  
        numbers.append(num1)
        num2 = input("What is the second number?")  
        numbers.append(num2)
        num3 = input("What is the third number?")  
        numbers.append(num3)
        num4 = input("What is the fourth number?")  
        numbers.append(num4)
        num5 = input("What is the fith number?")  
        numbers.append(num5)
        print(numbers)
        input("\nIf you wish to return home, press enter\n")
    if answ == 2:#Removes a slected var from the list
        print(numbers)
        removed = input("Which number do you wish to remove? ")
        numbers.remove(removed)
        print(numbers)
        input("\nIf you wish to return home, press enter\n")
    if answ == 3:#Finds slected value
        print(numbers)
        indx1 = input("What number do you wish to find? ")
        indx2 = numbers.index(indx1)
        print(indx1, "is located in postion", indx2)
        input("\nIf you wish to return home, press enter\n")
    if answ == 4:
        rand1 = random.choice(numbers)
        print("Your random number is ", rand1)
    if answ == 5:#reverses list
        numbers.reverse
        print(numbers)
        input("\nIf you wish to return home, press enter\n")
    if answ == 6:#exits
        x = 1000
        print("\nGoodbye\n")

