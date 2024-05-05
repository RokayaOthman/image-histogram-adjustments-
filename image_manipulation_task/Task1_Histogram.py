import cv2
import matplotlib.pyplot as plt

imgpath = r"D:\Documents\FEE\Sem_06\Digital_Image_Processing\image_manipulation_task\papsie-tiff.tiff"
img = cv2.imread(imgpath)

# showing the image before :

cv2.imshow('Image', img)
cv2.waitKey()

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Color Channels Histogram
red_hist = cv2.calcHist([img], [0], None, [256], [0, 255])
green_hist = cv2.calcHist([img], [1], None, [256], [0, 255])
blue_hist = cv2.calcHist([img], [2], None, [256], [0, 255])

hist_before = [red_hist, green_hist, blue_hist]

plt.subplot(4, 1, 1)
plt.imshow(img)
plt.title('image')
plt.xticks([])
plt.yticks([])

plt.subplot(4, 1, 2)
plt.plot(red_hist, color='r')
plt.xlim([0, 255])
plt.title('red histogram')

plt.subplot(4, 1, 3)
plt.plot(green_hist, color='g')
plt.xlim([4, 255])
plt.title('green histogram')

plt.subplot(4, 1, 4)
plt.plot(blue_hist, color='b')
plt.xlim([0, 255])
plt.title('blue histogram')

plt.tight_layout()
plt.show()

#--------------

# 2: increasing contrast, and leaving the brightness the same:

alpha = 1.7 #contrast control
beta = 0 #brightness control 

img2 = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

# showing the new image :
cv2.imshow('Image', img2)
cv2.waitKey()

#--------------

# 3: reducing the brightness:

alpha = 2
beta = -20

img2 = cv2.convertScaleAbs(img2, alpha=alpha, beta=beta)

cv2.imshow('Image', img2)
cv2.waitKey(0)

#--------------

#4: Showing the new histogram:
red_hist = cv2.calcHist([img2], [0], None, [256], [0, 255])
green_hist = cv2.calcHist([img2], [1], None, [256], [0, 255])
blue_hist = cv2.calcHist([img2], [2], None, [256], [0, 255])

hist_after = [red_hist, green_hist, blue_hist]
plt.subplot(4, 1, 1)
plt.imshow(img)
plt.title('image')
plt.xticks([])
plt.yticks([])

plt.subplot(4, 1, 2)
plt.plot(red_hist, color='r')
plt.xlim([0, 255])
plt.title('red histogram')

plt.subplot(4, 1, 3)
plt.plot(green_hist, color='g')
plt.xlim([4, 255])
plt.title('green histogram')

plt.subplot(4, 1, 4)
plt.plot(blue_hist, color='b')
plt.xlim([0, 255])
plt.title('blue histogram')

plt.tight_layout()
plt.show()
