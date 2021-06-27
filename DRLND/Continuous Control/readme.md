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

## Review:
* The recent achievement of the [Open AI group to play Dota 2](https://blog.openai.com/dota-2/) using Reinforcement Learning is a must read.
* Tensorflow and PyTorch are the two most competing choices for Deep Learning Applications. It would be good to check Tensorflow or PyTorch : [The Force is Strong with which One?](https://medium.com/@UdacityINDIA/tensorflow-or-pytorch-the-force-is-strong-with-which-one-68226bb7dab4)
* For additional resources on creating READMEs or using Markdown, see [here](https://www.udacity.com/courses/ud777) and [here](https://guides.github.com/features/mastering-markdown/).
* An effective way to improve the performance of DDPG is by using Prioritized Experience Replay. You should check this [github repo](https://github.com/rlcode/per) for a fast implementation of Prioritized Experience Replay using a special data structure Sum Tree.
* As specified in the report, an effective way to improve the performance of DDPG is by using Prioritized Experience Replay. You should check this [github repo](https://github.com/rlcode/per) for a fast implementation of Prioritized Experience Replay using a special data structure Sum Tree.
* Following posts give an insight into some other reinforcement learning algorithms that can be used to solve the environment: [Proximal Policy Optimization by Open AI](https://blog.openai.com/openai-baselines-ppo/), [Introduction to Various Reinforcement Learning Algorithms. Part II (TRPO, PPO)](https://towardsdatascience.com/introduction-to-various-reinforcement-learning-algorithms-part-ii-trpo-ppo-87f2c5919bb9)
