# _*_ coding:utf-8 _*_
# __author__ = 'JiangKui'
# __date__ = '4/23/20 15:17'
import face_recognition
import cv2

from os_lib import deal_result_dir


def read_video_info(video_path):
    assert video_path is not None, "video_path should given"

    input_movie = cv2.VideoCapture(video_path)
    length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(input_movie.get(cv2.CAP_PROP_FPS))
    width = int(input_movie.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(input_movie.get(cv2.CAP_PROP_FRAME_HEIGHT))
    size = (width, height)
    return length, fps, size


if __name__ == '__main__':
    file_path = '头像视频.mov'
    file_abs_path, root, result_dir, file_name, ext = deal_result_dir(file_path)
    length, fps, size = read_video_info(file_abs_path)
    print(result_dir)
    print(length, fps, size)
    print(file_path, root, result_dir, file_name, ext)
