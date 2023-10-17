import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import cv2 as cv
import Segmentation as sg

#Loading model
def get_model():
    model = tf.keras.models.Sequential([
    
        # The first convolution
        tf.keras.layers.Conv2D(16, (3,3), activation='relu', input_shape=(220, 220, 3)),
        tf.keras.layers.MaxPooling2D(2, 2),
        # The second convolution
        tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2,2),
        # The third convolution
        tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2,2),
        # The fourth convolution
        tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2,2),
        # The fifth convolution
        tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2,2),
    
        # Flatten the results to feed into a dense layer
        tf.keras.layers.Flatten(),
        # 128 neuron in the fully-connected layer
        tf.keras.layers.Dense(128, activation='relu'),
        # 5 output neurons for 5 classes with the softmax activation
        tf.keras.layers.Dense(5, activation='softmax')
    ])

    return model

#Processing Input image
def process_image(img,display=False):
    img=sg.Excecute_Segmentation(img=img)
    if display:
        cv.imshow('img',img)
        cv.waitKey(0)
    img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    img=cv.resize(img,(220,220))
    img=img/255
    img=np.reshape(img,(1,220,220,3))
    img = tf.image.convert_image_dtype(img, dtype=tf.float32)

    return img

#Initializing model
model=get_model()
model.compile(loss='categorical_crossentropy',
              optimizer=tf.keras.optimizers.RMSprop(learning_rate=0.001),
              metrics=['acc'])

model.load_weights(r'C:\Users\Shirshak\Desktop\IIT Roorkee submit\Data\model_weights.h5')

img=cv.imread(r"C:\Users\Shirshak\Desktop\IIT Roorkee submit\Images\box3.jpg")
processed_image=process_image(img,display=True)


#Getting model prediction and storing in data file
output=np.argmax(model.predict(processed_image))

diction={
    0:'Black soil',
    1:'cinder soil',
    2:'Laterite soil',
    3:'peat soil',
    4:'yellow soil',
}

# model.save_weights('./checkpoints/roorkee_checkpoint')
val =diction[output]
f=open(r'C:\Users\Shirshak\Desktop\IIT Roorkee submit\Data\Data.txt','a')

f.write(f'Soil Type:{val}')

f.close()
