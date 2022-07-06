<h1 align="center"> TP4 </h1>
![UDESA LOGO](https://user-images.githubusercontent.com/101142182/177570532-6c64a0f6-4c89-4ffd-a214-95629d620ab9.png)
## Uses
In the repository there are 3 instruments as example to use in the synthesizer in the directory 'synthesizer\instruments'.
To use the module synthesizer one must first have their music sheet and instrument ready in their own repo. The following code will show how to use the synthesizer. The first thing to do is to create a file.py to run in your console:

```
import syntheziser.main

if __name__ == "__main__":
    syntheziser.main.main()
```
After creating and importing these dependencies, open the terminal and run the lines below. It is important to put the python command before running your file.
```
python file.py -f (frequency) -i (instrument.txt) -p (music_sheet.txt) -o (file.wav)
```

The *frequency* parameter will define the sampling frequency. The *instrument.txt* file refers to the file containing the configuration of the instrument, including its harmonics and fundamentals used to build the soundwave of each note reproduced. The *music_sheet.txt* file refers to the sheet containing all notes, their starting time and duration. The *file.wav* refers to the output wave file that will reproduce the song.
### Example *instrument.txt*:
```
8
1 0.577501
2 0.577501
3 0.063525
4 0.127050
5 0.103950
6 0.011550
7 0.011550
8 0.011550
TRI 0.05 0.03 1.3
CONSTANT
INVLINEAR .02
```

### Example *music_sheet.txt*:
```
0 A4 1
1 Ab4 2
2 C4 4
4 D7 8
1 C3 20
```


The first number in *music_sheet.txt* refers to the starting time of the note, the second paramter is the note, and the second number in the right side of the note is its duration.




