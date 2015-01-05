# -*- coding: utf-8 -*-
# Author Name: Mesut G�ne�
# Author Email: gunesmes@gmail.com
# Author Github username: gunesmes

from subConverter import SubsConverter
import os, sys, getopt


def converter(argv):
    try:
        optlist, args = getopt.getopt(sys.argv[1:], "options")
    except getopt.GetoptError, err:
      print err
      sys.exit(2)

    try:
        # function that will be used
        function = args[0]

        #set file_dir = "D:/..." the path of files to be converted
        #file_dir = "/Users/mesutgunes/Projects/subtitle_translator"
        file_dir = args[1]

        # set third and forth parameters
        arg3 = args[2]
        arg4 = args[3]
    except IndexError:
        print "Arguments Error! Please run the file with the following format:" 
        print "\n   python run.py 'path/to/files' 'max-length-of-lines' 'translator:google or yandex' 'source language' 'target language'\n   python run.py /Users/mesutgunes/Projects/subtitle_translator 40 google pl tr\n"
        sys.exit(2)

    #set path
    path = os.listdir(file_dir)

    #set directory
    os.chdir(file_dir)

    s = SubsConverter()

    srt = list()
    if len(srt) == 0:
        print "There is no .srt files. Check the directory!"
        
    for item in path:
        if item.rfind(".srt") != -1:
            srt.append(item)
            continue

    for i in range(len(srt)):
        # windows
        #subFile = os.path.dirname(os.path.abspath(srt[i])) +"\\" + srt[i]
        
        # unix based
        subFile = os.path.dirname(os.path.abspath(srt[i])) +"/" + srt[i]
        

        if function == "convert":
            # def convert_substitle(self, fileName, fps_org, fps_tar):
            # this function converts a subtitle file from original frequency to desired 
            # frequency, the frequency of video
            # fileName: the name of the subtitle file
            # fps_org: the frequency of the subtitle
            # fps_tar: the frequency you want to have  
            s.convert_substitle(subFile, float(arg3), float(arg4))

        elif function == "set":
            # def set_time_dif(self, fileName, add_sub, time):
            # this function adds or subtract from the time of subtitle to set-up for videos.  
            # fileName: the name of the subtitle file
            # add_sub: option: type "add" for adding time or "sub" for subtract
            # time: time in second the set-up difference
            s.set_time_dif(subFile, arg3, float(arg4))
        
        else:
            print "First parameter should be either 'convert' or 'set'"

if __name__ == "__main__":
   converter(sys.argv[1:])
