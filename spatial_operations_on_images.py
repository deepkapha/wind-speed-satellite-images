# -*- coding: utf-8 -*-
"""spatial operations on images.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xgKP6tM8Ixc8eLzQN6KdeZJk7ssm2REH
"""

# from google.colab import drive
# drive.mount('/content/gdrive')

from google.colab import drive
drive.mount('/content/gdrive')

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/gdrive/My\ Drive/
# %cd nasa-data1

from pathlib import Path
import os

pth = Path("nasa-data1")
trn_imgs = pth/"train"
test_imgs = pth/"test"
for f in pth.iterdir():
    print(f)
print("Train images:", len(os.listdir(trn_imgs)))
print("Test images:", len(os.listdir(test_imgs)))

"""Here we are calling out for the dependencies

# FIRST WITH THE TRAINING SET
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
from PIL import Image
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

df = pd.read_csv("training_set_labels.csv")
df.head()

import matplotlib.pyplot as plt
import cv2
import numpy as np

# how to call in the whole dataset and iterate through it

#i1 = Image.open("train/abs_001.jpg")
#i2 = Image.open("train/abs_002.jpg")
#i3 = Image.open("train/abs_003.jpg")
#plt.imshow(image)
i1 = cv2.imread("train/abs_001.jpg")
i2 = cv2.imread("train/abs_002.jpg")
i3 = cv2.imread("train/abs_003.jpg")
plt.figure(figsize=(10,10))
plt.subplot(121)
plt.imshow(cv2.cvtColor(i1, cv2.COLOR_BGR2RGB))
plt.title("image 1")
plt.figure(figsize=(10,10))
plt.subplot(121)
plt.imshow(cv2.cvtColor(i2, cv2.COLOR_BGR2RGB))
plt.title("image 2")
plt.figure(figsize=(10,10))
plt.subplot(121)
plt.imshow(cv2.cvtColor(i3, cv2.COLOR_BGR2RGB))
plt.title("image 3")
plt.show()

"""showing the width, height and channels of the images"""

width_1, height_1,C_1=i1.shape
print('width, height,C',width_1, height_1,C_1)

width_1, height_1,C_1=i2.shape
print('width, height,C',width_1, height_1,C_1)

width_1, height_1,C_1=i3.shape
print('width, height,C',width_1, height_1,C_1)

"""Cropping and showing the difference between the images


