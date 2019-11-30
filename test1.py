import cv2
# img1 = cv2.imread('lena.png', cv2.IMREAD_UNCHANGED)
# cv2.imshow('rgb', img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

img2 = cv2.imread('lena.png', cv2.IMREAD_COLOR)
cv2.imshow('rgb', img2[:,:,:])
cv2.waitKey(0)
cv2.destroyAllWindows()