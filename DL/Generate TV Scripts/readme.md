# Project: Generate TV Scripts

## Review:
* Consider using [Python assertions](https://realpython.com/lessons/assertions/) for sanity testing - assertions are great for catching bugs. This is especially true of a dynamically type-checked language like Python where a wrong variable type or shape can cause errors at runtime
* Logging is important for long-running applications. Logging done right produces a report that can be analyzed to debug errors and find crucial information. There could be different levels of logging or logging tags that can be used to filter messages most relevant to someone. Messages can be written to the terminal using print() or saved to file, for example using the [Logger module](https://docs.python.org/3/library/logging.html). Sometimes it's worthwhile to catch and log exceptions during a long-running operation so that the operation itself is not aborted.
* Check out this guide on [debugging in python](https://towardsdatascience.com/ultimate-guide-to-python-debugging-854dea731e1b)
* Monitoring progress and debugging with [Tensorboard](https://www.tensorflow.org/tensorboard): This tool can log detailed information about the model, data, hyperparameters, and more. Tensorboard can be used with Pytorch as well.
* Profiling with Pytorch: [Pytorch's profiler](https://pytorch.org/tutorials/recipes/recipes/profiler.html) can be used to break down profiling information by operations (convolution, pooling, batch norm) and identify performance bottlenecks. The performance traces can be viewed in the browser itself. The profiler is a great tool for quickly comparing GPU vs CPU speedups for example.
* * Check out this guide on [Writing Custom Datasets, DataLoaders and Transforms in PyTorch](https://pytorch.org/tutorials/beginner/data_loading_tutorial.html)
* You can check out more features of [Dataloader here](https://pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader)
* Suggested Reading: Visual guide on LSTMs by Chris Olah: https://colah.github.io/posts/2015-08-Understanding-LSTMs/
* Check out this wonderful guide on [HyperParameter Optimization for Deep Neural Networks](https://blog.floydhub.com/guide-to-hyperparameters-search-for-deep-learning-models/)
* These two guides explain the fundamentals of cross-entropy-loss beautifully: [Visual Explanation of Binary Cross-Entropy Loss](https://towardsdatascience.com/understanding-binary-cross-entropy-log-loss-a-visual-explanation-a3ac6025181a), [Introduction to Cross-Entropy Loss](https://rdipietro.github.io/friendly-intro-to-cross-entropy-loss/#entropy)
