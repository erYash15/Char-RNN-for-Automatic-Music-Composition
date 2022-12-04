import os 
import json 
import numpy as np

DATA_DIR = "./clean_data/"
BATCH_SIZE = 32

text = open(os.path.join(DATA_DIR, 'final_data.txt')).read()


char_to_idx = { ch: i for (i, ch) in enumerate(sorted(list(set(text)))) }
print("Number of unique characters: " + str(len(char_to_idx))) #86

with open(os.path.join(DATA_DIR, 'char_to_idx.json'), 'w') as f:
     json.dump(char_to_idx, f)
     
T = np.asarray([char_to_idx[c] for c in text], dtype=np.int32) #convert complete text into numerical indices

print("Length of text:" + str(T.size))
length = T.size
batch_chars = int(length / BATCH_SIZE)
print(batch_chars)
