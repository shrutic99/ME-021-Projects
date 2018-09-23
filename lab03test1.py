x = int(input('a number: '));

m=2
n=1
a = m**2-n**2
b = 2*m*n

while m>n:
    while a<=x and b<=x:
        m=m+1
        n=n+1
        c = ((a**2)+(b**2))**(1/2)
        if (c).is_integer():
            if c%2 == 0 and c<=x:
                print (a,b,c);
