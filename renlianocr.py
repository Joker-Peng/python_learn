import face_recognition
from PIL import Image, ImageDraw

# 加载图片并转换成RGB格式（face_recognition需要RGB格式）
img = face_recognition.load_image_file("test1_1.png")
img_rgb = face_recognition.load_image_file("test1_1.png", mode='RGB')

# 检测人脸位置
face_locations = face_recognition.face_locations(img_rgb)
print(face_locations)

# 在图片上绘制矩形框
pil_image = Image.fromarray(img)
draw = ImageDraw.Draw(pil_image)

for face_location in face_locations:
    top, right, bottom, left = face_location
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255), width=5)

# 显示结果
pil_image.show()