"""

i1 = cv2.imread("train/abs_000.jpg")
i2 = cv2.imread("train/abs_006.jpg")
i3 = cv2.imread("train/abs_019.jpg")
i4 = cv2.imread("train/abs_034.jpg")
i5 = cv2.imread("train/abs_056.jpg")


plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(i1, cv2.COLOR_BGR2RGB))
plt.title("i1")
plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(i2, cv2.COLOR_BGR2RGB))
plt.title("i2")
plt.show()
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(i3, cv2.COLOR_BGR2RGB))
plt.title("i3")
plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(i4, cv2.COLOR_BGR2RGB))
plt.title("i4")
plt.show()

i1 = cv2.imread("train/abs_000.jpg")
i2 = cv2.imread("train/abs_006.jpg")
i3 = cv2.imread("train/abs_019.jpg")
i4 = cv2.imread("train/abs_034.jpg")
i5 = cv2.imread("train/abs_056.jpg")

upper = 150
lower = 300
left = 100
right = 280
crop_top = i1[upper: lower,:,:]
plt.figure(figsize=(10,10))
plt.imshow(cv2.cvtColor(crop_top, cv2.COLOR_BGR2RGB))
plt.show()

# for second image from the training set thats a bit different
upper = 70
lower = 300
left = 120
right = 380
crop_top = i2[upper: lower,:,:]
plt.figure(figsize=(10,10))
plt.imshow(cv2.cvtColor(crop_top, cv2.COLOR_BGR2RGB))
plt.show()

# for third image from the training set thats a bit different
upper = 42
lower = 300
left = 100
right = 380
crop_top = i3[upper: lower,:,:]
plt.figure(figsize=(10,10))
plt.imshow(cv2.cvtColor(crop_top, cv2.COLOR_BGR2RGB))
plt.show()

# for second image from the training set thats a bit different
upper = 20
lower = 200
left = 180
right = 380
crop_top = i4[upper: lower,:,:]
plt.figure(figsize=(10,10))
plt.imshow(cv2.cvtColor(crop_top, cv2.COLOR_BGR2RGB))
plt.show()

upper = 150
lower = 300
left = 100
right = 280
start_point, end_point = (left, upper),(right, lower)
image_draw = np.copy(i1)
cv2.rectangle(image_draw, pt1=start_point, pt2=end_point, color=(0, 255, 0), thickness=3) 
plt.figure(figsize=(5,5))
plt.imshow(cv2.cvtColor(image_draw, cv2.COLOR_BGR2RGB))
plt.show()

upper = 70
lower = 300
left = 120
right = 380
start_point, end_point = (left, upper),(right, lower)
image_draw = np.copy(i2)
cv2.rectangle(image_draw, pt1=start_point, pt2=end_point, color=(0, 255, 0), thickness=3) 
plt.figure(figsize=(5,5))
plt.imshow(cv2.cvtColor(image_draw, cv2.COLOR_BGR2RGB))
plt.show()

upper = 42
lower = 300
left = 100
right = 380
start_point, end_point = (left, upper),(right, lower)
image_draw = np.copy(i3)
cv2.rectangle(image_draw, pt1=start_point, pt2=end_point, color=(0, 255, 0), thickness=3) 
plt.figure(figsize=(5,5))
plt.imshow(cv2.cvtColor(image_draw, cv2.COLOR_BGR2RGB))
plt.show()

upper = 20
lower = 200
left = 180
right = 380
start_point, end_point = (left, upper),(right, lower)
image_draw = np.copy(i4)
cv2.rectangle(image_draw, pt1=start_point, pt2=end_point, color=(0, 255, 0), thickness=3) 
plt.figure(figsize=(5,5))
plt.imshow(cv2.cvtColor(image_draw, cv2.COLOR_BGR2RGB))
plt.show()

"""# Plotting the histograms and other graphs

We can plot it as a bar graph, the  𝑥
 -axis are the pixel intensities and the  𝑦
 -axis is the number of times of occurrences that the corresponding pixel intensity value on  𝑥
 -axis occurred.
"""

hist = cv2.calcHist([i1],[0], None, [80], [0,80])
intensity_values = np.array([x for x in range(hist.shape[0])])
plt.bar(intensity_values, hist[:,0], width = 5)
plt.title("Bar histogram for image 1")
plt.show()

hist = cv2.calcHist([i2],[0], None, [80], [0,80])
intensity_values = np.array([x for x in range(hist.shape[0])])
plt.bar(intensity_values, hist[:,0], width = 5)
plt.title("Bar histogram for image 2")
plt.show()

hist = cv2.calcHist([i3],[0], None, [80], [0,80])
intensity_values = np.array([x for x in range(hist.shape[0])])
plt.bar(intensity_values, hist[:,0], width = 5)
plt.title("Bar histogram for image 3")
plt.show()

hist = cv2.calcHist([i4],[0], None, [80], [0,80])
intensity_values = np.array([x for x in range(hist.shape[0])])
plt.bar(intensity_values, hist[:,0], width = 5)
plt.title("Bar histogram image 4")
plt.show()

"""The histogram is a function where  ℎ[𝑟]
  where  𝑟∈0,1,..,255
 .







We can convert it to a probability mass function by normalizing it by the number of pixels:
"""

#PMF = hist / (goldhill.shape[0] * goldhill.shape[1])
hist = cv2.calcHist([i1],[0], None, [80], [0,80])
plt.plot(intensity_values,hist)
plt.title("histogram 1")
plt.show()


hist = cv2.calcHist([i2],[0], None, [80], [0,80])
plt.plot(intensity_values,hist)
plt.title("histogram 2")
plt.show()


hist = cv2.calcHist([i3],[0], None, [80], [0,80])
plt.plot(intensity_values,hist)
plt.title("histogram 3")
plt.show()


hist = cv2.calcHist([i4],[0], None, [80], [0,80])
plt.plot(intensity_values,hist)
plt.title("histogram 4")
plt.show()

"""We can also apply a histogram to each image color channel:

In the loop, the value for i specifies what color channel calcHist is going to calculate the histogram for.

