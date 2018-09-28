file = fopen('cities.txt','r'); 
data = textscan(file,'%s%s%s%s%s','Delimiter','\t','Headerlines',1);
city_data = data{3}; 

% str1 = 'ABC'
% str2 = 'abc'
% 
% a = strcmp(s1,s2)
% 
% if a=1
%     disp('not case sensitive')
% else
%     disp('case sensitive')
% end
input_city = 'San Diego'; 
a = strcmp (city_data, input_city); 

fclose(file); 

