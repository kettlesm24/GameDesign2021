#Max Kettles 6-11
import random
from typing import Counter
gameWords= ['ppython','java','trackpad','ccomputer','kkeyboard','geeks','llaptop','headphones','charger','mmouse','ssoftware','hardware']
name = input("What is your name? ")
def menu():
    print("***********************") #menu
    print("*     Word Game       *")
    print("*        Menu         *")
    print("*                     *")
    print("*   1.-Play Game      *")
    print("*   2.-Leaderboard    *")
    print("*   3.-Quit Game      *")
    print("***********************")
menu()
answ = input("Which option do you chose? ")
while "1" in answ:
    print("Good Luck ", name)
    word = random.choice(gameWords)
    counter = len(word)
    print(counter)
    print(word)
    turns = 10 
    guesses =""
    def wrdprint(word):
        for char in word: # prints out dashes and letters
                if char in guesses:
                    print(char,end = " ")
                else:
                    print("_", end = " ")
    while turns >0 and counter >0:
        wrdprint(word)
        new_guess = input("\n\nGive me a letter ")
        if new_guess not in word:            
            turns -=1
            print("Wrong! You have ", turns, "guesses left.")
        else:
            var = word.count(new_guess)
            counter = counter - var
            print("Nice Guess!")
        guesses += new_guess
    wrdprint(word)
    if(counter == 0):
        print("\nYou won")
    else:
        print("Sorry your too dumb")
    menu()
    answ = input("Which option do you chose? ")
while "2" in answ:
    print("working")
    menu()
    answ = input("Which option do you chose? ")
while "3" in answ:
    answ = "4"
    print()
    
print(name, " thank you for playing!")
