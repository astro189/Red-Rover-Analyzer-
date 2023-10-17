import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras

import os
dir_black = os.path.join(r'C:\Users\Shirshak\Soil types/Black Soil')
dir_Cinder = os.path.join(r'C:\Users\Shirshak\Soil types/Cinder Soil')
dir_Laterite = os.path.join(r'C:\Users\Shirshak\Soil types/Laterite Soil')
dir_peat = os.path.join(r'C:\Users\Shirshak\Soil types/Peat Soil')
dir_yellow = os.path.join(r'C:\Users\Shirshak\Soil types/Yellow Soil')

image_size = 220
batch_size = 10


target_size = (image_size, image_size)
input_shape = (image_size, image_size, 3)


train_datagen = tf.keras.preprocessing.ImageDataGenerator(rescale=1/255)


train_generator = train_datagen.flow_from_directory(
        r'C:\Users\Shirshak\Soil types', 
        target_size=(200, 200),
        batch_size = batch_size,
        classes = [ 'Black Soil','Cinder Soil', 'Laterite Soil','Peat Soil','Yellow Soil'],
       class_mode='categorical')

# for image_batch, label_batch in train_generator:
#     break
#     image_batch.shape, label_batch.shape

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

from tensorflow.keras.optimizers import RMSprop, Adam

model.compile(loss='categorical_crossentropy',
              optimizer=Adam(learning_rate=0.001),
              metrics=['acc'])

total_sample = train_generator.n
n_epochs = 30

history = model.fit(
        train_generator, 
        steps_per_epoch = int(total_sample/batch_size),  
        epochs = n_epochs,
        verbose = 1)
import cv2 as cv
img=cv.imread(r"img1.jpg")

img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
img=cv.resize(img,(220,220))
img=img/255
img=np.reshape(img,(1,220,220,3))
img = tf.image.convert_image_dtype(img, dtype=tf.float32)

output=np.argmax(model.predict(img))

diction={
    0:'Black soil',
    1:'cinder soil',
    2:'Laterite soil',
    3:'peat soil',
    4:'yellow soil',
}

model.save_weights('./checkpoints/roorkee_checkpoint')
val =diction[output]
f=open('Data.txt','a')

f.write(val)

f.close()


