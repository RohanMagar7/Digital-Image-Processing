import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('pratical/naruto.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gradient_sobely=cv2.Sobel(img,-1,0,1)
fig, axis = plt.subplots(2, 3, figsize=(10, 5)) 
#figsize is the size of the window 2 and 3 are the rows and columns respectively
axis[0,0].imshow(img)
axis[0,0].set_title('Original image')
axis[0,0].axis('off')
axis[0,2].imshow(gradient_sobely)
axis[0,2].set_title('sobel y image')
axis[0,2].axis('off')
plt.show()
cv2.waitKey()