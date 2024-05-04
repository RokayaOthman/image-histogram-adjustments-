redhist = cv2.calcHist(img2, [0], None, 256, [0, 255])
greenhist = cv2.calcHist(img2, [1], None, 256, [0, 255])
bluehist = cv2.calcHist(img2, [2], None, 256, [0, 255])

plt.subplot(4, 2, 5)
plt.imshow(img2)
plt.title('Adjusted Image')
plt.xticks([])
plt.yticks([])

plt.subplot(4, 2, 6)
plt.plot(redhist, color='r')
plt.xlim([0, 255])
plt.title('Red Histogram (Adjusted)')

plt.subplot(4, 2, 7)
plt.plot(greenhist, color='g')
plt.xlim([0, 255])
plt.title('Green Histogram (Adjusted)')

plt.subplot(4, 2, 8)
plt.plot(bluehist, color='b')
plt.xlim([0, 255])
plt.title('Blue Histogram (Adjusted)')

plt.tight_layout()
plt.show()
