%%User Input
A = double(input('Input a radias for r(A): ')); 
thetaA = double(input('Input your angle in degrees for A: ')); 
B = double(input('Input a radias for r(B): ')); 
thetaB = double(input('Input your angle in degrees for B: ')); 

%%Angle Conversion
thetaA = deg2rad_lab06 (thetaA);
thetaB = deg2rad_lab06 (thetaB); 

%%Calcualting the total distance between the 
x = overallDistance(A,B,thetaA,thetaB);
disp(x)