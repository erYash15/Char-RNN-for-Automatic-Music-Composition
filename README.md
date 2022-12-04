# Music-Generationn-using-Deep-Learning

This project focuses on generating music automatically using Recurrent Neural Network(RNN). We do not necessarily have to be a music expert in order to generate music. Even a non expert can generate a decent quality music using RNN. We all like to listen interesting music and if there is some way to generate music automatically, particularly decent quality music then it's a big leap in the world of music industry. 
**Task:** Our task here is to take some existing music data then train a model using this existing data. The model has to learn the patterns in music that we humans enjoy. Once it learns this, the model should be able to generate **new** music for us. It **cannot simply copy-paste** from the training data. It has to understand the patterns of music to generate new music. We here are not expecting our model to generate new music which is of professional quality, but we want it to generate a **decent quality music** which should be melodious and good to hear. Now, what is music? In short music is nothing but **a sequence of musical notes**. Our input to the model is a sequence of musical events/notes. Our output will be new sequence of musical events/notes. 
In this project the model is limited to single instrument music as this is a first cut model. In future, it will be extended to multiple instrument music.

## Data Source

1. http://abc.sourceforge.net/NMD/
2. http://trillian.mit.edu/~jc/music/book/oneills/1850/X/

**From first data-source all the data files are downloaded which include:**
- Jigs (340 tunes)
- Hornpipes (65 tunes)
- Morris (31 tunes)
- Playford (15 tunes)
- Reels A-C (81 tunes)
- Reels D-G (84 tunes)
- Reels H-L (93 tunes)
- Reels M-Q (80 tunes)
- Reels R-T (92 tunes)
- Reels U-Z (34 tunes)
- Slip Jigs (11 tunes)
- Waltzes (52 tunes)
- Chrismas Carols and Songs (13 tunes)
- Ashover collection (46 tunes)

The data is saved in **data folder** in .txt format.

## How to run the model

In order to run the model, run the sample.py file. You can also load the weights in the model folder. Each weight file represents epoch number. The model was run for 100 epochs. You can add more layers or fine tune the model "Transfer Learning".
You can run the samples generated at https://abcjs.net/abcjs-editor.html

## Prerequisites

You need to have installed following softwares and libraries in your machine before running this project.

1. Python 3
2. Anaconda: It will install ipython notebook and most of the libraries which are needed like sklearn, pandas, seaborn, matplotlib, numpy, scipy.
3. Tensorflow 2

## Installing

1. Python 3 - https://www.python.org/downloads/
2. Anaconda - https://www.anaconda.com/download/
3. Tensorflow - pip install tensorflow

## References 

- https://folkrnn.org/
- https://en.wikipedia.org/wiki/ABC_notation
- https://abcjs.net/abcjs-editor.html
- https://towardsdatascience.com/how-to-generate-music-using-a-lstm-neural-network-in-keras-68786834d4c5
- http://karpathy.github.io/2015/05/21/rnn-effectiveness/
- https://medium.com/artists-and-machine-intelligence/neural-nets-for-generating-music-f46dffac21c0
