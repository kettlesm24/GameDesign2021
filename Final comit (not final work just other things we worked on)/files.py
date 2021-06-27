import os
import sys
import time

time.sleep(2)
os.system("cls")

file = input("What is the name of the file")
if os.path.exists(file):
    PEN=open(file,"r")
    print(PEN.read())
    PEN.close()
else:
    print("this file does not exist")
fileName="Maxgame.txt"
FILE=open(fileName,"w")
FILE.write("*************** THIS IS MAX's FILE ************")
FILE.close()

