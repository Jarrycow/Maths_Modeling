%%%%%%%%%%%%%%%%%%%
%% min z = c'|x|;
%% A * x ¡Ü b
%%%%%%%%%%%%%%%%%%%
function [x,z] = Absolute_Value__Linear_Programming(c,A,b,aeq,beq)
[~,n]=size(c);
c = [c,c]';
A = [A,-A];
aeq=[aeq,-aeq];
[y,z] = linprog(c,A,b,aeq,beq,zeros(size(c)));
x=y(1:n)-y(n+1:end);
end