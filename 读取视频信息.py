# _*_ coding:utf-8 _*_
# __author__ = 'JiangKui'
# __date__ = '4/23/20 15:17'
import face_recognition
import cv2
import os


def read_video_info(video_path):
    assert video_path is not None, "video_path should given"

    input_movie = cv2.VideoCapture(video_path)
    length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(input_movie.get(cv2.CAP_PROP_FPS))
    width = int(input_movie.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(input_movie.get(cv2.CAP_PROP_FRAME_HEIGHT))
    size = (width, height)
    return length, fps, size


def deal_result_dir(file_path):
    # 获取视频的绝对路径, 文件名
    file_abs_path = os.path.abspath(file_path)
    root, file_name_ext = os.path.split(file_path)
    file_name, ext = file_name_ext.split('.')

    # 构造输出路径result_dir
    result_dir = os.path.join(root, file_name)
    if not os.path.exists(result_dir):
        os.mkdir(result_dir)

    return file_abs_path, root, result_dir, file_name, ext


if __name__ == '__main__':
    file_path = '头像视频.mov'
    file_abs_path, root, result_dir, file_name, ext = deal_result_dir(file_path)
    length, fps, size = read_video_info(file_abs_path)
    print(result_dir)
    print (length, fps, size)
    print (file_path, root, result_dir, file_name, ext)
