import cv2
import numpy as np
img=cv2.imread('lena.PNG')
img1=cv2.GaussianBlur(img,(17,17),0)

img2=cv2

output=np.hstack((img,img1))
output=cv2.cvtColor(output,cv2.COLOR_BGR2RGB)
cv2.imshow('output',output)