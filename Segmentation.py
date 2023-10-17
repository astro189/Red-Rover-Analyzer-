from skimage.io import imread, imshow
from skimage.color import label2rgb
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
import Background_Removal as BR


#Thresholding image
def Binarize(img):
    img=cv.cvtColor(img,cv.COLOR_BGR2RGB)

    gray=cv.cvtColor(img,cv.COLOR_RGB2GRAY)
    _,thresh=cv.threshold(gray,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    return thresh

#Applying morphological transformations
def morphological_operations(thresh):
    kernel=np.ones((2,2),np.uint8)
    opening=cv.morphologyEx(thresh,cv.MORPH_OPEN,kernel,iterations=1)

    #Close the openings
    morphed_img=cv.dilate(thresh,kernel,iterations=12)

    return morphed_img

#Segmenting using watershed
def WaterShed(morphed_img,img):
    #Perform Distance transform
    distance=cv.distanceTransform(morphed_img,cv.DIST_L2,3)

    #Remove side of box touching sand
    _,roi=cv.threshold(distance,0.2*distance.max(),255,0)
    roi=np.uint8(roi)

    _,marker=cv.connectedComponents(roi)
    marker+=10
    labels=cv.watershed(img,marker)

    return labels

#Applying segmentation to the original Image
def Segment_img(img,labels):
    img[labels==-1]=[0,255,0]
    img2=label2rgb(labels,bg_label=0)

    mask = np.zeros((img.shape[0],img.shape[1]), dtype="uint8")

    labels=np.array(labels)
    unique, counts = np.unique(labels, return_counts=True)
    pairs=dict(zip(unique,counts))

    values=list(pairs.values())

    value=sorted(values,reverse=True)[1]
    required=0
    for k in pairs.keys():
        if pairs[k]==value:required=k

    for label in np.unique(labels):
      mask[labels==required]=255
    segmented=cv.bitwise_and(img,img,mask=mask)

    return mask,segmented

#Cropping the unnecessary background
def Crop_Roi(mask,segmented):
    x,y,w,h=cv.boundingRect(mask)
    roi = segmented[y:y+h, x:x+w]
    zoomed_roi = cv.resize(roi, None, fx=2, fy=2, interpolation=cv.INTER_LINEAR)
    zoomed_roi=cv.cvtColor(zoomed_roi,cv.COLOR_RGB2BGR)
    return zoomed_roi

#Execute the whole program
def Excecute_Segmentation(img):
    img=BR.Remove_background(img,ret=True)
    img=cv.cvtColor(img,cv.COLOR_RGB2BGR)
    binarized=Binarize(img)
    morphed=morphological_operations(binarized)
    labels=WaterShed(morphed,img)
    mask,segmented=Segment_img(img,labels)
    zoomed_roi=Crop_Roi(mask,segmented)

    return zoomed_roi



if __name__=="__main__":
    img=cv.imread(r'box3.jpg')
    zoomed_roi=Excecute_Segmentation(img)
    cv.imshow('cropped',zoomed_roi)
    cv.waitKey(0)