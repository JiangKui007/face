# _*_ coding:utf-8 _*_
# __author__ = 'JiangKui'
# __date__ = '4/23/20 14:00'
import os
import face_recognition
import cv2

from 读取视频信息 import read_video_info, deal_result_dir

# 输入视频
video_path = "头像视频.mov"
video_abs_path, root, result_dir, video_name, ext = deal_result_dir(video_path)
length, fps, size = read_video_info(video_abs_path)
input_movie = cv2.VideoCapture(video_abs_path)

# 输出视频
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_movie = cv2.VideoWriter('output2.avi', fourcc, fps, size)  # fps和 size 应与源文件一致

# 初始化部分变量
face_locations = []
face_encodings = []
face_names = []
frame_number = 0

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
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Label the results
    for (top, right, bottom, left) in face_locations:
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        # cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
        # font = cv2.FONT_HERSHEY_DUPLEX

    # print("result/image1_"+str(frame_number)+".jpg")
    output_movie.write(frame)

    cv2.imwrite(f"{result_dir}/{video_name}_{frame_number}.jpg", frame)  # 保存图片
    print("Writing frame {} / {}".format(frame_number, length))

# All done!
input_movie.release()
output_movie.release()
cv2.destroyAllWindows()
