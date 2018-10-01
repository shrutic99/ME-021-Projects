% clear all
% clc
% 
% input_city = 'Caracas'; 
% 
% file = fopen('cities.txt','r');
% data = textscan(file,'%s%s%s%s%s','Delimiter','\t','Headerlines',1);
% 
% % 
% 
% data = data{3}; 
% disp(data); 
% disp(city_data); 

% % str1 = 'ABC';
% % str2 = 'abc';
% % 
% % a = strcmp(str1,str2);
% % 
% % if a=1:
% %     disp('not case sensitive')
% % else
% %     disp('case sensitive')
% % end

s1 = 'and';
s2 = 'the and';
g = strcmp(s1,s2); 

if g == 0
    fprintf('this sucks \n');
else
    fprintf('it worked \n'); 
end
    
% a = strcmp (city_data, input_city); 
% 
% % fclose(file); 

