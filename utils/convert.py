from PIL import Image
from sys import stdout, version_info
from os import listdir
from utils.xpm_image import pil_save
from utils.path import *

GREEN = '\033[0;92m'
YELLOW = '\033[0;93m'
RED = '\033[0;91m'
ENDC = '\033[0m'

def convert_image(target_path):
    name = get_name_image(target_path)
    img_xpm = name + '.xpm'
    target_xpm = get_path('output') + '/' + img_xpm
    if verify_target_xpm(target_xpm) == False:
        img = Image.open(target_path)
        xpm_bytes = pil_save(img)
        stdout = open(target_xpm, 'w')
        if version_info.major >= 3:
            stdout.buffer.write(xpm_bytes)
        else:
            stdout.write(xpm_bytes)
        print(f'{GREEN}[OK]{ENDC} The image is converted -> {target_xpm}')
    else:
        print(f'{YELLOW}[WARNING]{ENDC} The image exists in -> {target_xpm}')

def convert_directory(target_dir):
    if verify_dir(target_dir) == True:
        content = listdir(target_dir)
        if len(content) >= 1:
            for file in content:
                file = target_dir + '/' + file
                if verify_target(file) == True:
                    convert_image(file)
        else:
            print(RED+'[ERROR]'+ENDC+' Nothing to convert!')
    else:
        print(RED+'[ERROR]'+ENDC+'Invalid Directory!')
