# RendersXpm

Program that transforms png images to xpm format.

<img src="https://media.giphy.com/media/GUA4ull0bS6p6Ztfi1/giphy-downsized-large.gif" width=400 heigth=400/>

To use the software we only have to execute the `render.py` once and a content directory and an output directory will be generated. The basic use of this is:
- Paste PNG images into the `content` directory.
- Execute the `render.py` script and it transforms all the images in the `content` directory and saves them in the `output` directory in XPM format.

There are other options when running the program:
- `-f` File: We can pass it the path of a PNG file and it will transform it to XPM and generate it in the output directory.
- `-d` Directory: We can pass it the path of a directory and it will transform the PNG images to XPM and generate them in the output directory.
- `-h` Displays the help message.

> IMPORTANT: The script is made to convert PNG images, if you try to convert another type of image, it will not work.

Examples of use:
```
python3 render.py

python3 render.py -f <file>

python3 render.py -d <directory>

python3 -h
```

This program has been created in collaboration with [JorgeVJ](https://github.com/JorgeVJ), I hope it can help you! Enjoy it!
