
# (1) - import os

import os


# (2) - access the target directory

os.chdir('/Volumes/Seagate2T/PHOTOS/Photos-2009/10-Oct\ 09/0_Bday_Disneyland_Tokyo')


# (3) - check if the right dir is being called in

print(os.getcwd())


# (4) - split the file name from its extension

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)


# (5) - further split the file name into its components

    f_ek, f_do = file_name.split('_')
    

# (6) - create new file name format, assign using placeholders and check if it works

    new_file = ('2009_Nov_{}{}'.format(f_do, file_ext))
    print(new_file)
    

# (7) - confirm changes to all file names

    os.rename(f, new_file)
















