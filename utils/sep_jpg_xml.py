#-*- coding: utf-8 -*-
import json
import os
import shutil
from tqdm import tqdm

# file path
dir_path=r'input/your_path'

# xml and img dir path
xml_dir_path=r'input/your_path'
img_dir_path=r'input/your_path'

if __name__ == '__main__':

    sep_dirs=os.listdir(dir_path)

    for i in tqdm(range(len(sep_dirs))):
        sep_name=sep_dirs[i]

        xml_path=os.path.join(xml_dir_path, sep_name)
        img_path=os.path.join(img_dir_path, sep_name)

        sep_file_path = os.path.join(dir_path, sep_name)

        if(os.path.splitext(sep_name)[1] == '.xml'):
            shutil.copyfile(sep_file_path, xml_path)
        else:
            shutil.copyfile(sep_file_path, img_path)