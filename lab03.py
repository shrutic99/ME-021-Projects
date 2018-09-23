

#user input
x = int(input('a number: '));

a=0

d=0
e = -1

#
while a<=x:
    #keeps increasing 'a' by 2
    a=a+2
    b=0
    while b<=x:
        #increases 'b' by 2
        b=b+2
        c = ((a**2)+(b**2))**(1/2)

        if c%2 == 0 and c<x:
            if c != d:
                print (a,b,c);
                #created a variable d in the loop so once d=c, no pythogorean triple will print twice
                d = c

        if c%2 == 0 and c == x:
            #if 'c' does not equal to 'd,' the pythogorean triple will print
            if c != d:
                print (a,b,c);
                #e is meant to break any repeating c values so no variation of the pythagorean triple repeats
                e = -2
                break
       #this break is meant to break the while loop on the max value   
    if e == -2:
        break
       
       

    
            

            
        





        
        
 
