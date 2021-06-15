import random
import time
#Max Kettles 6-7
#Menu pratice
planets = ["Lunrailia", "Runetera", "Uchillon", "Degeshan", "Zuiliv", "Corus", "Cizahiri", "Treigawa", "Geon", "Vadus"] #list of planets used by random 
x = 10 # var for loop so when we change the var program stops
while x == 10: # loop
    print("***********************") #menu
    print("* Astronaut Adventure *")
    print("*        Menu         *")
    print("*                     *")
    print("*   1.-First Planet   *")
    print("*   2.-Second Planet  *")
    print("*   3.-Leaderboard    *")
    print("*   4.-Upper Case     *")
    print("*   5.-Lower Case     *")
    print("*   6.-Quit Game      *")
    print("***********************")
    answ = input("Which option do you chose? (1-6): ") #input is able to select option from menu 
    answ = answ[0]
    if answ.isdigit():
        answ = int(answ)
    else:
        print("Error: input is not 1-6")
    if answ == 1: #Option 1 is first planet
        planets1 = random.choice(planets)
        print("Good luck on" ,planets1,"\n")
        time.sleep(2)
        print("Travling to " ,planets1,"\n")
        time.sleep(2)
        print("You have arrived at", planets1,"\n")
        #by Jgs
        print("""
                         *       +
           '                  |
       ()    .-.,="``"=.    - o -
             '=/_       \     |
          *   |  '=._    |
               \     `=./`,        '
            .   '=.__.=' `='      *
   +                         +
        O      *        '       .
        """)
        input("Press enter to continue\n")
    if answ == 2:#2nd planet
        planets2 = random.choice(planets)
        print("good luck on" ,planets2,"\n")
        time.sleep(2)
        print("travling to " ,planets2,"\n")
        time.sleep(2)
        print("You have arrived at", planets2,"\n")
        #by Jgs
        print("""
             _____
          .-'.  ':'-.
        .''::: .:    '.
       /   :::::'      \\
      ;.    ':' `       ;
      |       '..       |
      ; '      ::::.    ;
       \       '::::   /
        '.      :::  .'
           '-.___'_.-'
        """)
        input("\nIf you wish to return home, press enter\n")
    if answ == 3: #leaderboard
        print("\n***********************")
        print("*       Top Score       *")
        print("*    Max-95234843pts    *")
        print("*************************")
        input("Press enter to continue\n")
    if answ == 4:
        print("Input a phrase you want capitalised")
        phrase = input()
        phrase = phrase.upper()
        print(phrase) 
        input("Press enter to continue\n")
    if answ == 5:
        print("Input a phrase you want lowercased")
        phrase = input()
        phrase = phrase.lower()
        print(phrase) 
        input("Press enter to continue\n")
    if answ == 6:
        x = 1000
        print("\nGoodbye\n")