import cv2

img=cv2.imread('lena.png')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow('input',img)


img_scale=cv2.rectangle(img,(60,40),(420,510),(0,0,255),4)
img_scale=cv2.resize(img_scale,None,fx=0.5,fy=0.5)
img_mir=img_scale[:,::-1,:]
img_mir=cv2.cvtColor(img_mir,cv2.COLOR_BGR2HSV)
img_mir[:,:,2]=cv2.equalizeHist(img_mir[:,:,2])
img_mir=cv2.cvtColor(img_mir,cv2.COLOR_rg)
cv2.imshow('output',img_mir)

cv2.waitKey(0)
cv2.destroyAllWindows()
