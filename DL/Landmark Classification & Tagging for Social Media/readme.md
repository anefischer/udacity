# Project: Landmark Classification & Tagging for Social Media


## Project Overview
In this project, you will apply the skills you have acquired in the Convolutional Neural Network (CNN) module to build a landmark classifier.

Photo sharing and photo storage services like to have location data for each photo that is uploaded. With the location data, these services can build advanced features, such as automatic suggestion of relevant tags or automatic photo organization, which help provide a compelling user experience. Although a photo's location can often be obtained by looking at the photo's metadata, many photos uploaded to these services will not have location metadata available. This can happen when, for example, the camera capturing the picture does not have GPS or if a photo's metadata is scrubbed due to privacy concerns.

If no location metadata for an image is available, one way to infer the location is to detect and classify a discernible landmark in the image. Given the large number of landmarks across the world and the immense volume of images that are uploaded to photo sharing services, using human judgement to classify these landmarks would not be feasible.

In this project, you will take the first steps towards addressing this problem by building models to automatically predict the location of the image based on any landmarks depicted in the image. You will go through the machine learning design process end-to-end: performing data preprocessing, designing and training CNNs, comparing the accuracy of different CNNs, and using your own images to heuristically evaluate your best CNN.

## Project Steps
The high level steps of the project include:

* Create a CNN to Classify Landmarks (from Scratch) - Here, you'll visualize the dataset, process it for training, and then build a convolutional neural network from scratch to classify the landmarks. You'll also describe some of your decisions around data processing and how you chose your network architecture.

* Create a CNN to Classify Landmarks (using Transfer Learning) - Next, you'll investigate different pre-trained models and decide on one to use for this classification task. Along with training and testing this transfer-learned network, you'll explain how you arrived at the pre-trained network you chose.

* Write Your Landmark Prediction Algorithm - Finally, you will use your best model to create a simple interface for others to be able to use your model to find the most likely landmarks depicted in an image. You'll also test out your model yourself and reflect on the strengths and weaknesses of your model.

## Starter Code and Instructions
Clone the project from the GitHub [repository](https://github.com/udacity/nd101-c2-landmarks-starter), or use the classroom workspace on the next page. Follow the instructions in the README and jupyter notebook to complete the project.

## Review
The reviewer linked to the following articles about different network structures:
* https://towardsdatascience.com/the-w3h-of-alexnet-vggnet-resnet-and-inception-7baaaecccc96
* https://towardsdatascience.com/architecture-comparison-of-alexnet-vggnet-resnet-inception-densenet-beb8b116866d
