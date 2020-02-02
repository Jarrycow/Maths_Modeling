function [P,D]=min_Routie(G,i,j)
% % s为顶点1 t为顶点2 w为顶点3
% % function [P,D]=min_Routie(s,t,w,i,j)
% % G = graph(s,t,w); %生成了图
[P,D] = shortestpath(G,i,j);
myplot = plot(G, 'EdgeLabel', G.Edges.Weight, 'linewidth', 2);  %首先将图赋给一个变量
highlight(myplot, P, 'EdgeColor', 'r')

end