Intensity Transformations
It's helpful to think of an image as a function  𝑓(𝑥,𝑦)
  instead of an array at this point, where x is the row index and y is the column index. You can apply a transformation  𝑇
  to the image and get a new image:
𝑔(𝑥,𝑦)=𝑇(𝑓(𝑥,𝑦))
 
An Intensity Transformation depends on only one single point  (𝑥,𝑦)
 . For example, you can apply a linear transform  𝑔(𝑥,𝑦)=2𝑓(𝑥,𝑦)+1
 ; this will multiply each image pixel by two and add one.

As the Intensity transforms only depend on one value; as a result, it is sometimes referred to as a gray-level mapping. The variable if  𝑟
  is the gray level intensity, similar to the histogram values. The new output s is given by:

𝑠=𝑇(𝑟)

Image Negatives
Consider an image with  𝐿
  intensity values ranging from  [0,𝐿−1]
 . We can reverse the intensity levels by applying the following:
𝑔(𝑥,𝑦)=𝐿−1−𝑓(𝑥,𝑦)
 
Using the intensity transformation function notation
𝑠=𝐿−1−𝑟
 
This is called the image negative. For  𝐿=256
  the formulas simplifys to:
𝑔(𝑥,𝑦)=255−𝑓(𝑥,𝑦)and𝑠=255−𝑟
 






We can perform intensity transformation on the toy image where  𝐿=3
 :
"""

neg_i1 = -1 * i1 + 255

print("negative image\n", neg_i1)
print("image negatives\n", neg_i1)

neg_i1 = -1 * i1 + 255
plt.figure(figsize=(10,10))
plt.subplot(1, 2, 1) 
plt.imshow(i1,cmap="gray")
plt.subplot(1, 2, 2)
plt.imshow(neg_i1,cmap="gray")
plt.show()

neg_i2 = -1 * i2 + 255
plt.figure(figsize=(10,10))
plt.subplot(1, 2, 1) 
plt.imshow(i2,cmap="gray")
plt.subplot(1, 2, 2)
plt.imshow(neg_i2,cmap="gray")
plt.show()

neg_i3 = -1 * i3 + 255
plt.figure(figsize=(10,10))
plt.subplot(1, 2, 1) 
plt.imshow(i3,cmap="gray")
plt.subplot(1, 2, 2)
plt.imshow(neg_i3,cmap="gray")
plt.show()

neg_i4 = -1 * i4 + 255
plt.figure(figsize=(10,10))
plt.subplot(1, 2, 1) 
plt.imshow(i4,cmap="gray")
plt.subplot(1, 2, 2)
plt.imshow(neg_i4,cmap="gray")
plt.show()

"""Reversing image intensity has many applications, including making it simpler to analyze medical images. Consider the mammogram with micro-calcifications on the upper quadrant:

We can use multiplication by  𝛼
  for contrast control and addition by  𝛽
  to improve brightness control. This applies the Intensity Transformation as well. The image is  𝑓(𝑥,𝑦)
  and the transformed image is  𝑔(𝑥,𝑦)
 , where  𝑔(𝑥,𝑦)=𝛼𝑓(𝑥,𝑦)+𝛽
 .







Rather than implementing via array operations, we use the function convertScaleAbs. It scales, calculates absolute values, and converts the result to 8-bit so the values fall between  [0,255]
 . For brightness control, we can set  𝛼
  to 1 and  𝛽
  to 100: Remember the Good Hill image, it’s dark and hazy so let's see if we can improve it
"""

def plot_image(image_1, image_2,title_1="Orignal", title_2="New Image"):
    plt.figure(figsize=(10,10))
    plt.subplot(1, 2, 1)
    plt.imshow(image_1,cmap="gray")
    plt.title(title_1)
    plt.subplot(1, 2, 2)
    plt.imshow(image_2,cmap="gray")
    plt.title(title_2)
    plt.show()

"""# We can plot the brighter image, it's much brighter :

