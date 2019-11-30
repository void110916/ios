# import cv2
# img = cv2.imread('lena.png',cv2.IMREAD_COLOR)
# cv2.imshow('imput',img)

# alfa=2.0
# beta=0.0
# img_HSV=img
# contrast=cv2.convertScaleAbs(img_HSV,alpha=2,beta=0)
# lightness=cv2.convertScaleAbs(img_HSV,alpha=1,beta=50)
# cv2.imshow("contrast",contrast)
# cv2.imshow('lightness',lightness)
# #img_HSV=cv2.cvtColor(img_HSV,cv2.COLOR_BGR2HSV)
# #img_HSV_out=img_HSV.astype('float32')
# #img_HSV_out[...,1]=img_HSV_out[...,1]/255*alfa+beta
# #img_HSV_out=img_HSV_out*255
# #img_HSV_out=img_HSV_out.astype('uint8')
# #img_HSV_out=cv2.cvtColor(img_HSV_out,cv2.COLOR_HSV2BGR)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

#img_bgr=img
#img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#for i in range (3):
#   img_bgr[...,i]=cv2.equalizeHist(img_bgr[...,i])
#cv2.imshow("case1_equalizeHist_BGR",img_bgr)
#img_hsv[...,2]=cv2.equalizeHist(img_hsv[...,2])
#img_out=cv2.cvtColor(img_hsv,cv2.COLOR_HSV2BGR)
#cv2.imshow("case2_equalizeHist_HSV",img_out)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


# # 改變飽和度
# # 增加
# img_hsv = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
# img_hsv_de=img_hsv.astype('float32')
# img_hsv_de[...,1] = img_hsv[...,1]/255 - 0.2
# img_hsv_de[img_hsv_de[..., 1] < 0] = 0 #如果將值改成255才會是白色
# img_hsv_de[...,1]=img_hsv_de[...,1]*255
# img_hsv_de=img_hsv_de.astype('uint8')
# img_out=cv2.cvtColor(img_hsv_de,cv2.COLOR_HSV2BGR)
# cv2.imshow('output_decrease',img_out)
# # 減少
# img_hsv_in=img_hsv.astype('float32')
# img_hsv_in[...,1] = img_hsv[...,1]/255 + 0.2
# img_hsv_in[img_hsv_in[..., 1] > 1] = 1
# img_hsv_in[...,1]=img_hsv_in[...,1]*255
# img_hsv_in=img_hsv_in.astype('uint8')
# img_out=cv2.cvtColor(img_hsv_in,cv2.COLOR_HSV2BGR)
# cv2.imshow('output_increase',img_out)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# import numpy as np
# img_path = 'lena.png'

# img_hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
# change_percentage = 0.2

# # 針對飽和度的值做改變，超過界線 0~1 的都會 bound
# # 在 HLS color space 減少飽和度
# img_hls_down = img_hls.astype('float32')
# img_hls_down[..., -1] = img_hls_down[..., -1]/255 - change_percentage
# img_hls_down[img_hls_down[..., -1] < 0] = 0
# img_hls_down[..., -1] = img_hls_down[..., -1]*255
# img_hls_down = img_hls_down.astype('uint8')

# # 在 HLS color space 增加飽和度
# img_hls_up = img_hls.astype('float32')
# img_hls_up[..., -1] = img_hls_up[..., -1]/255 + change_percentage
# img_hls_up[img_hls_up[..., -1] > 1] = 1
# img_hls_up[..., -1] = img_hls_up[..., -1]*255
# img_hls_up = img_hls_up.astype('uint8')

# # 轉換
# img_hls_down = cv2.cvtColor(img_hls_down, cv2.COLOR_HLS2BGR)
# img_hls_up = cv2.cvtColor(img_hls_up, cv2.COLOR_HLS2BGR)

# # 組合圖片 + 顯示圖片
# img_hls_change = np.hstack((img, img_hls_down, img_hls_up))
# while True:
#     cv2.imshow('change saturation', img_hls_change)
    
#     k = cv2.waitKey(0)
#     if k == 27:
#         cv2.destroyAllWindows()
#         break




# # 1.
# # decrease
# img_hsv=img
# img_hsv = cv2.cvtColor(img_hsv , cv2.COLOR_BGR2HSV)
# img_hsv_de=img_hsv.astype('float32')
# img_hsv_de[...,1] = img_hsv[...,1]/255 - 0.2
# img_hsv_de[img_hsv_de[..., 1] < 0] = 0
# img_hsv_de[...,1]=img_hsv_de[...,1]*255
# img_hsv_de=img_hsv_de.astype('uint8')
# img_out=cv2.cvtColor(img_hsv_de,cv2.COLOR_HSV2BGR)
# cv2.imshow('output_decrease',img_out)
# # increase
# img_hsv_in=img_hsv.astype('float32')
# img_hsv_in[...,1] = img_hsv[...,1]/255 + 0.2
# img_hsv_in[img_hsv_in[..., 1] > 1] = 1
# img_hsv_in[...,1]=img_hsv_in[...,1]*255
# img_hsv_in=img_hsv_in.astype('uint8')
# img_out=cv2.cvtColor(img_hsv_in,cv2.COLOR_HSV2BGR)
# cv2.imshow('output_increase',img_out)

import cv2
img = cv2.imread('lena.png',cv2.IMREAD_COLOR)
cv2.imshow('imput',img)
img_HSV=img
img_bgr=img
img_hsv=cv2.cvtColor(img_bgr,cv2.COLOR_BGR2HSV)

# alpha/ beta 調整對比 / 明亮
contrast=cv2.convertScaleAbs(img_HSV,alpha=2,beta=0)
lightness=cv2.convertScaleAbs(img_HSV,alpha=1,beta=50)
cv2.imshow("contrast",contrast)
cv2.imshow('lightness',lightness)    

#對 RGB 圖直接處理
for i in range (3):
    img_bgr[...,i]=cv2.equalizeHist(img_bgr[...,i])
cv2.imshow("case1_equalizeHist_BGR",img_bgr)
img_hsv[...,2]=cv2.equalizeHist(img_hsv[...,2])
img_out=cv2.cvtColor(img_hsv,cv2.COLOR_HSV2BGR)
cv2.imshow("case2_equalizeHist_HSV",img_out)


cv2.waitKey(0)
cv2.destroyAllWindows()