# _*_ coding:utf-8 _*_
# __author__ = 'JiangKui'
# __date__ = '4/23/20 16:43'
import cv2
import face_recognition

from os_lib import deal_result_dir


def make_box_loop(video_path, input_movie, output_movie, length, img_tag):
    # 初始化部分变量
    face_locations = []
    face_encodings = []
    face_names = []
    frame_number = 0
    video_abs_path, root, result_dir, video_name, _, ext = deal_result_dir(video_path)

    while True:
        # Grab a single frame of video
        ret, frame = input_movie.read()
        frame_number += 1

        # Quit when the input video file ends
        if not ret:
            break

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)

        # Label the results
        for (top, right, bottom, left) in face_locations:
            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        output_movie.write(frame)
        if img_tag == True:
            cv2.imwrite(f"{result_dir}/{video_name}_{frame_number}.jpg", frame)  # 保存图片
        print("Writing frame {} / {}".format(frame_number, length))

    return input_movie, output_movie
