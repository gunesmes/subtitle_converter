# -*- coding: utf-8 -*-
# Author Name: Mesut G�ne�
# Author Email: gunesmes@gmail.com
# Author Github username: gunesmes

from subConverter import SubsConverter
import os

#set file_dir = "D:/..." the path of files to be converted
file_dir = "D:/workspace/subtitle_converter/files/"
path = os.listdir(file_dir)

#set directory
os.chdir(file_dir)

s = SubsConverter()

srt = list()
for item in path:
    if item.rfind(".srt") != -1:
        srt.append(item)
        continue

for i in range(len(srt)):
    subFile = os.path.dirname(os.path.abspath(srt[i])) +"\\" + srt[i]
    
    """
    def convert_substitle(self, fileName, fps_org, fps_tar):
    this function converts a subtitle file from original frequency to desired 
    frequency, the frequency of video
    fileName: the name of the subtitle file
    fps_org: the frequency of the subtitle
    fps_tar: the frequency you want to have  
    """     
    s.convert_substitle(subFile, 25, 23.976)
    
    
    """
    def set_time_dif(self, fileName, add_sub, time):
    this function adds or subtract from the time of subtitle to set-up for videos.  
    fileName: the name of the subtitle file
    add_sub: option: type "add" for adding time or "sub" for subtract
    time: time in second the set-up difference
    """
    s.set_time_dif(subFile, 'add', 2.2)
