import os
import cv2
import sys
import numpy as np
from PIL import Image
def getImageAndLabels(path):
    facesSamples=[]
    ids=[]
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    #检测人脸
    face_detector = cv2.CascadeClassifier('C:/Users/shupi/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')
    #遍历列表中的图片
    for imagePaths in imagePaths:
        #打开图片
        PIL_img=Image.open(imagePaths).convert('L')
        #将图片转换为数组
        img_numpy=np.array(PIL_img,'uint8')
        faces = face_detector.detectMultiScale(img_numpy)
        #获取每张图片的ID
        id = int(os.path.split(imagePaths)[1].split('.')[0])
        for x,y,w,h in faces:
            facesSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)
    return facesSamples,ids

if __name__ =='__main__':
    #图片路径
    path='./data/jm/'
    #获取图像数组和id标签数组
    faces,ids=getImageAndLabels(path)
    #获取循环对象
    recognizer=cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(faces,np.array(ids))
    #保存文件
    recognizer.write('trainer/trainer.yml')
