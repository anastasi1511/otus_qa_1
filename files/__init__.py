import os.path
from os.path import abspath

FILES_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)


TXT_FILE_PATH = get_path(filename="example.txt")
CSV_FILE_PATH = get_path(filename="123.csv")
JSON_FILE_PATH = get_path(filename="example.json")
CSV2_FILE_PATH = get_path(filename="books.csv")
JSON2_FILE_PATH = get_path(filename="users.json")
XML_FILE_PATH = get_path(filename="books.xml")
JPEG_FILE_PATH = get_path(filename="example.jpeg")


