#Max Kettles 6-11
import random
from typing import Counter
gameWords= ['ppython','java','trackpad','ccomputer','kkeyboard','geeks','laptop','headphones','charger','mouse','software','hardware']
answ = input ("Do you want to guess a word? ")
name = input("What is your name? ")
answ = answ.upper()
while "Y" in answ:
    print("Good Luck ", name)
    word = random.choice(gameWords)
    counter = len(word)
    print(counter)
    print(word)
    turns = 10 
    guesses =""
    while turns >0 and counter >0:
        for char in word:
            if char in guesses:
                print(char,end = " ")
            else:
                print("_", end = " ")
        new_guess = input("\n\n Give me a letter ")
        if new_guess not in word:            
            turns -=1
            print("Wrong! You have ", turns, "guesses left.")
        else:
            var2 = word.count(new_guess)
            counter = counter - var2
            guesses += new_guess
            print("Nice Guess!")

    answ = input("Would you like to play again? ")
    print(name, " thank you for playing!")