"""

alpha = 1 # Simple contrast control
beta = 100   # Simple brightness control   
new_image = cv2.convertScaleAbs(i1, alpha=alpha, beta=beta)
plot_image(i1, new_image, title_1 = "Orignal", title_2 = "brightness control")

alpha = 1 # Simple contrast control
beta = 100   # Simple brightness control   
new_image = cv2.convertScaleAbs(i2, alpha=alpha, beta=beta)
plot_image(i2, new_image, title_1 = "Orignal", title_2 = "brightness control")

alpha = 1 # Simple contrast control
beta = 100   # Simple brightness control   
new_image = cv2.convertScaleAbs(i3, alpha=alpha, beta=beta)
plot_image(i3, new_image, title_1 = "Orignal", title_2 = "brightness control")

alpha = 1 # Simple contrast control
beta = 100   # Simple brightness control   
new_image = cv2.convertScaleAbs(i4, alpha=alpha, beta=beta)
plot_image(i4, new_image, title_1 = "Orignal", title_2 = "brightness control")

"""# THRESHOLDING

HSV (Hue, Saturation and value)
"""

import cv2
from google.colab.patches import cv2_imshow
import numpy as np

cv2_imshow(i1)
ret, thresh1=cv2.threshold(i1,130,255,cv2.THRESH_BINARY)
print(thresh1.shape)
cv2_imshow(thresh1)

cv2_imshow(i2)
ret, thresh1=cv2.threshold(i2,130,255,cv2.THRESH_BINARY)
print(thresh1.shape)
cv2_imshow(thresh1)

cv2_imshow(i3)
ret, thresh1=cv2.threshold(i3,130,255,cv2.THRESH_BINARY)
print(thresh1.shape)
cv2_imshow(thresh1)

cv2_imshow(i4)
ret, thresh1=cv2.threshold(i4,130,255,cv2.THRESH_BINARY)
print(thresh1.shape)
cv2_imshow(thresh1)

cv2_imshow(i1)
ret, thresh1=cv2.threshold(i1,130,255,cv2.THRESH_BINARY)
print(thresh1.shape)
cv2_imshow(thresh1)

cv2_imshow(i2)
ret, thresh1=cv2.threshold(i2,130,255,cv2.THRESH_BINARY)
print(thresh1.shape)
cv2_imshow(thresh1)

cv2_imshow(i3)
ret, thresh1=cv2.threshold(i3,130,255,cv2.THRESH_BINARY)
print(thresh1.shape)
cv2_imshow(thresh1)

cv2_imshow(i4)
ret, thresh1=cv2.threshold(i4,130,255,cv2.THRESH_BINARY)
print(thresh1.shape)
cv2_imshow(thresh1)

"""in the next part we are sharpening the image showing the edges more statistically"""

# Common Kernel for image sharpening
kernel = np.array([[-1,-1,-1], 
                   [-1, 9,-1],
                   [-1,-1,-1]])
# Applys the sharpening filter using kernel on the original image without noise
sharpened = cv2.filter2D(i1, -1, kernel)
# Plots the sharpened image and the original image without noise
plot_image(sharpened , i1, title_1="Sharpened image",title_2="Image")

# Applys the sharpening filter using kernel on the original image without noise
sharpened = cv2.filter2D(i2, -1, kernel)
# Plots the sharpened image and the original image without noise
plot_image(sharpened , i2, title_1="Sharpened image",title_2="Image")

# Applys the sharpening filter using kernel on the original image without noise
sharpened = cv2.filter2D(i3, -1, kernel)
# Plots the sharpened image and the original image without noise
plot_image(sharpened , i3, title_1="Sharpened image",title_2="Image")

# Applys the sharpening filter using kernel on the original image without noise
sharpened = cv2.filter2D(i4, -1, kernel)
# Plots the sharpened image and the original image without noise
plot_image(sharpened , i4, title_1="Sharpened image",title_2="Image")

"""Edges are where pixel intensities change. The Gradient of a function outputs the rate of change; we can approximate the gradient of a grayscale image with convolution. There are several methods to approximate the gradient, let’s use the Sobel edge detector. This combines several convolutions and finding the magnitude of the result. Consider the following image:

"""

# Loads the image from the specified file
img_gray = cv2.imread('train/abs_000.jpg', cv2.IMREAD_GRAYSCALE)
print(img_gray)
# Renders the image from the array of data, notice how it is 2 diemensional instead of 3 diemensional because it has no color
plt.imshow(img_gray ,cmap='gray')

