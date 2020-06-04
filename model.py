#!/usr/bin/python
# -*- coding: utf-8 -*-
from keras.applications import VGG16
model = \
    VGG16(weights='/root/model/vgg16_weights_tf_dim_ordering_tf_kernels_notop.h5'
          , include_top=False, input_shape=(64, 64, 3))

model.layers[0].input
model.output
top_model = model.output

for l in model.layers:
    l.trainable = False

from keras.models import Sequential

from keras.layers import Dense, Flatten, Activation

top_model = Flatten()(top_model)
n1 = 256
n2 = 200
top_model = Dense(n1, activation='relu')(top_model)
# addlayerhere


top_model = Dense(n2, activation='relu')(top_model)
top_model = Dense(17, activation='softmax')(top_model)

from keras.models import Model

model.input

top_model

newmodel = Model(inputs=model.input, outputs=top_model)

from keras.preprocessing.image import ImageDataGenerator

train_data_dir = '/root/model/17_flowers/train/'
validation_data_dir = '/root/model/17_flowers/validation/'

train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest',
    )

validation_datagen = ImageDataGenerator(rescale=1./ 255)

# Change the batchsize according to your system RAM

train_batchsize = 16
val_batchsize = 10

train_generator = train_datagen.flow_from_directory(train_data_dir,
        target_size=(64, 64), batch_size=train_batchsize,
        class_mode='categorical')

validation_generator = \
    validation_datagen.flow_from_directory(validation_data_dir,
        target_size=(64, 64), batch_size=val_batchsize,
        class_mode='categorical', shuffle=False)

from keras.optimizers import RMSprop

newmodel.compile(loss='categorical_crossentropy',
                 optimizer=RMSprop(lr=0.001), metrics=['accuracy'])

nb_train_samples = 1190
nb_validation_samples = 170
epochs_x = 10
batch_size_x = 16

import sys
orig_stdout = sys.stdout
f = open('/root/model/output.txt', 'w')
sys.stdout = f

history = newmodel.fit_generator(train_generator,
                                 steps_per_epoch=nb_train_samples
                                 // batch_size_x, epochs=epochs_x,
                                 validation_data=validation_generator,
                                 validation_steps=nb_validation_samples
                                 // batch_size_x)
print(max(history.history['accuracy']))
print(max(history.history['val_accuracy']))

sys.stdout = orig_stdout
f.close()

# saving accuracy in the file

"""listoflines = list()
with open('/root/model/output.txt', 'r') as myfile:
    for line in myfile:
        listoflines.append(line.strip())

# converting list into string

model_history = listoflines[-1:]
str1 = ''
for element in model_history:
    str1 = element

# print(str1)

# converting string into float

accuracy = str1[80:87]
print(accuracy)
accuracy_f = float(accuracy)
val_accuracy = str1[122:129]
print(val_accuracy)
val_accuracy_f = float(val_accuracy)

# saving variable into seperate files

acc_file = open('/root/model/accuracy.txt', 'w')
acc_file.write('%f' % accuracy_f)
acc_file.close()

val_acc_file = open('/root/model/val_accuracy.txt', 'w')
val_acc_file.write('%f' % val_accuracy_f)
val_acc_file.close()
"""
accuracy_f = max(history.history['accuracy'])
print(accuracy_f)

val_accuracy_f = max(history.history['val_accuracy'])
print(val_accuracy_f)


# saving variable into seperate files

acc_file = open('/root/model/accuracy.txt', 'w')
acc_file.write('%f' % accuracy_f)
acc_file.close()

val_acc_file = open('/root/model/val_accuracy.txt', 'w')
val_acc_file.write('%f' % val_accuracy_f)
val_acc_file.close()
newmodel.save('vgg_newmodel.h5')
