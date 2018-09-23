% User Input
t = input('Please enter the number of years for your investment: ');
P0 = input('Please enter the initial amount of money you want to invest: ');
% percentages given from the problem
r = 0.1;
f = 0.03;

%vertical array of my years
years = [t-4; t-3; t-2; t-1; t]; 
years = double(years);

%vertical array of the future value of the investment
F = zeros(5,1); 
F(1,1)= P0*((1+r)^(years(1,1))); 
F(2,1)= P0*((1+r)^(years(2,1)));
F(3,1)= P0*((1+r)^(years(3,1)));
F(4,1)= P0*((1+r)^(years(4,1)));
F(5,1)= P0*((1+r)^(years(5,1)));
F = round(F, 4,'significant');
disp(F)

%vertical array of the future value of the investment fund adjusted for inflation
G = zeros(5,1);
G(1,1) = F(1,1)*((1+f)^(-years(1,1)));
G(2,1) = F(2,1)*((1+f)^(-years(2,1)));
G(3,1) = F(3,1)*((1+f)^(-years(3,1)));
G(4,1) = F(4,1)*((1+f)^(-years(4,1)));
G(5,1) = F(5,1)*((1+f)^(-years(5,1)));
G = round(G,4,'significant'); 
disp(G)

%my print function where i is taking the columns of years, F, and G. 
for i = 1:i
   fprintf('At the end of year %g, your investment fund has $ %g, which is $ %g adjusted for inflation \n',years(i,1), F(i,1),G(i,1));
end

