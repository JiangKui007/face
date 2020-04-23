# _*_ coding:utf-8 _*_
# __author__ = 'JiangKui'
# __date__ = '4/23/20 14:00'
import os
import face_recognition
import cv2

from 读取视频信息 import read_video_info, deal_result_dir
from core import make_box_loop

IMAGE_TAG = True

# 输入视频
video_path = "头像视频.mov"
video_abs_path, root, result_dir, video_name, ext = deal_result_dir(video_path)
length, fps, size = read_video_info(video_abs_path)
input_movie = cv2.VideoCapture(video_abs_path)

# 输出视频
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_movie = cv2.VideoWriter('output2.avi', fourcc, fps, size)  # fps和 size 应与源文件一致

input_movie,output_movie =  make_box_loop(video_path, input_movie ,output_movie, length, IMAGE_TAG)

# All done!
input_movie.release()
output_movie.release()
cv2.destroyAllWindows()
