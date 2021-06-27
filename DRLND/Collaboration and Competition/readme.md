# Udacity Deep Reinforcement Learning ? Project 2

This is my solution of Project 2 Continuous Control for the Deep Reinforcement Learning Nanodegree by Udacity. 

## Workspace 
If you want to run my implementation or maybe even want to solve the project yourself its best to start at the official github by Udacity and setup the Python environment correctly:
* [Udacity Workspace](https://github.com/udacity/deep-reinforcement-learning/tree/master/p3_collab-compet)
* [Python Dependencies](https://github.com/udacity/deep-reinforcement-learning#dependencies)

Additionally the Unity Environment for your OS is required:
* [Windows](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Windows_x86_64.zip)
* [OSX](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis.app.zip)
* [Linux](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Linux.zip)

## Deep Deterministic Policy Gradient-Network
Difficult? Well, not if you followed the course. There we learned about DDPG The course explained in detail how to use it, I can highly recommend it and implement the DDPG yourself. Again you can find the source code at the official github:
* [Udacity DDPQ Exercise]( https://github.com/udacity/deep-reinforcement-learning/tree/master/ddpg-pendulum)

## Implementation
The solution now is very simple. We just need to adopt the DDPG to interact with the given environment of the unity engine. Additionally the code is modified to take actions for multiple agents with a shared memory. Just look at my code and the comments. 
There are a few parameters to tweak and play with. But the most important one is to increase max_t. 

You can copy my files to your workspace and start the training straight out of the notebook. Chears.

## Review:
* As next step, please go through the resource: [human-like robot hand trained to manipulate physical objects with unprecedented dexterity](https://blog.openai.com/learning-dexterity/).
* A good read: [PyTorch vs TensorFlow — spotting the difference](https://towardsdatascience.com/pytorch-vs-tensorflow-spotting-the-difference-25c75777377b)
* For additional resources on creating READMEs or using Markdown, see [here](https://www.udacity.com/courses/ud777) and [here](https://guides.github.com/features/mastering-markdown/).
* You should try implementing Prioritized Experience Replay also. It helps to improve the performance and significantly reduces the training time. This should also help to stabilize the performance to some extent. A fast implementation of Prioritized Experience Replay is possible using a special data structure called Sum Tree. I found a [good implementation here](https://github.com/rlcode/per).
* Also, I request you to check the following posts to get familiar with more reinforcement learning algorithms: [Asynchronous Actor-Critic Agents (A3C)](https://medium.com/emergent-future/simple-reinforcement-learning-with-tensorflow-part-8-asynchronous-actor-critic-agents-a3c-c88f72a5e9f2), [Trust Region Policy Optimization (TRPO) and Proximal Policy Optimization (PPO)](https://medium.com/@sanketgujar95/trust-region-policy-optimization-trpo-and-proximal-policy-optimization-ppo-e6e7075f39ed)
* Here is an [implementation](https://github.com/jcrudy/drlnd_p3) of PPO on tennis environment. The training was slow but the final average score achieved was almost 1.25 (with some fluctuation). You should surely try PPO in future.
