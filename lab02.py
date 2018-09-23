##problem 1
##fullname = input('Write your name: ');
##year = input('Write your year of birth: ');
##year = int(year);
##print(f'Your name is {fullname} and your year of birth is {year}!');

##problem 2
a = input('Enter a number of your choice: ');
b = input('Enter another number of your choice: ');
c = input('Enter your last number of your choice: ');

a = int(a)
b = int(b)
c = int(c)


if (a>b) and (a>c):
    largest = a
elif (b>a) and (b>c):
    largest = b
elif (c>a)and (c>b):
    largest = c
else:
    print('N/A')

print(f' The largest of the numbers entered is {largest}');


##problem 3
P0 = input('Enter your initial deposit: ');
r = input('Enter your annual interest: ');
n = input('Enter your number of times your interest is compounded per year: ');
t = input('Enter your total number of years: ');

P0 = int(P0)
r = int(r)
n = int(n)
t = int(t)

for x in range(1,t+1):
    P = P0*((1+((r/100)/n))**(n*x))
    o = round(P,2)
    print(f'After year {x}, the amount in the account is {o}.');

