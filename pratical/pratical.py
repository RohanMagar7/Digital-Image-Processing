# Image acquisition and representation

# import cv2
# img=cv2.imread('pratical/naruto.jpg',0)

# # Check if the image was successfully loaded
# if img is None:
#     print("Error: Could not read the image.")
# else:
#   cv2.imshow("Image",img)
#   cv2.waitKey(0)
#   cv2.destroyAllWindows()

# 2) Image compression and storage.
# import cv2
# img=cv2.imread('pratical/naruto.jpg',1)
# compressed_img_param=[cv2.IMWRITE_JPEG_QUALITY,80]
# cv2.imwrite('compressed_naruto.jpg',img,compressed_img_param)
# cv2.imshow("Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 3)mage Filtering and Restoration - Spatial domain filtering, Frequency domain filtering,
#Image denoising and restoration.
# import cv2
# import numpy as np
# img=cv2.imread('pratical/naruto.jpg',0)
# # Check if the image was successfully loaded
# if img is None:
#     print("Error: Could not read the image.")
# else:
#     # Apply Gaussian filter
#     img_gaussian=cv2.GaussianBlur(img,(5,5),0)
#     cv2.imshow("Gaussian Filter",img_gaussian)
#     cv2.imwrite('gaussian_naruto.jpg',img_gaussian)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

    
# import cv2
# import numpy as np
# img=cv2.imread("pratical/naruto.jpg",0)
# denoised=cv2.GaussianBlur(img,(5,5),0)
# cv2.imshow("original image",img)
# cv2.imshow("denoised image",denoised)
# cv2.imwrite("denoised_naruto.jpg",denoised)
# if(cv2.waitKey()==ord('q')):
#  cv2.destroyAllWindows()

#4) Convert bright image into dark image

# import cv2
# bright_image = cv2.imread("pratical/naruto.jpg")
# darkening_factor = 70
# dark_image = cv2.subtract(bright_image, darkening_factor)
# dark_image = cv2.max(dark_image, 0)
# cv2.imshow("Original image",bright_image)
# cv2.imshow("Dark Image", dark_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#5) Convert dark image into bright image.

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# dark_img = cv2.imread("pratical/naruto.jpg")
# brightening_factor = 50
# bright_img = np.clip(dark_img + brightening_factor, 0, 255).astype(np.uint8)
# plt.figure(figsize=(10, 6))
# plt.subplot(1, 2, 1)
# plt.imshow(cv2.cvtColor(dark_img, cv2.COLOR_BGR2RGB))
# plt.title("Original Dark Image")
# plt.subplot(1, 2, 2)
# plt.imshow(cv2.cvtColor(bright_img, cv2.COLOR_BGR2RGB))
# plt.title("Newly Brightened Image")
# plt.tight_layout()
# plt.show()
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #6) Take an image and apply Gaussian blur filer on it to sharp the image.
# import cv2
# import numpy as np
# img=cv2.imread("pratical/naruto.jpg")
# output_gaussian=cv2.GaussianBlur(img,(5,5),0,)
# cv2.imshow("gaussian blur",output_gaussian)
# cv2.imshow("original image",img)
# cv2.waitKey(0)

# #7) Take an image and apply Median blur filer on it

# import cv2
# import numpy as np
# img=cv2.imread("pratical/naruto.jpg")
# output_median_blur=cv2.medianBlur(img,5)
# cv2.imshow("median blur",output_median_blur)
# cv2.imshow("original image",img)
# cv2.waitKey(0)

# #8) Take an image and apply bilateral filter on it

# import cv2
# import numpy as np
# img=cv2.imread("pratical/naruto.jpg")
# output_biliteral=cv2.bilateralFilter(img,5,6,6)
# cv2.imshow("biliteral filter",output_biliteral)
# # #original image
# cv2.imshow("original image",img)
# cv2.waitKey(0)

