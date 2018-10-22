% classdef city1
%     properties
%         lat
%         long
%         name
%     end
%     methods
        function [lat] = lat_proj1(city)
            myfile = fopen('cities (1).txt', 'r'); 
%             header = fgetl(myfile); 
% 
%             frewind(myfile); 
            filedata = textscan (myfile, '%s%s%s%s%s', 'Delimiter', '\t', 'header', 1);
            latData = filedata{1, 1}{city};
            
            
            %%FIND WHAT THE OR IS
            locationLat = extractBefore(latData,('N'));
            locationDegLat = str2double(extractBefore(locationLat, '°')); 
            locationMinLat = str2double(extractAfter(locationLat, '°'));
            
            
%             disp (locationDegLat);
%             disp (locationMinLat);
            lat = locationDegLat + (locationMinLat/60); 
           
        end
%     end
% end
%             
            