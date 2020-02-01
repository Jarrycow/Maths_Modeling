% % function [x,y]=abs_linar(f,A,b,Aeq,beq,lb,ub)
% % f=[f,f]';
% % A=[A,-A];
% % b=b';
% % [x,y]=linprog(f,A,b,Aeq,beq,lb,ub);
% % x=x(1:size(x,2)/2)-x(size(x,2)/2+1,end)
% % 
% % end

% % % % % % % % % % % % % % % % % % % % % % % % % 
% % function [x,y]=abs_linar(f,A,b,Aeq,beq)
% % f=[f,f]';
% % A=[A,-A];
% % b=b';
% % [x,y]=linprog(f,A,b,Aeq,beq);
% % x=x(1:size(x,2)/2)-x(size(x,2)/2+1,end)
% % 
% % end
% % % % % % % % % % % % % % % % % % % % % % % % % 
function [x,y]=abs_linar(f,A,b)
f=[f,f]';
A=[A,-A];
b=b';
[x,y]=linprog(f,A,b,zeros(size(f),1));
x=x(1:size(x,2)/2)-x(size(x,2)/2+1,end);

end