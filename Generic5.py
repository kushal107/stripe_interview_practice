import pathlib

path_of_file = pathlib.Path('mytextfile.txt')
content_of_file = path_of_file.read_text()
print(content_of_file)