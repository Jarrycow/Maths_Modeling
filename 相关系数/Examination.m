function [RESULT,R]=Examination(Test)
MIN = min(Test);  % ÿһ�е���Сֵ
MAX = max(Test);   % ÿһ�е����ֵ
MEAN = mean(Test);  % ÿһ�еľ�ֵ
MEDIAN = median(Test);  %ÿһ�е���λ��
SKEWNESS = skewness(Test); %ÿһ�е�ƫ��
KURTOSIS = kurtosis(Test);  %ÿһ�еķ��
STD = std(Test);  % ÿһ�еı�׼��
RESULT = [MIN;MAX;MEAN;MEDIAN;SKEWNESS;KURTOSIS;STD];  %����Щͳ�����ŵ�һ���������б�ʾ
end

