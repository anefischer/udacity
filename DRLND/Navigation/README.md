# Udacity Deep Reinforcement Learning - Projet 1

This is my solution of Project 1 Navigation for the Deep Reinforcement Learning Nanodegree by Udacity. 

## Workspace 
If you want to run my implementation or maybe even want to solve the project yourself its best to start at the official github by Udacity:
* [Udacity Workspace](https://github.com/udacity/deep-reinforcement-learning/blob/master/p1_navigation/README.md)

## Q-Network
Difficult? Well, not if you followed the course. There we learned about Deep Q-network(DQN). The course explained in detail how to use it, I can highly recommend it and implement the DQN yourself. Again you can find the source code at the official github:
* [Udacity DQN Exercice](https://github.com/udacity/deep-reinforcement-learning/tree/master/dqn)

## Implementation
The solution now is very simple. We just need to adopt the DQN to interact with the given environment of the unity engine. Just look at my code and the comments. 
I set a limit of the training score at 13. I only once reached 14 and nearly ran out of gpu time. 


## Review:

* For an extra challenge, try to train an agent from raw pixels! In case you get stuck, take a look at [this github repository](https://github.com/chocolateHszd/RL_Navigation) and [this other one](https://github.com/yingweiy/drlnd_project1_navigation)
* Suggested reading: [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html), [PEP 8 — the Style Guide for Python Code](https://pep8.org/), [Python Best Practices](https://airbrake.io/blog/python/python-best-practices), [Clean Code Summary](https://gist.github.com/wojteklu/73c6914cc446146b8b533c0988cf8d29)
* Suggested reading about the discussion of what machine learning framework should be used: [TensorFlow vs. Pytorch](https://dzone.com/articles/the-battle-tensorflow-vs-pytorch), [Tensorflow or PyTorch : The force is strong with which one?](https://medium.com/@UdacityINDIA/tensorflow-or-pytorch-the-force-is-strong-with-which-one-68226bb7dab4), [What is the best programming language for Machine Learning?](https://towardsdatascience.com/what-is-the-best-programming-language-for-machine-learning-a745c156d6b7), [Deep Learning Frameworks Comparison – Tensorflow, PyTorch, Keras, MXNet, The Microsoft Cognitive Toolkit, Caffe, Deeplearning4j, Chainer](https://www.netguru.co/blog/deep-learning-frameworks-comparison)
* Suggested reading: [Saving and Loading Models](https://pytorch.org/tutorials/beginner/saving_loading_models.html), [Best way to save a trained model in PyTorch?](https://stackoverflow.com/questions/42703500/best-way-to-save-a-trained-model-in-pytorch)
* I recommend you to check: This awesome [template to make good README.md](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2), This article: [Make a README - Because no one can read your mind (yet)](https://www.makeareadme.com/)
* The README must describe all instructions for: Installing [dependencies](https://github.com/udacity/deep-reinforcement-learning#dependencies), Downloading needed files in [Getting Started instructions item](https://github.com/udacity/deep-reinforcement-learning/tree/master/p1_navigation#getting-started)
* I recommend you to check the [Mastering Markdown](https://guides.github.com/features/mastering-markdown/), there are great tips about how to use Markdown
* You could consider the use of Prioritized Experience Replay: [Prioritized Experience Replay](http://arxiv.org/abs/1511.05952), [Implementation of Prioritized Experience Replay](https://github.com/Damcy/prioritized-experience-replay), [Let’s make a DQN: Double Learning and Prioritized Experience Replay](https://jaromiru.com/2016/11/07/lets-make-a-dqn-double-learning-and-prioritized-experience-replay/)
* Prioritized Experience Replay (PER) helps to improve the performance and also helps to significantly reduce the training time, using Sum Tree, a special data structure. Take a look at this [implementation](https://github.com/rlcode/per)
* Take a look at the following resources to get familiar with the Rainbow algorithm: [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://arxiv.org/abs/1710.02298), [Conquering OpenAI Retro Contest 2: Demystifying Rainbow Baseline](https://medium.com/intelligentunit/conquering-openai-retro-contest-2-demystifying-rainbow-baseline-9d8dd258e74b)
* Reinforcement learning algorithms are really hard to make work. Take a look at this article: [Deep Reinforcement Learning Doesn't Work Yet](https://www.alexirpan.com/2018/02/14/rl-hard.html)
