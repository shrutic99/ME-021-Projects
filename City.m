classdef City
    properties
        lat
        long
        name
    end
    methods
        function latDec(obj)
            myfile = fopen('cities (1).txt', 'r'); 
            header = fgetl(myfile); 
            filedata = textscan (myfile, '%s%s%s%s%s', 'Delimiter', '\t', 'header', 1);

            latData = zeros(1,5);
            latData(1,1) = filedata{1, 1};
            latData(1,2) = filedata{1, 2};
            latData(1,3) = filedata{1, 3};
            latData(1,4) = filedata{1, 4};
            latData(1,5) = filedata{1, 5};
            
            locationDegLat = str2double(longData(1,1), extractBefore('°')); 
            locationMinLat = str2double(longData(1,1), extractAfter('°'));
            
            obj.la = locationDegLat + (locationMinLat/60); 
           
            
        end
        function longDec(lon)
            myfile = fopen('cities.txt', 'r'); 
            header = fgetl(myfile); 
            filedata = textscan (myfile, '%s%s%s%s%s', 'Delimiter', '\t', 'header', 1);
            
            longData = zeros(1,5);
            longData(1,1) = filedata(2,1);
            longData(1,2) = filedata(2,2);
            longData(1,3) = filedata(2,3);
            longData(1,4) = filedata(2,4);
            longData(1,5) = filedata(2,5);
            
            locationDegLong = str2double(longData(1,2), extractBefore('°'));
            locationMinLong = str2double(longData(1,2), extractAfter('°')); 
            
            lon = locationDegLong + (locationMinLong/60);
        end
        
        function obj = City(la, lon, nam)
            obj.lat = latDec(la);
            obj.long = longDec(lon);
            obj.name = nam;
            
            obj.longDec()
            obj.latDec()
        end
        function printStuff(latDec(la), longDec(lon),nam)
            disp(obj.lat)
            disp(obj.long)
        end
    end
end