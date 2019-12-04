import cv2
import numpy as np
img=cv2.imread("lena.PNG",cv2.IMREAD_COLOR)
row,cols=img.shape[:2]
M=cv2.getRotationMatrix2D((row/2,cols/2),45,0.5)
img1=cv2.warpAffine(img,M,(cols,row))
tran=np.array([[1,0,100],[0,1,-50]],dtype=np.float32)
img2=cv2.warpAffine(img1,tran,(cols,row))
output=np.hstack((img,img1,img2))
output=cv2.cvtColor(output,cv2.COLOR_BGR2RGB)

cv2.imshow('input',output)