# #9) Write a program to show only horizontal feature using sobel operator

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# img=cv2.imread('pratical/naruto.jpg')
# img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# gradient_sobely=cv2.Sobel(img,-1,0,1)
# fig, axis = plt.subplots(2, 3, figsize=(10, 5)) 
# #figsize is the size of the window 2 and 3 are the rows and columns respectively
# axis[0,0].imshow(img)
# axis[0,0].set_title('Original image')
# axis[0,0].axis('off')
# axis[0,2].imshow(gradient_sobely)
# axis[0,2].set_title('sobel y image')
# axis[0,2].axis('off')
# plt.show()
# cv2.waitKey()

#10) Write a program to show only vertical feature using sobel operator

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# img=cv2.imread('pratical/naruto.jpg')
# img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# gradient_sobelx=cv2.Sobel(img,-1,1,0)
# gradient_sobely=cv2.Sobel(img,-1,0,1)
# fig, axis = plt.subplots(2, 3, figsize=(10, 5))
# axis[0,0].imshow(img)
# axis[0,0].set_title('Original image')
# axis[0,0].axis('off')
# axis[0,1].imshow(gradient_sobelx)
# axis[0,1].set_title('sobel x image')
# axis[0,1].axis('off')
# axis[0,2].imshow(gradient_sobely)
# axis[0,2].set_title('sobel y image')
# axis[0,2].axis('off')
# plt.show()
# cv2.waitKey()

# #11) Write a program to apply laplacian filter on a image

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# img=cv2.imread('pratical/naruto.jpg')
# img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# gradient_laplacian=cv2.Laplacian(img,-1,)
# fig, axis = plt.subplots(2, 3, figsize=(10, 5))
# axis[0,0].imshow(img)
# axis[0,0].set_title('Original image')
# axis[0,0].axis('off')
# axis[1,1].imshow(gradient_laplacian)
# axis[1,1].set_title('laplacian image is ')
# axis[1,1].axis('off')
# plt.show()
# cv2.waitKey()

# #12) Write a program to draw a histogram of an image

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# def plot_histogram(img,title):
#   hist=cv2.calcHist([img],[0],None,[256],[0,255])
#   plt.plot(hist)
# bright=cv2.imread("pratical/naruto.jpg",0)
# dark=cv2.imread("pratical/denoised_naruto.jpg",0)
# plt.figure(figsize=(10,6))
# plt.subplot(2,2,1)
# plot_histogram(bright,"bright")
# plt.title("bright image histogram")
# plt.subplot(2,2,2)
# plot_histogram(dark,"dark")
# plt.title("dark image histogram")
# plt.tight_layout()
# plt.show()

#13) Write a program to apply thresholding on an image and show the thresholded output.
# import cv2
# image = cv2.imread('pratical/naruto.jpg', 0) # Load as grayscale (0)
# threshold_value = 127
# _, thresholded_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
# cv2.imshow('Original Image', image)
# cv2.imshow('Thresholded Image', thresholded_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#6) Image enhancement - Histogram equalization, Contrast stretching, Gamma correction.

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# img=cv2.imread("pratical/naruto.jpg",0)
# # Histogram equalization
# img_eq=cv2.equalizeHist(img)
# # Contrast stretching
# minmax_img=cv2.normalize(img,None,0,255,cv2.NORM_MINMAX)
# # Gamma correction
# gamma=2
# gamma_img=np.power(img/float(np.max(img)),gamma)
# gamma_img=np.uint8(255*gamma_img)
# plt.figure(figsize=(10,6))
# plt.subplot(2,2,1)
# plt.imshow(img,cmap='gray')
# plt.title("Original Image")
# plt.subplot(2,2,2)
# plt.imshow(img_eq,cmap='gray')
# plt.title("Histogram Equalized Image")
# plt.subplot(2,2,3)
# plt.imshow(minmax_img,cmap='gray')
# plt.title("Contrast Stretched Image")
# plt.subplot(2,2,4)
# plt.imshow(gamma_img,cmap='gray')
# plt.title("Gamma Corrected Image")
# plt.tight_layout()
# plt.show()
# cv2.waitKey(0)
# cv2.destroyAllWindows()

