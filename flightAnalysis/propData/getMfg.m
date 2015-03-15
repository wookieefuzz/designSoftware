function output = getMfg(s)

% ance = Aeronaut
% apc29ff = APC 29 Free Flight
% apccf = APC Carbon Fiber
% apce = APC Electric
% apcsf = APC Slow Flyer
% apcsp = APC Sport
% grcp = Graupner CAM Prop
% grcsp = Graupner CAM Slim Prop
% grsn = Graupner Super Nylon
% gwsdd = GWS Direct Drive
% gwssf = GWS Slow Flyer
% kavfk = Kavon FK
% kyosho = Kyosho
% ma = Master Airscrew
% mae = Master Airscrew Electric
% magf = Master Airscrew G/F
% mas = Master Airscrew Scimitar
% rusp = Rev Up Special Prop Series
% zin = Zingali

if(~isempty(strfind(s,'ance')))
    name = 'Aeronaut';
elseif(~isempty(strfind(s,'apc29ff')))
    name = 'APC 29 Free Flight';
elseif(~isempty(strfind(s,'apccf')))
    name = 'APC Carbon Fiber';
elseif(~isempty(strfind(s,'apce')))
    name = 'APC Electric';
elseif(~isempty(strfind(s,'apcsf')))
    name = 'APC Slow Flyer';
elseif(~isempty(strfind(s,'apcsp')))
    name = 'APC Sport';
elseif(~isempty(strfind(s,'grcp')))
    name = 'Graupner CAM Sport';
elseif(~isempty(strfind(s,'grcsp')))
    name = 'Graupner CAM Slim Prop';
elseif(~isempty(strfind(s,'grsn')))
    name = 'Graupner Super Nylon';
elseif(~isempty(strfind(s,'gwsdd')))
    name = 'GWS Direct Drive';
elseif(~isempty(strfind(s,'gwssf')))
    name = 'GWS Slow Flyer';
elseif(~isempty(strfind(s,'kavfk')))
    name = 'Kavon FK';
elseif(~isempty(strfind(s,'kyosho')))
    name = 'Kyosho';
elseif(~isempty(strfind(s,'ma')))
    name = 'Master Airscrew';
elseif(~isempty(strfind(s,'mae')))
    name = 'Master Airscrew Electric';
elseif(~isempty(strfind(s,'magf')))
    name = 'Master Airscrew G/F';
elseif(~isempty(strfind(s,'mas')))
    name = 'Master Airscrew Scimitar';
elseif(~isempty(strfind(s,'rusp')))
    name = 'Rev Up Special Prop Series';
elseif(~isempty(strfind(s,'zin')))
    name = 'Zingali';
else
    name = 'no mfg';
end
    
    output = name;
    
    
    
    
    
    
    
    