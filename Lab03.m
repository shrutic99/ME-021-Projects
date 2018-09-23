%User Prompt
date = num2str(input('Enter the date in mmddyyyy: '));

%If the month is from 01-09, add a 0 in the front
%because input ignores first 0
bleh = '0';

if (length(date) == 7) 
    date = strcat(bleh, date);
end 

%extracts the different parts of the input 
month = date(1:2);
day = date(3:4);
year = date(5:8);

%month
monthNum = str2double(month);
monthStr = ' ';

switch monthNum
    case 1 
        monthStr = 'January';
    case 2 
        monthStr = 'February';
    case 3 
        monthStr = 'March';
    case 4 
        monthStr = 'April';
    case 5 
        monthStr = 'May';
    case 6 
        monthStr = 'June';
    case 7 
        monthStr = 'July';
    case 8 
        monthStr = 'August';
    case 9
        monthStr = 'September';
    case 10
        monthStr = 'October';
    case 11
        monthStr = 'November';
    case 12
        monthStr = 'December';
end 


%day suffixes
dayNum = str2double(day);
dayOrder = ' ';
st = 'st';
nd = 'nd';
rd = 'rd';
th = 'th';

%convert the day accordingly
%1st, 2nd, 3rd, and 4th must not include the 0 in front of 01,02,03 and 04
if (dayNum == 1) 
    dayOrder = strcat(num2str(dayNum), st);
elseif (dayNum == 2)
    dayOrder = strcat(num2str(dayNum), nd);
elseif (dayNum == 3)
    dayOrder = strcat(num2str(dayNum), rd);
elseif (dayNum > 3 && dayNum < 21)
    dayOrder = strcat(num2str(dayNum), th);
elseif (dayNum == 21)
    dayOrder = strcat(day, st);
elseif (dayNum == 22)
    dayOrder = strcat(day, nd);
elseif (dayNum == 23)
    dayOrder = strcat(day, rd);
elseif (dayNum > 23 && dayNum < 31)
    dayOrder = strcat(day, th);
elseif (dayNum == 31)
    dayOrder = strcat(day, st);
end

%convert year string to number
year = str2double(year);

%Output the final string
fprintf("The date is %s %s, %d. \n", monthStr, dayOrder, year);


