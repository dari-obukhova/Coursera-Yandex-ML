import re
import numpy as np
from scipy.spatial import distance

words_lists = [] # list of lists, where every list represent a line of the text

lines = 0

# tokenization of words
with open('sentences.txt', 'r') as Sentences:
    for line in Sentences:
        lines += 1
        words_lists.append(re.split('[^A-Za-z]+', line.lower().strip()))

words = [item for sublist in words_lists for item in sublist] # TODO: How to avoid to flat a list?

word_dicc = {}
words_qty = 0
word_index = 0

# dicctionary with indexes for each word
for word in words:
    if word not in word_dicc and (word not in ['']): # to not to inlude the '' which is presented in word_dicc
        word_dicc[word] = word_index
        word_index += 1
        words_qty += 1


word_matrix = np.zeros((lines, words_qty))

line_index = 0

# matrix lines x words (number of occurance of each word in the sentence)
for line in words_lists:
    for word in line:
        if word not in ['']:
            word_index = word_dicc[word]
            word_matrix[line_index][word_index] += 1
    line_index += 1

# calculate the cosine of the angle between the first vector and the rest

distance_cosine = []

for line in range(lines):
    distance_cosine.append(distance.cosine(word_matrix[0], word_matrix[line]))

# find the vector with the minimum distance from the first vector

min_1 = min(distance_cosine[1:]) # to not compare the first vector with it self
min_1_index = distance_cosine.index(min_1)

# find the second vector with the minimum distance from the first vector

distance_cosine.pop(min_1_index)
min_2 = min(distance_cosine[1:])
min_2_index = distance_cosine.index(min_2)

# save the result in the text file

file_obj = open('sentences_result.txt', 'w')
result = str(min_1_index) + ' ' + str(min_2_index)
file_obj.write(result)
file_obj.close()
