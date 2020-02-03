function [k,b]=linar_fit(x,y)
xlabel('x的值');
ylabel('y的值');
n = size(x,1);
k = (n*sum(x.*y)-sum(x)*sum(y))/(n*sum(x.*x)-sum(x)*sum(x));
b = (sum(x.*x)*sum(y)-sum(x)*sum(x.*y))/(n*sum(x.*x)-sum(x)*sum(x));
grid on % 显示网格线
xx=min(x)-0.5:0.1:max(x)+0.5;
yy=k*x+b;
plot(xx,yy,'-')
end
