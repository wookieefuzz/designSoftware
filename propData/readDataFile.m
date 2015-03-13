function [J ct cp eta] = readDataFile(f)

[A,delimiterOut,headerlinesOut] = importdata(f);
data = A.data;

J = data(:,1);
ct = data(:,2);
cp = data(:,3);
eta = data(:,4);
