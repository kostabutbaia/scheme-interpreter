import sys
from reader.reader import FileReader

from errors.no_input_file import NoInputFileError

def main(*args):
    if len(args) == 0:
        raise NoInputFileError()
    filepath = args[0]

    FileReader(filepath).exec()

if __name__ == '__main__':
    main(*sys.argv[1:])