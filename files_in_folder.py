from os import walk
files_names=[]
path_files= []
for (dirpath, dirnames, filenames)  in walk('/home/bilel/ansible'):
    files_names = filenames
    for names in filenames:
     path = '/home/bilel/ansible/' + names
     path_files.append(path)


print(files_names)
print(path_files)


azeazeaz
