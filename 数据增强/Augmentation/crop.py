import os
import shutil
from os.path import join
import cv2
import glob
from util import read_label_txt

root_dir = "./Images"
save_dir = "./bbox"

jpg_list = glob.glob(root_dir + "/*.jpg")


# fo = open("dpj_small.txt", "w")

max_s = -1
min_s = 1000

for jpg_path in jpg_list:
    txt_path = jpg_path.replace("jpg", "txt")
    jpg_name = os.path.basename(jpg_path)

    f = open(txt_path, "r")

    img = cv2.imread(jpg_path)

    height, width, channel = img.shape

    file_contents = f.readlines() # 读取全部内容 ，并以列表方式返回
    print(file_contents)


    for num, file_content in enumerate(file_contents):
        # print(num)
        clss, xc, yc, w, h = file_content.split()
        xc, yc, w, h = float(xc), float(yc), float(w), float(h)

        xc = xc * width
        yc = yc * height
        w = w * width
        h = h * height

        # max_s = max(w*h, max_s)
        # min_s = min(w*h, min_s)

        half_w, half_h = w // 2, h // 2

        x1, y1 = int(xc - half_w), int(yc - half_h)
        x2, y2 = int(xc + half_w), int(yc + half_h)

        crop_img = img[y1:y2, x1:x2]

        crop_width, crop_height, crop_channel = crop_img.shape
        new_jpg_name = jpg_name.split('.')[0] + "_crop_" + str(num) + ".jpg"
        if crop_height <= 400 and crop_width <= 400:
            cv2.imwrite(os.path.join(save_dir, new_jpg_name), crop_img)
            fo = open(os.path.join(save_dir, new_jpg_name.replace("jpg", "txt")), "w")
            cl = file_content.split(' ')[0]
            fo.write(cl)
            fo.close()
            # fo.write(os.path.join(save_dir, new_jpg_name)+"\n")
            # cv2.imshow("crop", crop_img)
            # cv2.waitKey(0)
            print('{}截取成功'.format(new_jpg_name))
        else:
            print('{}不符合要求'.format(new_jpg_name))

    print('===处理完成===')

    f.close()

# fo.close()

# print(max_s, min_s)
