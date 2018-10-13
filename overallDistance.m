%%The function to calculate my overall distance given my variables. 
function [distance] = overallDistance(A,B,thetaA,thetaB) 
distance = ((A^2)+(B^2)-(2*A*B)*cos(thetaA-thetaB))^(1/2);
end

