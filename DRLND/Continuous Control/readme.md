# Udacity Deep Reinforcement Learning ? Project 2

This is my solution of Project 2 Continuous Control for the Deep Reinforcement Learning Nanodegree by Udacity. 

## Workspace 
If you want to run my implementation or maybe even want to solve the project yourself its best to start at the official github by Udacity and setup the Python environment correctly:
* [Udacity Workspace](https://github.com/udacity/deep-reinforcement-learning/tree/master/p2_continuous-control)
* [Python Dependencies](https://github.com/udacity/deep-reinforcement-learning#dependencies)

Additionally the Unity Environment for your OS is required:
* [Windows](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86_64.zip)
* [OSX](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher.app.zip)
* [Linux](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Linux.zip)

## Deep Deterministic Policy Gradient-Network
Difficult? Well, not if you followed the course. There we learned about DDPG The course explained in detail how to use it, I can highly recommend it and implement the DDPG yourself. Again you can find the source code at the official github:
* [Udacity DDPQ Exercise]( https://github.com/udacity/deep-reinforcement-learning/tree/master/ddpg-pendulum)

## Implementation
The solution now is very simple. We just need to adopt the DDPG to interact with the given environment of the unity engine. Just look at my code and the comments. 
There are a few parameters to tweak and play with. But the most important one is to increase max_t. 

You can copy my files to your workspace and start the training straight out of the notebook. Chears.


