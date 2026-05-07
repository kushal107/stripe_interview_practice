import pathlib

path_of_file = pathlib.Path('mytextfile2.txt')
new_content = 'Its a wonderful life\n'
new_content = new_content + 'yes it is a great life!'
path_of_file.write_text(new_content)
content_of_file = path_of_file.read_text()

print(content_of_file)
