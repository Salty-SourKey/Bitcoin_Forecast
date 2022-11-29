from sklearn import model_selection
from sklearn.model_selection import train_test_split
from PIL import Image
import os, glob
import numpy as np
import matplotlib.pyplot as plt


char_dir = "./chart_data/"
X = []  # 이미지 데이터
Y = []  # 레이블 데이터

files = glob.glob("./chart_data/*.png")
for index, file in enumerate(files):
    img = Image.open("./chart_data/chart_{0}.png".format(index))
    img = img.convert("RGB")
    img = img.resize((48,48))
    X.append(np.asarray(img).astype('float32')/255.0)

with open('chart_label.txt', 'r') as f:
    line = f.readline().rstrip()
    while line:
        label = (int)(line)
        Y.append(label)
        line = f.readline().rstrip()

X = np.array(X)
Y = np.array(Y)

X_train = X[:55989]
X_test = X[55989:]
y_train = Y[:55989]
y_test = Y[55989:]

xy = (X_train, X_test, y_train, y_test)
np.save("btc_chart.npy", xy)
print("ok, ", len(Y))