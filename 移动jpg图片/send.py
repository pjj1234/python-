'''
根据XML文件名，将对应的JPG图片移动到指定目录
'''
import os


# 指定源目录和目标目录

source_jpg_dir = r'E:\AircraftDetection\env_det\第一次标注\images'
target_jpg_dir = r'E:\AircraftDetection\env_det\没有秸秆图片及标注\images'


# 指定目录路径
directory = r'E:\AircraftDetection\env_det\没有秸秆图片及标注\annotations'

# 用于保存XML文件名的列表
xml_files = []

# 遍历指定目录
for root, dirs, files in os.walk(directory):
    for file in files:
        # 检查文件是否以.xml结尾
        if file.endswith('.xml'):
            # 将文件名添加到列表中
            file = file[:-3] + 'jpg'
            # print(file)
            xml_files.append(file)

# 打印XML文件名列表
# for file in xml_files:
#     print(file)


# 指定要转移的JPG图片名称
for each in xml_files:

    image_name = each

    # 在源目录中搜索指定的JPG图片
    for root, dirs, files in os.walk(source_jpg_dir):
        if image_name in files:
            # 找到图片后，获取其完整路径
            image_path = os.path.join(root, image_name)

            # 将图片移动到目标目录
            os.rename(image_path, os.path.join(target_jpg_dir, image_name))
            print('Moved:', image_name)
