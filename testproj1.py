import math

class Location(object):
    def __init__(self, lat, long, city, state, country):
        self.lat = lat
        self.long = long
        self.city = city
        self.state = state
        self.country = country

        #initializing my methods
        self.convertLat()
        self.convertLong()
        self.locVacation()
        self.locDistMerced()

    def locDistMerced(self):
        self.latMerced = '37°22N'
        self.longMerced = '120°42W'

        #latitude of UCM
        latDM_Merced = self.latMerced.strip().split('°')
        ladD_Merced = int(latDM_Merced[0])
        latM_Merced = int(latDM_Merced[1][:latDM_Merced[1].find('N' or 'S')])
        latNS_Merced = (latDM_Merced[1][latDM_Merced[1].find('N' or 'S')])

        self.dL_Merced = ladD_Merced
        self.mL_Merced = latM_Merced/60
        self.degDec_Merced = self.dL_Merced + self.mL_Merced
        self.NS_Merced = latNS_Merced

        self.radsDecLat_Merced = math.radians(self.degDec_Merced)

        #longitude of UCM
        longDM_Merced = self.longMerced.strip().split('°')
        longD_Merced = int(longDM_Merced[0])
        longM_Merced = int(longDM_Merced[1][:longDM_Merced[1].find('W' or 'E')])
        longWE_Merced = (longDM_Merced[1][longDM_Merced[1].find('W' or 'E')])

        self.d_Merced = longD_Merced
        self.m_Merced = longM_Merced/60
        self.degLong_Merced = self.d_Merced + self.m_Merced
        self.WE_Merced = longWE_Merced

        self.radsDecLong_Merced = math.radians(self.degLong_Merced)

        #calculating distance
        d1NS = self.radsDecLat_Merced
        d2NS = self.radsDecLat
        c1WE = self.radsDecLong_Merced
        c2WE = self.radsDecLong
        R = 6360

        dNS = (math.sin((d2NS - d1NS)/2))**2
        d1 = math.cos(d1NS)
        d2 = math.cos(d2NS)

        dWE = (math.sin((c2WE - c1WE)/2))**2

        dsqrt = math.sqrt(dNS + (d1*d2*dWE))

        self.darcsin = math.asin(dsqrt)
        self.distance = 2*R*self.darcsin

    def convertLat(self):
        #converting any latitudes of cities(1).txt
        latDM = self.lat.strip().split('°')
        latD = int(latDM[0])
        latM = int(latDM[1][:latDM[1].find('N' or 'S')])
        latNS = (latDM[1][latDM[1].find('N' or 'S')])

        #so they can be initialized
        self.dL = latD
        self.mL = latM/60
        self.degDec = self.dL + self.mL
        self.NS = latNS
            
        self.radsDecLat = math.radians(self.degDec)

    def convertLong(self):
        #converting every longitude of cities(1).txt
        longDM = self.long.strip().split('°')
        longD = int(longDM[0])
        longM = int(longDM[1][:longDM[1].find('W' or 'E')])
        longWE = (longDM[1][longDM[1].find('W' or 'E')])

        #so they can be initialized
        self.d = longD
        self.m = longM/60
        self.degLong = self.d + self.m
        self.WE = longWE
        
        self.radsDecLong = math.radians(self.degLong)

        
    def printStuff(self):
##        print(self.lat)
##        print(self.long)
        print(self.city)
        print(self.state)
        print(self.country)
##        print(self.d)
##        print(self.m)
##        print(self.NS)
##        print(self.degDec)
##        print(self.radsDecLat)
##        print(self.radsDecLong)
##        print(self.Summer)
##        print(self.Winter)
##        print(self.radsDecLat_Merced)
##        print(self.radsDecLong_Merced)
##        print(self.darcsin)
##        print(self.distance)
        print(' ')


    def locVacation(self):
        #establishing winter, summer, warm, and cold
        if (self.degDec > 66 and self.NS == 'N'):
            self.Summer = 'Cold'
            self.Winter = 'Cold'
        elif (self.degDec > 35 and self.degDec < 66)and(self.NS == 'N'):
            self.Summer = 'Warm'
            self.Winter = 'Cold'
        elif (self.degDec < 35 and self.NS == 'N') or (self.degDec < 35 and self.NS == 'S'):
            self.Summer = 'Warm'
            self.Winter = 'Warm'
        elif (self.degDec > 35 and self.degDec < 66)and(self.NS == 'S'):
            self.Summer = 'Cold'
            self.Winter = 'Warm'
        elif (self.degDec > 66 and self.NS == 'S'):
            self.Summer = 'Cold'
            self.Winter = 'Cold'
        

def main():
    file = open('cities (1).txt','r')
    locList = []
    sortedList = []
    count = 0
    for b in file:
        info = b.strip().split('\t')
        lat = info[0]
        long = info[1]
        city = info[2]
        state = info[3]
        country = info[4]
        if (count > 0):
            locList.append(Location(lat, long, city, state, country))
        #locList[count].convert()
        
        count = count + 1

    #locList[1].printStuff()
    #locList[2].printStuff()


    #User Input
    sum1 = input('Winter or Summer: ')
    clim1 = input('Warm or Cold: ')


    #starting the count at 0, and creating lists after each count
    count = 0
    for x in locList:
        if sum1 == 'Winter':
            if locList[count].Winter == clim1:
                sortedList.append(locList[count])
        if sum1 == 'Summer':
            if locList[count].Summer == clim1:
                sortedList.append(locList[count])
        count += 1

    #sortedList[2].printStuff()
    sortedList.sort(key=lambda x: x.distance)

    #printing the first 5 cities
    for x in range(0, 5):
        sortedList[x].printStuff()


    file.close()
main()


