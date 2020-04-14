import cv2
from matplotlib import pyplot as plt

img  = cv2.imread("bye.jpg")
img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)


# for x,y,z in img[:]:
#     if (x==255 and y==255 and z==255):
#         if  
print(img.shape)
for i in range(1024):
    for j in range(746):
        if (img[i,j,0] >= 250 and img[i,j,1] >= 250 and img[i,j,2] >= 250) or (215 <= img[i,j,0] <= 225 and 215 <= img[i,j,1] <= 225 and 215 <= img[i,j,2] <= 225):
            img[i,j,0] = 33
            img[i,j,1] = 33
            img[i,j,2] = 33

for i in range(20):
    img = cv2.medianBlur(img,5)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imwrite("byeCorrected.jpg",img)
titles = ['images']
images = [img]
for i in range(1) :
    plt.subplot(1,1,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()