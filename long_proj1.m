function [long] = long_proj1(city)
            myfile = fopen('cities (1).txt', 'r'); 
%             header = fgetl(myfile); 
% 
%             frewind(myfile); 
            filedata = textscan (myfile, '%s%s%s%s%s', 'Delimiter', '\t', 'header', 1);
            longData = filedata{1, 2}{city};
            
            
            %%FIND WHAT THE OR IS
            locationLong = extractBefore(longData,('W'));
            locationDegLat = str2double(extractBefore(locationLong, '°')); 
            locationMinLat = str2double(extractAfter(locationLong, '°'));
            
            
%             disp (locationDegLat);
%             disp (locationMinLat);
            long = locationDegLat + (locationMinLat/60); 
end
