# Automatic-Music-Composition

## Project Name: Char-RNN-for-Automatic-Music-Composition

Multi-layer recurrent neural networks for training and sampling from texts, inspired by [karpathy/char-rnn](https://github.com/karpathy/char-rnn).

### Description:
	
Code is divided into 3 Parts.

_Objective 1_ - Training Model

_Objective 2_ - Model Making

_Objective 3_ - Sample Creation

### Table of Contents

#### Directories

[datasets](https://github.com/erYash15/Char-RNN-for-Automatic-Music-Composition/tree/master/datasets) - Contains all the training data [ABC version of the Nottingham Music Database](http://abc.sourceforge.net/NMD/) in .txt format 
[models]() - Contains saved Model and Weights in h5 format.
[training_log]() - Contains training accuracy and training loss for every epoch in .csv format 

#### Codes

[train.py]() - processing data and training Models and saves the weights
[model.py]() - Create Models and functionality like saving and loading weights
[sample.py]() - Loads the models and create the new music data

### Requirements

This code is written in Python 3, and it requires the 
 - [Tensorflow](https://www.tensorflow.org/)
 - [Keras](https://keras.io)
 - [NumPy](http://www.numpy.org/)
 - [Pickle](https://docs.python.org/3/library/pickle.html)

### Usage

Type in terminal command in the root directory after downloading or cloning ( where this readme is present ).

```bash
$ python train.py
```

```bash
$ python sample.py
```

### Credits:

1. Keunwoo Choi, George Fazekas, and Mark Sandler. 2016. Text-basedLSTM networks for automatic music composition. arXiv preprint
arXiv:1604.05358 (2016).(https://arxiv.org/abs/1604.05358)

2. http://karpathy.github.io/2015/05/21/rnn-effectiveness/

3. https://medium.com/datadriveninvestor/music-generation-using-deep-learning-85010fb982e2



