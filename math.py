#Max Kettles
#We will print a multiplication table for 2 using print

x=5 #define x
y=7 #define y
print (x+y) #add them togehter

z = 2 #define what you want to multiply
for i in range (0,11): print (z, 'x', i, '=', z*i) #the "For range" makes each line change its value then print what the value goes into 
z = 3
for i in range (0,11): print (z, 'x', i, '=', z*i)
print()
for z in range (1,11): 
    for i in range (1,11): print (z, 'x', i, '=', z*i) 
    print()