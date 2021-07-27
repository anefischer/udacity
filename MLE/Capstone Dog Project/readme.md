# Capstone Project: Dog Project

## Outline

In this project three different Convolutional Neural Networks (CNN) are trained to classified dog breeds. Additionally, the final model is also used to classify actors as dog breeds. (Of course this is just for entertaining.)

The three networks are:
-	Custom made network according to the popular guide from cs231n: https://cs231n.github.io/convolutional-networks/#layers
-	A pretrained ResNet50

The custom build network achieves just an accuracy of 4% while the VGG16 achieves 40% and the ResNet50 about 80%. This example clearly shows the benefit of using a pretrained model.

## Instructions

The plain workspace can be cloned from udacity:
* https://github.com/udacity/dog-project

The images from the dogs and humans to train the networks can be downloaded from the following links and need to be placed in the “dogImages”-folder:
* https://s3-us-west-1.amazonaws.com/udacity-aind/dog-project/dogImages.zip
* http://vis-www.cs.umass.edu/lfw/lfw.tgz

To train the networks udacity provided bootleneck features which can be downloaded from the following links and need to be placed in the “bottleneck_features”-folder:
* https://s3-us-west-1.amazonaws.com/udacity-aind/dog-project/DogVGG16Data.npz
* https://s3-us-west-1.amazonaws.com/udacity-aind/dog-project/DogResnet50Data.npz

