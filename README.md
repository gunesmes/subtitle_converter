subtitle_converter
==================

This can be used for converting subtitles. There are two main functionality which you can set the time differences by adding or subtracting seconds with the function set_time_dif() and you can change the frequency (FPS) of the subtitles with convert_substitle().

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
