import cv2 as cv
img = cv.imread('leaf.jpg')
cv.imshow('img',img)
print('原来图片的形状：',img)

resize_img = cv.resize(img,dsize = (400,470))
print('修改后图片的形状：',resize_img.shape)
cv.imshow('resize_img',resize_img)

#只有输入q时退出
while True:
    if ord('q') == cv.waitKey(0):
        break

cv.destroyAllWindows()