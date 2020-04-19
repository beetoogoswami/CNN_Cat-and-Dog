# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 01:06:31 2020

@author: PC
"""
import os

os.chdir("C:/Users/PC/Desktop/Image cat")

from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

datagen=ImageDataGenerator(rotation_range=40,width_shift_range=.2,height_shift_range=0.2,
                           zoom_range=0.2,horizontal_flip=True ,fill_mode='nearest' )

img=load_img('C:/Users/PC/Desktop/Image cat/10.jpg')

print(img)

x=img_to_array(img)

print(x)
x.shape

x=x.reshape((1,)+x.shape)

x.shape


i=0
for batch in datagen.flow(x,batch_size=1,save_to_dir='preview' , 
                      save_prefix='cat',save_format='jpg'):
    i+=1
    if i>20:
        break