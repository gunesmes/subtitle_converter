Subtitle Converter
==================

This can be used for converting subtitles. There are two main functionality which you can set the time differences by adding or subtracting seconds with the function `set_time_dif()` and you can change the frequency (FPS) of the subtitles with `convert_substitle()`.

Make sure you have Python 2.7 or above installed
Check Python:
```shell
python --version
```

Clone the project:
```shell
git clone https://github.com/gunesmes/subtitle_converter.git
```
   
# To run the Subtitle Converter
* you must have a valid subtitle in .srt format

* run python file

```shell
python run.py <function> <path/to/files> <arg3> <arg4> 
```

 ## For folder which has multible .srt files:
 ### Add/subtract seconds:
 ```shell
 python run.py set '/Users/mesutgunes/Projects/subtitle_converter' add 2.5
 python run.py set '/Users/mesutgunes/Projects/subtitle_converter' sub 2.5
 ```

 ### Convert the fps from 25 to 23.976:
 ```shell
 python run.py convert '/Users/mesutgunes/Projects/subtitle_converter' 25 23.976
 ```

 ## For a single .srt file:
 ### Add/subtract seconds:
 ```shell
 python run.py set '/Users/mesutgunes/Projects/subtitle_converter/still-alice.srt' add 2.5
 python run.py set '/Users/mesutgunes/Projects/subtitle_converter' sub 2.5
 ```
 ### Convert the fps from 25 to 23.976:
 ```shell
 python run.py convert '/Users/mesutgunes/Projects/subtitle_converter/still-alice.srt' 25 23.976
  ````
