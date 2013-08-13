# -*- coding: utf-8 -*-
import sys

class SubsConverter():
    def read_file(self, fileName):
        fr = open(fileName, "r")
        lines = fr.readlines()
        fr.close()
        
        return lines
    
    def write_file(self, fileName, name_sep):
        fn = self.format_file_name(fileName, name_sep)   
        fw = open(fn, 'w')
    
        return fw
    
    def calculate_time_taken(self, subsTime):
        timeTaken = list()
        
        for i in range(len(subsTime)):
            hour   = subsTime[i][0:2]
            minute = subsTime[i][3:5]
            second = subsTime[i][6:12].replace(",", ".").replace(":", ".")
        
            timeTaken.append((int(hour))*3600 + (int(minute))*60 + float(second))
            
        return timeTaken
          
    def convert_time_taken(self, timeTaken, fps_org, fps_tar):           
        # formula to convert the time in second taken by
        # FPS = fps_org to FPS = fps_tar
        totalTime = list()
        for i in range(2):
            totalTime.append(float(timeTaken[i]) * fps_tar / fps_org)
        
        return totalTime
          
    def re_calculate_time_taken(self, timeTaken, add_sub, time):
        reTimeTaken = list()                    
        for i in range(len(timeTaken)):
            if add_sub == 'add': #['A', 'AD', 'ADD']
                reTimeTaken.append(float(timeTaken[i] + time))
            else:
                reTimeTaken.append(float(timeTaken[i] - time))
                if reTimeTaken[i] < 0:
                    print 'starting time of a subtitle should not be earlier than video!\n please correct the time or try adding time'
                    sys.exit()
                       
        return reTimeTaken
      
    def format_time(self, totalTime):
        formatSubsTime = list()
        hh = list()
        mm = list()
        ss = list()
        
        for i in range(len(totalTime)):                                                 
            hh.append(int(totalTime[i] / 3600))
            if hh[i] < 10:
                hh[i] = str('0' + str(hh[i]))
                                       
            mm.append(int((totalTime[i] % 3600) / 60))
            if mm[i] < 10:
                mm[i] = str('0' + str(mm[i]))
                                
            ss.append(format(((totalTime[i] % 3600) % 60), '.3f'))                    
            if ss[i] < 10:
                ss[i] = str('0' + str(ss[i]))
                                                
            formatSubsTime.append(str(hh[i]) + ':' + str(mm[i]) + ':' + str(ss[i]))
                                       
        return formatSubsTime
    
    def format_file_name(self, fileName, name_sep):

        lastDot = fileName.rfind('.')   #index number of last dot
        if str(name_sep).rfind("_") == -1:
            if lastDot == -1:               #means there is no dots in the file name
                newFileName = fileName + str('_fps_' + str(name_sep)) + '.srt'                    
            else:
                baseName = fileName[0: lastDot]
                ext = fileName[lastDot: len(fileName)]
                
                newFileName = baseName + str("_fps_" + str(name_sep)) + ext
        else:
            if lastDot == -1:               #means there is no dots in the file name
                newFileName = fileName + name_sep + '.srt'                    
            else:
                baseName = fileName[0: lastDot]
                ext = fileName[lastDot: len(fileName)]
                
                newFileName = baseName + name_sep + ext
                                            
        return newFileName                                
                  
    def convert_substitle(self, fileName, fps_org, fps_tar):
        # this function converts a subtitle file from original frequency to desired 
        # frequency, the frequency of video
        # fileName: the name of the subtitle file
        # fps_org: the frequency of the subtitle
        # fps_tar: the frequency you want to have
        
        fw = self.write_file(fileName, fps_tar) 
        lines = self.read_file(fileName)
        
        for line in lines:
            (str0) = line.split(" ")
            
            if len(str0) > 2 and str0[1] == '-->':
                subsTime = (str0[0], str0[2])
                                          
                totalTime = self.convert_time_taken(self.calculate_time_taken(subsTime), fps_org, fps_tar)
    
                formatTime = self.format_time(totalTime)
                                                                           
                str0 = formatTime[0] + ' -->' + ' ' + formatTime[1] + '\n'                                 
            else:
                str0 = line
                
            print str0                                              
            fw.write(str0)
        
        print "New file name: ", self.format_file_name(fileName, fps_tar)
    
    def set_time_dif(self, fileName, add_sub, time):
        # this function adds or subtract from the time of subtitle to set-up for videos.  
        # fileName: the name of the subtitle file
        # add_sub: option: type "add" for adding time or "sub" for subtract
        # time: time in second the set-up difference

        if add_sub.upper() in ['A', 'AD', 'ADD']:
            name_sep = '_+' + str(time) + '_Second'
        elif add_sub.upper() in ['S', 'SU', 'SUB']:
            name_sep = '_-' + str(time) + '_Second'
        else:
            print "You type '"'%s'"', please type '"'add'"' or '"'sub'"'" %add_sub
            sys.exit()
           
        fw = self.write_file(fileName, name_sep) 
        lines = self.read_file(fileName)
        
        for line in lines:
            (str0) = line.split(" ")
            
            if len(str0) > 2 and str0[1] == '-->':
                subsTime = (str0[0], str0[2])
                                          
                totalTime = self.re_calculate_time_taken(self.calculate_time_taken(subsTime), add_sub, time)
    
                formatTime = self.format_time(totalTime)
                                                                           
                str0 = formatTime[0] + ' -->' + ' ' + formatTime[1] + '\n'                              
            else:
                    str0 = line
                    
            print str0                                              
            fw.write(str0)
        
        print "New file name: ", self.format_file_name(fileName, name_sep)

