clear all; 
clc

s1 = input('What state do you want to visit? ', 's'); 

myfile = fopen('cities (1).txt', 'r'); 
header = fgetl(myfile); 

frewind(myfile); 
filedata = textscan (myfile, '%s%s%s%s%s', 'Delimiter', '\t', 'header', 1);

%fprintf(filedata{1,1}{1});
%find cities in big list, keeps count of how many
%times you find one 
count = 0;
city = 0;
for x=1:length(filedata{1,4})
%     if (count ~= 1)
        if (strcmp(filedata{1,4}{x},s1))
            count = count + 1;
            city = x;
            for y=3
                %fprintf(filedata{1,y}{x});
                fprintf(filedata{1,y}{x});
                disp(' ');
                
%                 cityArray = zeros(1, count);
%                 cityArray(1,count) = filedata{1:y}{x};
%                 disp(cityArray);
%                 
%                 
                
            end
            disp(' '); 
            disp(lat_proj1(city));
            disp(long_proj1(city));
            
            
            %disp(distance(city));
        end
    
    %end
end
%populating array of cities 
for a=1:count
    
end


%call the NSorEW function here
%to determine if the state is NS or EW
%if it is EW oriented, sort by the long property 

%disp(count);
    

% s2 = filedata{4};
% a = strcmp(s1,s2); 
% 
% if a == 0
%     fprintf('State/Province not found! \n'); 
% else
%     first = filedata{1, 1}{a};
%     second = filedata{1, 2}{a};
%     third = filedata{1, 3}{a};
%     fourth = filedata{1, 4}{a};
%     fifth = filedata{1, 5}{a};
%     
%     blanklist = zeros(a,5);
%     
% end

