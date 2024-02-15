#------------------------------video 2
#import cv2
# img=cv2.imread('assets/hamkroun.png',1)
# img=cv2.resize(img,(800,800))
# img=cv2.resize(img,(0,0),fx=0.5,fy=0.75)
# img=cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
# cv2.imwrite('assets/new_img.png',img)
# cv2.imshow('imagee',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#------------------------------video 2
import cv2
import random
img=cv2.imread('assets/hamkroun.png',1)
        # print(img)
        # print(type(img))
        # print(img.shape)
        # for i in range(img.shape[0]):
        #     for j in range(img.shape[1]):
        #         img[i][j]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
tag=img[100:200,250:350]
img[50:150,250:350]=tag

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()        