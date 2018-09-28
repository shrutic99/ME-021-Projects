##city = input('Enter the city you are looking for: ')
##
##newfile = open('cities.txt','r')
##
##data = []
##
##for row_num, line in enumerate (newfile):
##    values = line.strip().split('\t')
##
##    if row_num == 0:
##        data.append(values)
##    else:
##        thisrow = []
####        for v in values:
####            thisrow.append(v)
##        for i in values:
##            if city in i:
##                z = line.strip().split('\t')
##
####print(newfile.index(Caracas))
##
##print(data)
##
##newfile.close()
##
##
##
##
##
####result1 = print(city + mycoords)


##pancake = 'this is awesome'
##print(pancake.find('is a'))



        ##print (myinfo)
        ##print (mydegreesign)
        
##        mylong = myinfo[0:2] + ' degrees ' + myinfo[3:5] + ' minutes ' + myinfo[5]
##        mylat = myinfo[7:9]+ ' degrees ' + myinfo[10:12] + ' minutes ' + myinfo[12]
##        mycoords = city + ' is '+ mylong + ' and ' + mylat
##        print(mycoords)
##        print(myinfo)
##        data.append(myinfo)
##        print(len(myinfo))
##        print(data)
##        
##        print(len(myinfo))
    ## if city doesn't exits print "City not found!", then break the loop
##        if myinfo[] != city:

text = "Denver.dwg Group Layer\\Denver.dwg Annotation"
ext = ".dwg"
rip = "dwg"

fileNameOnly = text[:text.find(ext) + len(ext)]
print (fileNameOnly)
