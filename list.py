#Max Kettles 6-10
# learing how to use a list
# I previously used a list to select a random planet from a list in my menu file
import random
from typing import Counter
planets = ["Lunrailia", "Runetera", "Uchillon", "Degeshan", "Zuiliv", "Corus", "Cizahiri", "Treigawa", "Geon", "Vadus"]
#print(planets)
#for planet in planets:
#    print(planet)
#or planet in planets:
    #print(planet, end=" , ")
#if "Corus" in planets:
    #print("Yes, Corus is in the list")
Counter=len(planets)
#for x in range[0,Counter-1]:
    #print(planets[x], end=" , ")
#print(Counter)
planets.remove("Corus")
for planet in planets:
    print(planet, end=" , ")
