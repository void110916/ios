import cv2
import time
import numpy as np
img=cv2.imread('lena.png',cv2.IMREAD_COLOR)
cv2.imshow('input',img)

img_hor=img[::-1,:,:]
cv2.imshow('horizenal change',img_hor)
img_ver=img[:,::-1,:]
cv2.imshow('vertical change',img_ver)

img_scale=cv2.resize(img,None,fx=0.2,fy=0.2)
start_t=time.time()
img_scale_out=cv2.resize(img_scale,None,fx=8,fy=8,interpolation=cv2.INTER_NEAREST)
print('nearest cost time{}'.format(time.time()-start_t))
cv2.imshow('nearest',img_scale_out)

img_scale=cv2.resize(img,None,fx=0.2,fy=0.2)
start_t=time.time()
img_scale_out=cv2.resize(img_scale,None,fx=8,fy=8,interpolation=cv2.INTER_CUBIC)
print('cubic cost time{}'.format(time.time()-start_t))
cv2.imshow('cubic',img_scale_out)

img_shift=img
M=np.array([[1.0,0,100],[0,1.0,50]])
img_shift=cv2.warpAffine(img,M,(img.shape[0],img.shape[1]))
cv2.imshow('shift',img_shift)

cv2.waitKey(0)
cv2.destroyAllWindows()