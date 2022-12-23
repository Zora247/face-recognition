import cv2 as cv
img = cv.imread('George.jpg')
#左上角的坐标是x，y；矩形的宽度和高度是w，h
#x,y,w,h =50,50,30,30
#cv.rectangle(img,(x,y,x+w,y+h),color=(0,255,0),thickness=2)#BGR绘制矩形
#绘制圆,center为圆心坐标,radius为半径,thickness为线条宽度
x,y,r = 60,60,60
cv.circle(img,center=(x,y),radius=r,color=(0,255,0),thickness=(2))
#显示图片
cv.imshow('rectangle.img',img)
cv.waitKey(0)
cv.destroyAllWindows()