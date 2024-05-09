class NoInputFileError(Exception):
    def __init__(self):
        pass
    
    def __str__(self) -> str:
        return f'No input file specified, please run "python main.py <file_path>"'