

A = double(input('Input a radias for r(A): ')); 
thetaA = double(input('Input your angle in degreesfor A: ')); 
B = double(input('Input a radias for r(B): ')); 
thetaB = double(input('Input your angle in degrees for B: ')); 

% x = A*cos(thetaA); 
% y = B*cos(thetaB); 

theta1 = (pi/180)*thetaA;
theta2 = (pi/180)*thetaB; 

c = ((A^2)+(B^2)-(2*A*B)*cos(theta1-theta2))^(1/2); 

disp(c)