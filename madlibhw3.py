#project 3 by Jessica Stuart

# code developed by Jackie Cohen; revised by Paul Resnick
# further revised by Colleen van Lent for Python3
import nltk # requires some downloading/installing dependencies to use all its features; numpy is especially tricky to install
import random

#import nltk
nltk.download('punkt')
#nltk.download()

from nltk import word_tokenize,sent_tokenize
from nltk.text import Text
from nltk.corpus import gutenberg

debug = False #True

# get file from user to make mad lib out of
if debug:
	print ("Getting information from file madlib_test.txt...\n")

fname = "austen-sense.txt" # need a file with this name in directory

f = open(fname, 'r')
para = f.read()

tokens = nltk.word_tokenize(para)
#print("TOKENS")
#print(tokens[:151])
tagged_tokens = nltk.pos_tag(tokens) # gives us a tagged list of tuples
#print("TAGGED TOKENS")
#print(tagged_tokens)
if debug:
	print ("First few tagged tokens are:")
	for tup in tagged_tokens[:151]:
		print (tup)
x = []
for each in tagged_tokens[:151]:
	x.append(each[0])

print ( " ". join(x))

tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective", "PRP": "a preposition"}
substitution_probabilities = {"NN":.15,"NNS":.10,"VB":.10,"JJ":.10, "PRP":.10}

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

final_words = []

count = 0 
for (word, tag) in tagged_tokens:
	if count <= 151: 
		if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
			final_words.append(spaced(word))
		else:
			new_word = input("Please enter %s:\n" % (tagmap[tag]))
			final_words.append(spaced(new_word))
			count +=1
			continue 

print ("".join(final_words))