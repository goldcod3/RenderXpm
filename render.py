from utils.args import config_args
from utils.path import *
from utils.convert import *

RED = '\033[0;91m'
ENDC = '\033[0m'

def run_render():
    args = config_args()
    verify_path_dir(get_path('output'))
    content_dir = get_path('content')

    # Directory render
    if args.directory != None and args.file == None:
        if verify_dir(args.directory) == True:
            convert_directory(args.directory)
        else:
            print(RED+'[ERROR]'+ENDC+' Invalid Directory!')

    # File render
    if args.directory == None and args.file != None:
        target_path = args.file
        if verify_target(target_path) == True:
             convert_image(target_path)
        else:
            print(RED+'[ERROR]'+ENDC+' Invalid file!')

    # Convert files of content directory
    if args.directory == None and args.file == None:
        verify_path_dir(content_dir)
        convert_directory(content_dir)

if __name__ == '__main__':
    run_render()