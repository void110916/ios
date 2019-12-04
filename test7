import cv2
import numpy as np
img=cv2.imread("lena.PNG")
p1=np.array([[60,40],[420,40],[420,150],[60,510]],dtype=np.float32)
p1_sh=np.array(p1,dtype=np.int32)
p1_sh=p1_sh.reshape((4,1,2))
p2=np.array([[0,80],[img.shape[1],120],[img.shape[1],430],[0,470]],dtype=np.float32)
p2_sh=np.array(p2,dtype=np.int32)
M=cv2.getPerspectiveTransform(p1,p2)
img1=cv2.warpPerspective(img,M,(img.shape[0],img.shape[1]))
img=cv2.polylines(img,[p1_sh],True,(0,255,0),3)
img1=cv2.polylines(img1,[p2_sh],True,(0,255,0),3)
output=np.hstack((img,img1))
output=cv2.cvtColor(output,cv2.COLOR_BGR2RGB)

cv2.imshow('input',output)

