import glob
import sys
import shutil
import os
# usage
# python rename_2.py image_path target_path
file_path = sys.argv[1]
target_path = sys.argv[2]
if not os.path.exists(target_path):
        os.makedirs(target_path)
file_names = sorted(glob.glob(file_path+'/*.png'))
print file_names
i = 0
for file_name in file_names:
    file_name_parse = file_name.split('_')
    print file_name_parse
    newfile_name = target_path+'/b_'+file_name_parse[-2]+'_'+file_name_parse[-1]
    print newfile_name
    shutil.copy(file_name,newfile_name)
    i = i+1

