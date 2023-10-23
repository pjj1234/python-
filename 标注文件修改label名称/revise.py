"""
使用python xml解析树解析xml文件，批量修改xml文件里object节点下name节点的text
"""


import xml.etree.ElementTree as ET
import os
path = r'E:\AircraftDetection\new_dataset\Annotations'    # xml文件夹路径
i = 0
filelist = os.listdir(path)    # 该文件夹下所有的文件（包括文件夹）
for xml_file in filelist:

    print(xml_file)
    if xml_file.endswith('.xml'):
        file_path = os.path.join(path, xml_file)  # 完整的文件路径
        tree = ET.parse(file_path)    # 解析xml文件
        root = tree.getroot()    # 获取根节点
        obj_list = root.findall('object')  # 找到根节点下所有的object节点
        for per_obj in obj_list:

            if per_obj[0].text == 'Burning Black':    # 错误的标签“33”
                per_obj[0].text = 'Burning black'    # 修改成“44”
                print(xml_file, '修改完成')
                i = i+1
        tree.write(file_path)    # 将改好的文件重新写入，会覆盖原文件
    else:
        continue
print('共完成了{}处替换'.format(i))
