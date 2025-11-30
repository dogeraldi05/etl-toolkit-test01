import os
from contextlib import contextmanager


class SafeFileOpen:
    """
    Context Manager class para abrir arquivos de forma segura.
    """
    def __init__(self, filepath, mode="r", encoding="utf-8"):
        self.filepath = filepath
        self.mode = mode
        self.encoding = encoding
        self.file = None

    def __enter__(self):
        base_dir = os.path.dirname(os.path.dirname(__file__))  # volta da pasta src/
        full_path = os.path.join(base_dir, self.filepath)
        self.file = open(full_path, self.mode, encoding=self.encoding)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False


@contextmanager
def safe_file_open(filepath, mode="r", encoding="utf-8"):
    """
    Context Manager seguro para abrir arquivos usando @contextmanager.
    """
    base_dir = os.path.dirname(os.path.dirname(__file__))  # volta da pasta src/
    full_path = os.path.join(base_dir, filepath)

    file = None
    try:
        file = open(full_path, mode, encoding=encoding)
        yield file
    finally:
        if file:
            file.close()
