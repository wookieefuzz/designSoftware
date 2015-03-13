function [Jout,etaout,ctout,cpout] = plotSeligPropData(mfg,dia,pitch,fs,ignoreMfg)

Jout = [];
etaout = [];
ctout = [];
cpout = [];

etaMax = 0;

n = 0;

for i = 1:numel(fs)
    
    % if you find a data file that matches....
    
    if(ignoreMfg == 1)
        
        if((fs(i).dia == dia) &&(fs(i).pitch == pitch) && (strcmp(fs(i).type,'data')) && isempty(strfind(fs(i).name,'static')))
            
            n = n+1;
            
            if(n == 1)
                figure
            end
            
            nameString = fullfile('propData',fs(i).name);
            
            [J , ct , cp , eta] = readDataFile(nameString);
            
            Jout = horzcat(Jout,J');
            etaout = horzcat(etaout,eta');
            cpout = horzcat(cpout,cp');
            ctout = horzcat(ctout,ct');
            
            if(max(eta)>etaMax)
                etaMax = max(eta);
                bestProp = [fs(i).mfg,' ',num2str(fs(i).dia),'x',num2str(fs(i).pitch)];
            end
            
            subplot(1,3,1)
            plot(J,ct)
            xlim([0 1])
            ylim([0 .2])
            if(n == 1)
                title('ct as function of J')
            end
            hold on
            subplot(1,3,2)
            plot(J,cp)
            xlim([0 1])
            ylim([0 .1])
            if(n == 1)
                title('cp as function of J')
            end
            hold on
            subplot(1,3,3)
            plot(J,eta)
            xlim([0 1])
            ylim([0 1])
            if(n == 1)
                title('eta as function of J')
            end
            hold on
            
            
        end
        
    else 
        
        if((strcmp(fs(i).mfg,mfg))&&(fs(i).dia == dia) &&(fs(i).pitch == pitch) && (strcmp(fs(i).type,'data')) && isempty(strfind(fs(i).name,'static')))
            
            n = n+1;
            
            if(n == 1)
                figure
            end
            
            nameString = fullfile('propData',fs(i).name);
            
            [J , ct , cp , eta] = readDataFile(nameString);
            
            Jout = horzcat(Jout,J');
            etaout = horzcat(etaout,eta');
            cpout = horzcat(cpout,cp');
            ctout = horzcat(ctout,ct');
            
            if(max(eta)>etaMax)
                etaMax = max(eta);
                bestProp = [fs(i).mfg,' ',num2str(fs(i).dia),'x',num2str(fs(i).pitch)];
            end
            
            subplot(1,3,1)
            plot(J,ct)
            xlim([0 1])
            ylim([0 .2])
            if(n == 1)
                title('ct as function of J')
            end
            hold on
            subplot(1,3,2)
            plot(J,cp)
            xlim([0 1])
            ylim([0 .1])
            if(n == 1)
                title('cp as function of J')
            end
            hold on
            subplot(1,3,3)
            plot(J,eta)
            xlim([0 1])
            ylim([0 1])
            if(n == 1)
                title('eta as function of J')
            end
            hold on
            
            
        end
        
        n = n+1;
        
        if(n == 1)
            figure
        end
        
        [J , ct , cp , eta] = readDataFile(fs(i).name);
        
        Jout = horzcat(Jout,J');
        etaout = horzcat(etaout,eta');
        cpout = horzcat(cpout,cp');
        ctout = horzcat(ctout,ct');
        
        if(max(eta)>etaMax)
            etaMax = max(eta);
            bestProp = [fs(i).mfg,' ',num2str(fs(i).dia),'x',num2str(fs(i).pitch)];
        end
        
        subplot(1,3,1)
        plot(J,ct)
        xlim([0 1])
        ylim([0 .2])
        if(n == 1)
            title('ct as function of J')
        end
        hold on
        subplot(1,3,2)
        plot(J,cp)
        xlim([0 1])
        ylim([0 .1])
        if(n == 1)
            title('cp as function of J')
        end
        hold on
        subplot(1,3,3)
        plot(J,eta)
        xlim([0 1])
        ylim([0 1])
        if(n == 1)
            title('eta as function of J')
        end
        hold on
        
        
    end
    
end




end


disp('best prop was a')
disp(bestProp)
disp('with a peak efficiency of')
disp(etaMax)

end

