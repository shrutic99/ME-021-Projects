##User input
x=input('What day are you interested in? ');

##dictionary for which weekday will have which meal
weekdays = {'Monday': 'Spagetti Bolognase', 'Tuesday': 'Cheese Burger', 'Wednesday': 'Chow mein', 'Thursday':'pizza', 'Friday':'Grilled Salmon'}

##Saturday and Sunday share the same print message
if x == 'Saturday' or x == 'Sunday':
    print(f'{x} is not in the menu!')
else:
    print(f'The food choice for {x} is {weekdays[x]}')

