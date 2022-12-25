import os

# get environment variable
# print(os.environ)    # a dictionary

# get current working directory
print("---------------------------------------------------")
print("File location using os.getcwd(): ", os.getcwd())
print(__file__)
print(os.path.realpath(__file__))
print(f"File location using __file__ variable: {os.path.realpath(os.path.dirname(__file__))}")

# change CWD
print("---------------------------------------------------")
print("current cwd = " + os.getcwd())
os.chdir('../')
print("after change, cwd =  " + os.getcwd())

# create directory
# 1. os.mkdir()
print("---------------------------------------------------")
directory = "geek"
os.chdir("./module")
parent_dir = os.getcwd() 
path = os.path.join(parent_dir, directory)
mode_path = 0o666
try:
    os.mkdir(path, mode_path)
except FileExistsError:
    pass
os.rmdir(path)

# 2. os.makedirs
os.makedirs(path, mode_path)

# create sub-dir
root_dir = os.getcwd()
sub_dir_name = 'c'
a_folder = os.path.join(root_dir, "a")      # create inter-level directory
b_folder = os.path.join(a_folder, "b")      # create inter-level directory
c_folder = os.path.join(b_folder, sub_dir_name)

try:
    os.makedirs(c_folder, mode_path)
except FileExistsError:
    pass

os.rmdir(c_folder)  # delete c folder
os.rmdir(b_folder)   # delete b
os.rmdir(a_folder)        # delete a
os.rmdir(path)          # delete geek

# list out all of file and dir
current_dir = os.getcwd()
files = os.listdir(current_dir)
print(files)

file_name = "data.txt"
# create file
with open (file_name, "w") as fp:
    fp.write("create a some data")
    pass
# delete file
if file_name in files:
    os.remove(file_name)





# COMMON use function
print(os.name)  # name of operating system

# getsize, rename, remove, exist
with open (file_name, "w") as fp:
    fp.write("create a some data")
    pass

print(f"size of {file_name} = {os.path.getsize(file_name)} byte")

if(os.path.exists(file_name)):
    print(f"Create file {file_name}")
new_file_name = "new_name.txt"
try:
    os.rename(file_name, "new_name.txt")
    print(f"change name of {file_name} to {new_file_name}")
except FileExistsError:
    pass
os.remove(new_file_name)
print(f"remove {new_file_name}")