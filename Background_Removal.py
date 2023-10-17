from skimage.io import imshow
from skimage.color import rgb2hsv
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

#convert from RGB to HSV
def RGB2HSV(img, display=False):
    hsv_img = rgb2hsv(img)
    if display:
        fig, ax = plt.subplots(1, 3, figsize=(20,20))
        ax[0].imshow(hsv_img[:,:,0], cmap='gray')
        ax[0].set_title('Hue')

        ax[1].imshow(hsv_img[:,:,1], cmap='gray')
        ax[1].set_title('Saturation')

        ax[2].imshow(hsv_img[:,:,2], cmap='gray')
        ax[2].set_title('Value')
    return hsv_img

#Display HSV image with colorbar for setting lower and upper bound on value
def Show_colorbar(hsv):
    fig, ax = plt.subplots(1, 3, figsize=(15, 5))
    ax[0].imshow(hsv[:,:,0],cmap='hsv')
    ax[0].set_title('hue')

    ax[1].imshow(hsv[:,:,1],cmap='hsv')
    ax[1].set_title('transparency')

    ax[2].imshow(hsv[:,:,2],cmap='hsv')
    ax[2].set_title('value')

    fig.colorbar(imshow(hsv[:,:,0],cmap='hsv'))
    fig.tight_layout()

#Generate masked image
def Generate_mask(img,hsv,lower_threshold,upper_threshold,saturation_threshold,display=False):
    #refer to hue channel (in the colorbar)
    lower_mask = hsv[:,:,0] > lower_threshold
    #refer to hue channel (in the colorbar)
    upper_mask = hsv[:,:,0] < upper_threshold
    #refer to transparency channel (in the colorbar)
    saturation_mask = hsv[:,:,1] >saturation_threshold

    mask = upper_mask*lower_mask*saturation_mask
    red = img[:,:,0]*mask
    green = img[:,:,1]*mask
    blue = img[:,:,2]*mask

    marker_masked = np.dstack((red,green,blue))

    if display:
        imshow(marker_masked)
    
    return marker_masked

#Execute the whole program
def Remove_background(img,ret=False):
    img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    hsv=RGB2HSV(img,display=False)

    section1=Generate_mask(img,hsv,lower_threshold=0.0,upper_threshold=0.12,saturation_threshold=0.1)
    section2=Generate_mask(img,hsv,lower_threshold=0.4,upper_threshold=0.8,saturation_threshold=0.2)
    masked=cv.bitwise_or(section1,section2)

    masked=cv.cvtColor(masked,cv.COLOR_RGB2BGR)
    section1=cv.cvtColor(section1,cv.COLOR_RGB2BGR)
    
    if ret:
        return section1
 

if __name__=='__main__':
    img=cv.imread(r"C:\Users\Shirshak\Desktop\IIT Roorkee submit\box3.jpg")
    Bgr_removed=Remove_background(img,ret=True)
    cv.imshow('img',Bgr_removed)
    cv.waitKey(0)