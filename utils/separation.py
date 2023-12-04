#-*- coding: utf-8 -*-
import json
import os
import shutil
from tqdm import tqdm

move_TrainVal_anno_path=r'input/your_path'
move_test_anno_path=r'input/your_path'

anno_dir_path=r'input/your_path'

if __name__ == '__main__':
    count = 0

    anno_dirs=os.listdir(anno_dir_path)

    dirs_len = len(anno_dirs)
    train = int(dirs_len * 0.9)

    for i in tqdm(range(dirs_len)):
        file_name = anno_dirs[i]

        origin_anno_path = os.path.join(anno_dir_path, file_name)

        if (i <= train):
            train_anno_path = os.path.join(move_TrainVal_anno_path, file_name)

            shutil.copyfile(origin_anno_path, train_anno_path)

        else:
            test_anno_path = os.path.join(move_test_anno_path, file_name)

            shutil.copyfile(origin_anno_path, test_anno_path)