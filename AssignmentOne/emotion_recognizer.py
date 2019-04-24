#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Intelligent and Interactive Systems
Assignment 1: Machine learning methods for auto recognition of human emotions
Author: Adam Ross
Date: 24/04/2019
"""

# import data sets, classifiers and performance metrics
from __future__ import absolute_import, division, print_function, unicode_literals
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import patches, pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.decomposition import PCA
from sklearn import datasets, manifold, neighbors, metrics
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
import numpy as np
import re


class Recognizer:
    """
    Class for recognizing human emotions using machine learning methods
    """
    FACE_FEAT = 'dataset/Face-Feat-with-image-file-names.txt'
    HOG_FEAT = 'dataset/HogFeat-with-image-file-names.txt'
    CTGRY = {'POSITIVE': [1, 'lime'], 'NEUTRAL': [0, 'skyblue'],
             'NEGATIVE': [-1, 'tomato']}
    SIMPLE_EMBEDDING = True
    MANUAL_SPLIT = False
    DATA_2D = False
    N_NEIGHBOURS = 10  # number of nearest neighbours
    K_FOLD = 5  # number of groups to split data into for k-fold cross validation
    RANDOM_STATE = 5

    def __init__(self):
        """
        Class initializer
        """
        self.data = datasets.base.Bunch(data=[], target=[], col=[])  # data
        self.n = 0  # the number of samples in self.data

    def hold_out(self, percent_split=0.8):
        """
        This function splits the data into training and test sets
        """
        if self.MANUAL_SPLIT:
            n_train_samples = int(self.n * percent_split)
            train_dat = self.data.data[:n_train_samples, :]
            train_lbls = self.data.target[:n_train_samples]
            tst_dat = self.data.data[n_train_samples:, :]
            xpctd_lbls = self.data.target[n_train_samples:]
        else:
            train_dat, tst_dat, train_lbls, xpctd_lbls = \
                train_test_split(self.data.data, self.data.target,
                                 test_size=(1.0 - percent_split),
                                 random_state=self.RANDOM_STATE,
                                 stratify=self.data.target)
        return train_dat, train_lbls, tst_dat, xpctd_lbls

    def plot_data(self, x):
        """
        This function plots either 2D data or 3D data
        """
        if self.DATA_2D:
            plt.scatter(x[:, 0], x[:, 1], c=self.data.col)
        else:
            ax = Axes3D(plt.figure())
            ax.scatter(x[:, 0], x[:, 1], x[:, 2], c=self.data.col)
            ax.set_zlabel("Z Axis")
        plt.legend(handles=[patches.Patch(color=self.CTGRY[i][1], label=i)
                            for i in self.CTGRY.keys()])
        plt.title("Human Emotion Recognition")
        plt.xlabel("X Axis")
        plt.ylabel("Y Axis")
        plt.grid(True)
        plt.show()

    def merge_files(self):
        """
        Merges extracted hog data to extracted face data and formats to Bunch
        """
        # extracts file data to array, splits each line into list of strings
        # splices file name for each line to match corresponding image name
        # sorts data so the output is in alphabetical order of category
        face = sorted([[i.split(",\t")[0][-8:-4]] + i.split(",\t")[1:-1] for i
                       in open(self.FACE_FEAT).readlines()], key=lambda x: x[1])
        hog = sorted([[i.split(",\t")[0][-8:-4]] + re.split("[,\t\n]+", i)[1:-1]
                   for i in open(self.HOG_FEAT).readlines()], key=lambda x: x[1])

        for h in hog:
            if h[0] == face[self.n][0]:
                if not self.n:
                    self.data.col = np.array([self.CTGRY[face[self.n][1]][1]])
                    self.data.target = np.array([self.CTGRY[face[self.n][1]][0]])
                    self.data.data = np.array([[float(j) for j in
                                                face[self.n][2:] + h[2:]]])
                else:
                    self.data.col = np.append(self.data.col, [self.
                                              CTGRY[face[self.n][1]][1]], axis=0)
                    self.data.target = np.append(self.data.target, [self.CTGRY[
                                                 face[self.n][1]][0]], axis=0)
                    self.data.data = np.append(self.data.data,
                                               np.array([[float(j) for j in
                                                          face[self.n][2:] +
                                                          h[2:]]]), axis=0)
                self.n += 1

    def data_reduction(self):
        """
        Data reduction
        """
        n_comp = 2 if self.DATA_2D else 3

        if self.SIMPLE_EMBEDDING:
            # dimensionality Reduction PCA for data reduction
            return PCA(n_components=n_comp).fit_transform(self.data.data)
        # manifold embedding with tSNE for data reduction
        return manifold.TSNE(n_components=n_comp, init='pca',
                             random_state=self.RANDOM_STATE).fit_transform(self.data.data)

    def knn_analysis(self, train, labels, test, true_labels):
        """
        K-NearestNeighbour classifier analysis of trained and tested model
        """
        knn_classifier = neighbors.KNeighborsClassifier(self.N_NEIGHBOURS,
                                                        weights='distance')
        knn_classifier.fit(train, labels)  # training the model
        predicted_labels = knn_classifier.predict(test)  # prediction
        print("Classification report for classifier %s: \n %s \n"
              % ('k-NearestNeighbour', metrics.
                 classification_report(true_labels, predicted_labels)))
        print("Confusion matrix:\n %s"
              % metrics.confusion_matrix(true_labels, predicted_labels))
        return cross_val_score(knn_classifier, self.data.data,
                               self.data.target, cv=self.K_FOLD)

    def svm_analysis(self, train, labels, test, true_labels, svm=LinearSVC()):
        """
        Support vector machine classifier analysis of trained and tested model
        """
        svm.fit(train, labels)  # training the model
        y_pred_svm = svm.predict(test)  # prediction
        print("Linear SVM accuracy: ", accuracy_score(true_labels, y_pred_svm))
        return cross_val_score(svm, self.data.data, self.data.target,
                               cv=self.K_FOLD)

    def main(self):
        # merge face and hog data sets
        self.merge_files()
        # data reduction and visualization
        self.data.data = self.data.data.reshape(len(self.data.data), -1)
        self.plot_data(self.data_reduction())
        # split data
        x_train, x_labels, x_test, x_true_labels = self.hold_out()
        # train, test and analyze models for auto emotion recognition
        print(self.knn_analysis(x_train, x_labels, x_test, x_true_labels))
        print(self.svm_analysis(x_train, x_labels, x_test, x_true_labels))


if __name__ == "__main__":
    app = Recognizer()
    app.main()
