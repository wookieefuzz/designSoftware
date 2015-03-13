function [dia,pitch] = getPropPitchDia(s)

dia = 0;
pitch = 0;

% example string 'apce_8x4_2792rd_4001.txt'

% need to look for an "x" in between some underscores

% underscore locations
us = strfind(s,'_');


pd = s(us(1)+1 : us(2) - 1);

xloc = strfind(pd,'x');

dia = pd(1:xloc - 1);
pitch = pd(xloc + 1 : end);

pitch = str2num(pitch);
dia = str2num(dia);

