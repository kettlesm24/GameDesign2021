while True:
#Max Kettles 6-4-2021
#Multiplication table using a input from the user
    print('\nMath tables')
    print("\nWhat is the base?\n")
    base=int(input()) 
    print("\nAddition table of" ,base,"\n")
    for var in range (0,11): 
        print (base, '+', var, '=', base+var)
    print("\nSubtraction table of" ,base,"\n")
    for var in range (0,11): 
        print (var, '-', base, '=', var-base)
    print("\nMultiplication table of" ,base)
    for var in range (0,11): 
        print (base, 'x', var, '=', base*var) 
    print("\nDivision table of" ,base,"\n")
    for var in range (1,11): 
        print (base, '/', var, '=', base/var)
    