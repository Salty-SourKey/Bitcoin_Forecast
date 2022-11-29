import keras
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import Adam
from keras.utils import np_utils
import numpy as np


X_train, X_test, y_train, y_test = np.load("btc_chart.npy")

train_len = len(X_train)
batch_size = 16
num_epochs = 10

inputs = keras.Input(shape=(48,48,3))
x = inputs
x = Conv2D(32, 3, activation='relu', padding="same")(x)
x = Conv2D(32, 3, activation='relu', padding="same")(x)
x = MaxPooling2D(2)(x)
x = Conv2D(64, 3, activation='relu', padding="same")(x)
x = Conv2D(64, 3, activation='relu', padding="same")(x)
x = MaxPooling2D(2)(x)
x = Conv2D(128, 3, activation='relu', padding="same")(x)
x = Conv2D(128, 3, activation='relu', padding="same")(x)
x = MaxPooling2D(2)(x)
x = Conv2D(256, 3, activation='relu', padding="same")(x)
x = Conv2D(256, 3, activation='relu', padding="same")(x)
x = MaxPooling2D(2)(x)
x = Flatten()(x)
x = Dense(256)(x)
x = Dense(1, activation='sigmoid')(x)
outputs = x

model = keras.Model(inputs, outputs)

model.compile(loss='binary_crossentropy',
    optimizer='Adam',
    metrics=['accuracy'])

model.fit(X_train, y_train, batch_size=batch_size, epochs=num_epochs)

score=model.evaluate(X_test, y_test)
print('loss =',score[0])
print('accuracy=', score[1])