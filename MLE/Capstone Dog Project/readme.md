# Capstone Project: Dog Project

## Outline

In this project three different Convolutional Neural Networks (CNN) are trained to classified dog breeds. Additionally, the final model is also used to classify actors as dog breeds. (Of course this is just for entertaining.)

The three networks are:
-	Custom made network according to the popular guide from cs231n: https://cs231n.github.io/convolutional-networks/#layers
-	A pretrained ResNet50

The custom build network achieves just an accuracy of 10% while the ResNet50 75%. This example clearly shows the benefit of using a pretrained model.

## Instructions

The plain workspace can be cloned from udacity:
* https://github.com/udacity/deep-learning-v2-pytorch/tree/master/project-dog-classification

The images from the dogs and humans to train the networks can be downloaded from the following links and need to be placed in the “dog_images”-folder:
* https://s3-us-west-1.amazonaws.com/udacity-aind/dog-project/dogImages.zip
* http://vis-www.cs.umass.edu/lfw/lfw.tgz


## Review

* Here a useful reference about [Choosing the Right Metric for Evaluating Machine Learning Models](https://www.kdnuggets.com/2018/04/right-metric-evaluating-machine-learning-models-1.html).
* And here an article that discusses [What metrics should be used for evaluating a model on an imbalanced data set](https://towardsdatascience.com/what-metrics-should-we-use-on-imbalanced-data-set-precision-recall-roc-e2e79252aeba)
* For deep learning - https://www.fast.ai/
* General ML, more Developer Oriented - https://machinelearningmastery.com/
* General Data Science - https://www.datasciencecentral.com/
* Podcast - https://dataskeptic.com/
* Grokking Machine Learning - our Luis Serrano’s Intro Level Book https://www.manning.com/books/grokking-machine-learning
* Learning from Data - CalTech Professor abu-Mostafa’s lectures http://work.caltech.edu/lectures.html
* Best AI papers 2020: https://github.com/louisfb01/Best_AI_paper_2020
* https://github.com/Developer-Y/cs-video-courses#math-for-computer-scientist
* Interesting read on metrics for model evaluation: https://www.math.ucdavis.edu/~saito/data/roc/ferri-class-perf-metrics.pdf
* Dataset exploration: https://www.kaggle.com/pmarcelino/comprehensive-data-exploration-with-python
* An interesting read I found recently: A Visual Explanation of Gradient Descent Methods (Momentum, AdaGrad, RMSProp, Adam) (https://towardsdatascience.com/a-visual-explanation-of-gradient-descent-methods-momentum-adagrad-rmsprop-adam-f898b102325c)
* Maybe also plot some Intensity Histograms(https://homepages.inf.ed.ac.uk/rbf/HIPR2/histgram.htm). In an image processing context, the histogram of an image normally refers to a histogram of the pixel intensity values. This histogram is a graph showing the number of pixels in an image at each different intensity value found in that image.
* http://cs231n.github.io/convolutional-networks/
* https://stanford.edu/~shervine/teaching/cs-230/cheatsheet-convolutional-neural-networks
* Some interesting posts on the topic: https://medium.com/levvel-consulting/define-benchmark-deploy-6a8d0fb0decd https://towardsdatascience.com/benchmarking-simple-machine-learning-models-with-featureextraction-against-modern-black-box-80af734b31cc
* Importance of the benchmark in machine learning work: https://blog.dominodatalab.com/benchmarking-predictive-models/
* https://cloud.google.com/solutions/machine-learning/data-preprocessing-for-ml-with-tf-transform-pt1
* https://towardsdatascience.com/understanding-generative-adversarial-networks-gans-cd6e4651a29
* Python framework for feature engineering https://www.featuretools.com/
* Could also even play around with Test Time Augmentation (TTA) - https://towardsdatascience.com/test-time-augmentation-tta-and-how-to-perform-it-with-keras-4ac19b67fb4d
* Modern Data Augmentation Techniques for Computer Vision: https://app.wandb.ai/authors/tfaugmentation/reports/Modern-Data-Augmentation-Techniques-for-Computer-Vision--VmlldzoxNzU3NTU
* Another idea would be to check out using Cyclical Learning Rates for Training Neural Networks(https://arxiv.org/abs/1506.01186). This is where we simply keep increasing the learning rate from a very small value, until the loss stops decreasing and then bump it up once more. We can plot the learning rate across batches to see what this looks like.
* Bag of tricks for improving image classification: https://towardsdatascience.com/a-big-of-tricks-for-image-classification-fec41eb28e01
* 'Ensemble' all of the models 'squeeze out' a few more percentage points by doing so. Could look into using VotingClassifier(https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html)
* Using Progressive resizing: https://towardsdatascience.com/boost-your-cnn-image-classifier-performance-with-progressive-resizing-in-keras-a7d96da06e20
* https://towardsdatascience.com/boost-your-image-classifier-e1cc7a56b59c
* Check out this interesting book that shows how to understand the feature importance and accumulated local effects and explaining individual predictions: https://christophm.github.io/interpretable-ml-book/.
* https://github.com/slundberg/shap
* Data visualization and clustering: https://hypertools.readthedocs.io/en/latest/
* One can use cross validation to check the robustness of the solution. Take a look here: https://machinelearningmastery.com/k-fold-cross-validation/
