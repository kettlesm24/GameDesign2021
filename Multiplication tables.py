#Max Kettles 6-4-2021
#Multiplication table using print and range
print()
print('Multiplication tables')
print()
for base in range (0,11):
    print("Multiplication of", base)
    for var in range (0,11): 
        print (base, 'x', var, '=', base*var) 
    print()