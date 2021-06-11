numbers = []
#["Lunrailia", "Runetera", "Uchillon", "Degeshan", "Zuiliv"]
# creating an empty list
# number of elemetns as input
x = 10
while x == 10:
    print("***********************") #menu
    print("*  Number Adventure   *")
    print("*        Menu         *")
    print("*                     *")
    print("*   1.-Input List     *")
    print("*   2.-Delet Element  *")
    print("*   3.-Find Element   *")
    print("*   4.Reverse list    *")
    print("*   5.Exit            *")
    print("***********************")
    answ = int(input("Which option do you chose? (1-5): "))
    if answ == 1:
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
    if answ == 2:
        print(numbers)
        removed = input("Which number do you wish to remove? ")
        numbers.remove(removed)
        print(numbers)
        input("\nIf you wish to return home, press enter\n")
    if answ == 3:
        print(numbers)
        inx1 = input("What number do you wish to find? ")
        inx2 = numbers.index(inx1)
        print(inx1, "is located in postion", inx2)
        input("\nIf you wish to return home, press enter\n")
    if answ == 4:
        numbers.reverse
        print(numbers)
        input("\nIf you wish to return home, press enter\n")
    if answ == 5:
        x = 1000
        print("\nGoodbye\n")

