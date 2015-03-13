function output = structToPropName(fs)

output = [fs.mfg ,'_' ,num2str(fs.dia) ,'x' ,num2str(fs.pitch),'-',fs.type];