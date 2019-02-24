# -*- coding: utf-8 -*-
# Author Name: Mesut G�ne�
# Author Email: gunesmes@gmail.com
# Author Github username: gunesmes

from subConverter import SubsConverter
import os
import sys
import getopt
import platform


def convert_file(function, file, arg3, arg4):
    subtitle_converter = SubsConverter()

    try:
        if function == "convert":
            print("Processing: Converting frequency %f to %f for %s\n" %(float(arg3), float(arg4), file))
            # def convert_substitle(self, fileName, fps_org, fps_tar):
            # this function converts a subtitle file from original frequency to desired 
            # frequency, the frequency of video
            # fileName: the name of the subtitle file
            # fps_org: the frequency of the subtitle
            # fps_tar: the frequency you want to have  
            subtitle_converter.convert_substitle(file, float(arg3), float(arg4))

        elif function == "set":
            print("Processing: %s %f seconds for %s\n" %(arg3.replace("sub", "subtract"), float(arg4), file))
            # def set_time_dif(self, fileName, add_sub, time):
            # this function adds or subtract from the time of subtitle to set-up for videos.  
            # fileName: the name of the subtitle file
            # add_sub: option: type "add" for adding time or "sub" for subtract
            # time: time in second the set-up difference
            subtitle_converter.set_time_dif(file, arg3, float(arg4))
        
        else:
            print("First parameter should be either 'convert' or 'set'")
    except Exception as err:
        # try next file
        print(err)
        pass


def converter(argv):
    is_file = False

    try:
        optlist, args = getopt.getopt(sys.argv[1:], "options")
    except err:
      print(err)
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
        print("Arguments Error! Please run the file with the following format:")
        print("\n For folder which has multible .srt files:\n =========================================")
        print(" * Add/subtract seconds:\n  - python run.py set '/Users/mesutgunes/Projects/subtitle_converter' add 2.5\n  - python run.py set '/Users/mesutgunes/Projects/subtitle_converter' sub 2.5")
        print("\n * Convert the fps from 25 to 23.976:\n  - python run.py convert '/Users/mesutgunes/Projects/subtitle_converter' 25 23.976\n")
        print("\n For a single .srt file:\n =======================")
        print(" * Add/subtract seconds:\n  - python run.py set '/Users/mesutgunes/Projects/subtitle_converter/still-alice.srt' add 2.5\n  - python run.py set '/Users/mesutgunes/Projects/subtitle_converter' sub 2.5")
        print("\n * Convert the fps from 25 to 23.976:\n  - python run.py convert '/Users/mesutgunes/Projects/subtitle_converter/still-alice.srt' 25 23.976\n")
        sys.exit(2)

    # list of strs in the path
    srt = list()


    if(file_dir[-4:] == ".srt"):
        path = os.path.dirname(file_dir)
        os.chdir(path)        

        convert_file(function, file_dir, arg3, arg4)
    else:
        path = os.listdir(file_dir)
        os.chdir(file_dir)

        for item in path:
            if item.rfind(".srt") != -1:
                srt.append(item)
                continue
    
        if len(srt) == 0:
            print("There is no .srt files. Check the directory!")
            sys.exit(2)

        for i in range(len(srt)):
            if platform.version() == "Windows":
                file = os.path.dirname(os.path.abspath(srt[i])) +"\\" + srt[i]
            else:
                file = os.path.dirname(os.path.abspath(srt[i])) +"/" + srt[i]
            
            convert_file(function, file, arg3, arg4)

if __name__ == "__main__":
   converter(sys.argv[1:])
