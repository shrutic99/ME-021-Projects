clear all;
clc
%%User Input
s2 = input('Choose a city of your choice: ', 's');
%%city = 'Caracas'; 
myfile = fopen('cities.txt', 'r'); 
header = fgetl(myfile); 

%%I need to get back to the beginning of the file
frewind(myfile); 
filedata = textscan (myfile, '%s%s%s%s%s', 'Delimiter', '\t', 'header', 1);

%%string compares the city in filedata and the input
s1 = filedata{3};
a = strcmp(s1,s2); 

%%if the the input given does not have the city, then print "City not found"
if (a == 0)
    fprintf('City not found! \n');
else
%%the city exists    
    first = filedata{1, 1}{a};
    second = filedata{1, 2}{a};
    third = filedata{1, 3}{a};
    fourth = filedata{1, 4}{a};
    fifth = filedata{1, 5}{a};
%%extracting the longitude angle before the degree symbol
    locationbeforedegree = extractBefore(first,'°');
    locationbeforedegree = str2double(locationbeforedegree); 
%%locate the 'N' and 'S' on 'first'    
    longlocationN = strfind(first,'N');
    longlocationS = strfind(first,'S');

%%conditions for polar, temperate, and tropical
    if (locationbeforedegree > 66 && first(longlocationN) == 'N')
        fprintf('Polar \n');
    elseif (((locationbeforedegree > 35) && (locationbeforedegree < 66)) && first(longlocationN) == 'N')
        fprintf('Temperate \n')
    elseif (locationbeforedegree == 35)
        fprintf('Tropical \n')
    elseif (((locationbeforedegree > 35) && (locationbeforedegree < 66)) && first(longlocationS) == 'S')
        fprintf('Temperate \n')
    else %if (locationbeforedegree < 66 && first(longlocationS) == 'S')
        fprintf('Polar \n');
    end

end

fclose(myfile); 