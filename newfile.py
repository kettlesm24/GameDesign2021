import os
import sys
import time
import datetime
os.system('cls')

#FILE="dict.txt"
#file=open(FILE, 'r')
#content = file.read()
#print(content)
#file.close()
#file = open(FILE, 'r')
#content_list = file.readlines()
#print(content_list)
#file.close()
#for element in content_list:
#    print('line : ', element)
#   element_list= element.split
#    print(element_list)


file = open("dict.txt","r")
sort = file.readlines()
sortedscores = sorted(sort,reverse=True)[::-1]
print("Top 5 scores:")
print("Pos, Name, Date, Points\n")
for line in range(5):
    print(str(line+1)+" "+str(sortedscores[line]))
file.close()
