import glob
import sys
import shutil
import os
# usage
# python rename.py image_path target_path
file_path = sys.argv[1]
target_path = sys.argv[2]
if not os.path.exists(target_path):
        os.makedirs(target_path)
file_names = sorted(glob.glob(file_path+'/*.png'))
print file_names
i = 0
for file_name in file_names:
    i_1 = i/1000
    i_2 = i%1000
    newfile_name = target_path+'/a_'+str(i_1).zfill(3)+'_'+str(i_2).zfill(3)+'.png'
    print newfile_name
    shutil.copy(file_name,newfile_name)
    i = i+1

