% looking for a prop that's 10x6
d = 11;
p = 7;


% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
% prop libary
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
% This function will go through every file in the propData folder and turn
% it into a struct that can then be referenced.

% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
% Prefixes
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
% Geometry
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

% if it exists, the characters before the .txt will be "geom" or you can
% just search for "geom" in the file name

% in the geom file, the three columns of data are: r/R    c/R     beta
% so the first is radial station, the second is chord distribution, and the
% third is twist. These files should be read by ignoring the first line,
% creating a matrix of the read data, and then just taking the columns and
% assigning them to the struct.

%% finding files to read
% get a list of all the files in the directory
listing = dir;

% now go through that struct and add the files that end in ".txt" to a new
% listing

% loop through the file list, create a struct of files 

n = 0;
for i = 1:numel(listing)
    if( ~listing(i).isdir )
        if (~isempty(strfind(listing(i).name,'.txt')))

            n = n + 1;
            
            fStruct(n).name = listing(i).name;
            
            fStruct(n).pitch = 0;
            fStruct(n).dia = 0;
            [fStruct(n).dia , fStruct(n).pitch] = getPropPitchDia(listing(i).name);
            fStruct(n).mfg = getMfg(fStruct(n).name);
            if(~isempty(strfind(listing(i).name,'geom')))
                fStruct(n).type = 'geom';
            else
                fStruct(n).type = 'data';
            end
           
        end
        
    end
    
end

%% Compare found files to requested dimensions

for i = 1:numel(fStruct)
    
    if((fStruct(i).pitch == p) && (fStruct(i).dia == d))
       disp(structToPropName(fStruct(i))); 
    end
    
end















