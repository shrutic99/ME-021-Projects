T = input('Enter the temperature in Fahrenheit: ');
minV = input('Enter a min wind speed: ');
maxV = input('Enter a max wind speed: ');
% 
minV = double(minV);
maxV = double(maxV);
% 

for k = minV:5:maxV
    WCF = 35.7 +(0.6*T)-(35.7*(k^0.16))+(0.43*T*(k^0.16));
    WCF = double(WCF);
    finalanswer = round(WCF,1);
    fprintf("The wind chill factor for a windspeed of %g m.p.h is: %g degrees F. \n", k, finalanswer);
end

