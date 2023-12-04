import os
import shutil
from tqdm import tqdm


if __name__ == '__main__':

    train_val_file_path = r'input/your_path'
    save_train_val_path = r'input/your_path'

    test_file_path = r'input/your_path'
    save_test_path = r'input/your_path'

    train_file = ""
    val_file = ""
    test_file = ""


    file_dirs = os.listdir(train_val_file_path)

    for i in tqdm(range(len(file_dirs))):
        file = file_dirs[i]
        file_name = os.path.splitext(file)[0]

        test_file += file_name + "\n"
        # save file
        f = open(save_train_val_path, 'w')
        f.write(test_file)
        f.close()

    test_file_dirs = os.listdir(test_file_path)

    for j in tqdm(range(len(file_dirs))):
        file = file_dirs[j]
        file_name = os.path.splitext(file)[0]

        test_file += file_name + "\n"
        # save file
        f = open(save_test_path, 'w')
        f.write(test_file)
        f.close()