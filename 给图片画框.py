# _*_ coding:utf-8 _*_
#__author__ = 'JiangKui'
#__date__ = '4/23/20 13:55'
import face_recognition
from skimage import draw, io
# %matplotlib inline
# 图片文件
files = "1587619702634.jpg"
# 加载图片
image = face_recognition.load_image_file(files)
# 识别人脸坐标
face_locations = face_recognition.face_locations(image)
# 我们在此使用之前介绍过的skimage库进行绘制
# 读出的图片在skimage中不能使用，故重新导入
img = io.imread(files)

print("I found {} face(s) in this photograph.".format(len(face_locations)))
# 循环标记人脸
for face_location in face_locations:
    # 每个人脸的坐标
    top, right, bottom, left = face_location
    # 为每个人脸画四边形
    # polygon_perimeter作用是绘制不填充的多边形
    rr, cc = draw.polygon_perimeter([top, top, bottom, bottom], [left, right, right, left])    # 设置颜色为红色
    draw.set_color(img, [rr, cc], [255, 0, 0])
    # 保存
    io.imsave(f'{files[:-4]}_boxed.png', img)
