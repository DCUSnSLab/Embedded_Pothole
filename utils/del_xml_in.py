import os
import shutil

from lxml import etree
from tqdm import tqdm

# xml and img dir path
xml_dir_path = r'input/your_path'
img_dir_path = r'input/your_path'

# Arrival path
move_xml_path = r'input/your_path'
move_img_path = r'input/your_path'

if __name__ == '__main__':
    count = 0

    xml_dirs = os.listdir(xml_dir_path)

    for i in tqdm(range(len(xml_dirs))):

        xml_name = xml_dirs[i]
        xml_file_path = os.path.join(xml_dir_path, xml_name)

        tree = etree.parse(xml_file_path)
        root = tree.getroot()
        datas = root.getchildren()
        for d in datas:
            if d.tag == "filename":
                img_name = d.text
                img_file_path = os.path.join(img_dir_path, img_name)
                if os.path.isfile(img_file_path):
                    pass
                else:
                    move_xml = os.path.join(move_xml_path, xml_name)
                    shutil.move(xml_file_path, move_xml)
            # other tag check
            if d.tag == "object":
                obj_child = d.getchildren()
                for i in obj_child:
                    if i.tag == "name":
                        if i.text == "object":
                            if os.path.isfile(img_file_path):
                                count += 1
                        if count>=1:
                            move_img = os.path.join(move_img_path, img_name)
                            move_xml = os.path.join(move_xml_path, xml_name)

                            shutil.move(img_file_path, move_img)
                            shutil.move(xml_file_path, move_xml)
                            count=0
