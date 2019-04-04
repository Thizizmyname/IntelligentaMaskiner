#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Intelligent and Interactive Systems 
Spring 2019
Lab 2: Software for Machine Learning 
"""

# Import data sets, classifiers and performance metrics
from __future__ import absolute_import, division, print_function, unicode_literals
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.decomposition import PCA
from sklearn import datasets, manifold, neighbors, metrics
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
import tensorflow as tf
import numpy as np
import cv2

# Global Variables
SIMPLE_EMBEDDING = False
MANUAL_SPLIT = True
DATA_2D = True
N_NEIGHBOURS = 10  # number of nearest neighbours
K_FOLD = 5  # number of groups to split data into for k-fold cross validation
DIM = 100  # dimensions; height and width
PIXELS = 255  # number of image pixels - 1
EPOCHS = 5
INPUT_SHAPE = 28
H5 = 'labTwo.h5'


def display_images(digits_im):
    """
    This function allows viewing the data
    """
    i = 0

    for img in digits_im:
        if i < N_NEIGHBOURS:
            # Visualize your data
            im_max = np.max(img)
            img = PIXELS * (np.abs(im_max - img) / im_max)
            res = cv2.resize(img, (DIM, DIM), interpolation=cv2.INTER_CUBIC)
            cv2.imwrite('digit ' + str(i) + '.png', res)
            i += 1
        else:
            break


def hold_out(fn_digits, fn_data, n_sample, percent_split=0.8):
    """
    This function splits the data into training and test sets
    """
    if MANUAL_SPLIT:
        n_train_samples = int(n_sample * percent_split)
        train_dat = fn_data[:n_train_samples, :]
        train_lbls = fn_digits.target[:n_train_samples]
        tst_dat = fn_data[n_train_samples:, :]
        xpctd_lbls = fn_digits.target[n_train_samples:]
    else:
        train_dat, tst_dat, train_lbls, xpctd_lbls = \
            train_test_split(fn_data, fn_digits.target,
                             test_size=(1.0 - percent_split),
                             random_state=0)
    return train_dat, train_lbls, tst_dat, xpctd_lbls


def plot_data(x):
    """
    This function plots either 2D data or 3D data
    """
    if DATA_2D:
        plt.scatter(x[:, 0], x[:, 1])
        plt.show()
    else:
        fig = plt.figure()
        ax = Axes3D(fig)
        ax.scatter(x[:, 0], x[:, 1], x[:, 2])
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        plt.show()


def plot_image(i, predictions, true_label, img):
    predictions_array, true_label, img = predictions[i], true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img, cmap=plt.cm.binary())


def plot_value_array(i, predictions_array, true_label):
    predictions_array, true_label = predictions_array[i], true_label[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    this_plot = plt.bar(range(10), predictions_array, color="#777777")
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions_array)
    this_plot[predicted_label].set_color('red')
    this_plot[true_label].set_color('blue')


def main():
    # Data Visualization
    digits = datasets.load_digits()
    # Function to display the data
    display_images(digits.images)
    # Transforming the data in a (samples, features) matrix:
    n_samples = len(digits.images)
    data = digits.images.reshape((n_samples, -1))

    # Data Dimension
    if DATA_2D:
        n_comp = 2
    else:
        n_comp = 3

    # Data Reduction
    if SIMPLE_EMBEDDING:
        #  Dimensionality Reduction PCA
        pca = PCA(n_components=n_comp)
        x_trans = pca.fit_transform(data)
        plt.scatter(x_trans[:, 0], x_trans[:, 1])
        plt.show()
    else:
        # Manifold embedding with tSNE
        x_trans = manifold.TSNE(n_components=n_comp, init='pca',
                                random_state=0).fit_transform(data)
    # Plotting Data
    plot_data(x_trans)
    # Manually Split your data
    x_train, x_labels, x_test, x_true_labels = hold_out(digits, data,
                                                        n_samples)
    print(data.shape)
    print(x_labels.shape)
    print(x_true_labels.shape)
    # k-NearestNeighbour Classifier
    knn_classifier = neighbors.KNeighborsClassifier(N_NEIGHBOURS,
                                                    weights='distance')
    # Training the model
    knn_classifier.fit(x_train, x_labels)
    predicted_labels = knn_classifier.predict(x_test)
    # Display classifier results
    print("Classification report for classifier %s: nn %s nn"
          % ('k-NearestNeighbour',
             metrics.classification_report(x_true_labels, predicted_labels)))
    print("Confusion matrix:nn %s"
          % metrics.confusion_matrix(x_true_labels, predicted_labels))
    # Cross Validation
    scores = cross_val_score(knn_classifier, data, digits.target, cv=K_FOLD)
    print(scores)
    # Support Vector Machines
    clf_svm = LinearSVC()
    # Training
    clf_svm.fit(x_train, x_labels)
    # Prediction
    y_pred_svm = clf_svm.predict(x_test)
    acc_svm = accuracy_score(x_true_labels, y_pred_svm)
    print("Linear SVM accuracy: ", acc_svm)
    # Cross Validation
    scores = cross_val_score(clf_svm, data, digits.target, cv=K_FOLD)
    print(scores)
    # Deep learning: digits classification
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / PIXELS, x_test / PIXELS
    plt.figure(figsize=(10, 10))

    for i in range(N_NEIGHBOURS):
        plt.subplot(1, N_NEIGHBOURS, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(x_train[i], cmap=plt.cm.binary())
    plt.show()
    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(INPUT_SHAPE, INPUT_SHAPE)),
        tf.keras.layers.Dense(512, activation=tf.nn.relu),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(N_NEIGHBOURS, activation=tf.nn.softmax)
    ])
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=EPOCHS)
    # Save entire model to a HDF5 file
    model.save(H5)
    # Recreate the exact same model, including weights and optimizer
    new_model = tf.keras.models.load_model(H5)
    new_model.summary()
    test_loss, test_acc = new_model.evaluate(x_test, y_test)
    predictions = new_model.predict(x_test)
    np.argmax(predictions[0])
    # Plot the first X test images, their predicted label, and the true label
    # Color correct predictions in blue, incorrect predictions in red
    num_rows, num_cols = N_NEIGHBOURS, 5
    num_images = num_rows * num_cols
    plt.figure(figsize=(2 * 2 * num_cols, 2 * num_rows))

    for i in range(num_images):
        plt.subplot(num_rows, 2 * num_cols, 2 * i + 1)
        plot_image(i, predictions, y_test, x_test)
        plt.subplot(num_rows, 2 * num_cols, 2 * i + 2)
        plot_value_array(i, predictions, y_test)
    plt.show()


if __name__ == "__main__":
    main()
