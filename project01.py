class Summer(object)
    def __init__(self, latitude, longitude, degrees):
        self.lat = lat
        self.long = long
        self.degrees = deg

    def degreesCalc (self):
        newfile = open('cities (1).txt','r')
        for database in newfile:
            myinfo = database.strip().split('\t')
            if holiday == 'Summer':
                latLocation = myinfo[0].split('°')
                latLocationMin = latLocation[1].split('N' or 'S')
                
            
    

    


def main():
    holiday = input('Summer or Winter: ')
    destTemp = input ('Cold or Warm: ')
    newfile = open ('cities.txt', 'r')
    

main()



newfile = open('cities.txt', 'r')

##for d in newfile:
##
##    firstline = True
##    for row in newfile:
##        if firstline:    #skip first line
##            firstline = False
##            continue
##        myinfo = d.strip().split('\t')
##        latLocation = myinfo[0].split('°')
##
##        if int(latLocation[0]) > 66:
##            print ('fuck my life')
##        else:
##            print ('i hope this works')
##
##    
