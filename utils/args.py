import argparse

def config_args():
    parse = argparse.ArgumentParser(
        description="""*** Renders - PNG to XPM ***
        Tool to convert PNG images to XPM format.
        """
    )
    # Recursive download resources
    parse.add_argument("-d","--directory", default=None, help="[-d <dir_path>] Convert all files png of directory.")
    parse.add_argument("-f","--file", default=None, help="[-f <file_path>] Convert a file png to xpm.")
    return parse.parse_args()