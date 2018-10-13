#User Input
a = int(input('A value for a: '));
b = int(input('A value for b: '));
gamma = int(input('Input an angle in degrees: '));

#Importing the math module
import math
#Converting degrees to radians
radians = math.radians(gamma)

#The equation for the law of cosines. 
c = math.sqrt((a**2)+(b**2)-2*a*b*math.cos(radians)); 

print('The distance c is equal to: ', c);
