
##User Input
city = input('Enter the city you are looking for: ')

##Creating a variable for referencing cities.txt, and making it a read only file
newfile = open('cities.txt','r')
found = 0

##Creating a for loop for any i (city)
for i in newfile:
    
    ## if the city exists on the document, print it's longitude and latititude
    if city in i:
        myinfo = i.strip().split('\t')

        ## taking out the degree symbol 
        longlocation = myinfo[0].split('°')
        latlocation = myinfo[1].split('°')

        ## extracting number before north or south
        ## using the find function as a way to print the numbers until the function finds N, S, E, or W
        longitude = (longlocation[1][:longlocation[1].find('N'or 'S')])
        latitude = (latlocation[1][:latlocation[1].find('W' or 'E')])

        ## finds the location of N, S, E, and W
        dNS = longlocation[1].find('N' or 'S')
        dWE = latlocation[1].find('W' or 'E')

        ## takes the indexed location to print the specific index
        NS = longlocation[1][dNS]
        WE = latlocation[1][dWE]

        print (city + ' is ' + longlocation[0] + ' degrees ' + longitude + ' minutes ' + NS + ' and '+ latlocation[0] + ' degrees ' + latitude + ' minutes ' + WE)
        found = 1
        break
    
## if i is not in cities.txt
if found is 0:
    print('City not found!')
    
##Closing file after use
newfile.close()

