from os.path import abspath, exists, isfile, isdir
from os import getcwd, mkdir

def verify_dir(path):
    if isdir(path) == True:
        return True
    else:
        return False

def verify_target(path):
    if isfile(path) == True and path.endswith('.png'):
        return True
    else:
        return False

def verify_target_xpm(target_path):
    if (exists(target_path) == True):
        return True
    else:
        return False

def verify_path_dir(path):
    try:
        while (exists(path) == False):
            mkdir(path)
        return True
    except:
        return False

def get_path(name_path):
    current_path = abspath(getcwd())
    return current_path + '/' + name_path

def get_name_image(target_path):
    img = target_path.split('/')[-1]
    name = img.split('.')[0]
    return name
