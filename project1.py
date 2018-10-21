holiday = input ('Summer or Winter: ')
destTemp = input ('Cold or Warm: ')
#city = input ('enter a city: ')

##if destTemp = Cold:
    

newfile = open('cities (1).txt', 'r')
x = 0
for d in newfile:
    #if city in i:
    

    myinfo = d.strip().split('\t')
    
    latLocation = myinfo[1].split('°')
    #print (latLocation)

    if (x > 0):
        if (latLocation[1].find('S') == False):
            latN = latLocation[1].find('N')
            print (latN)
    x = x + 1















    
    #print(latLocation)
##    latLocationMin = latLocation[1].find('N' or 'S')
##    NS = latLocation[1][latLocationMin]
##
##    print (latLocationMin)
##    print (NS)
##    ##latLocationMin = latLocation[1][:latLocation[1].find('N' or 'S')]
##    ##print(latLocationMin)

    
