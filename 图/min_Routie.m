function [P,D]=min_Routie(G,i,j)
% % sΪ����1 tΪ����2 wΪ����3
% % function [P,D]=min_Routie(s,t,w,i,j)
% % G = graph(s,t,w); %������ͼ
[P,D] = shortestpath(G,i,j);
myplot = plot(G, 'EdgeLabel', G.Edges.Weight, 'linewidth', 2);  %���Ƚ�ͼ����һ������
highlight(myplot, P, 'EdgeColor', 'r')

end