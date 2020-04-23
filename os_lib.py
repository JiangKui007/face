# _*_ coding:utf-8 _*_
# __author__ = 'JiangKui'
# __date__ = '4/23/20 17:07'
import os


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
