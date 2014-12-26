# some_file.py
import sys
sys.path.insert(0, '/home/sshrandy/GitProjects/sickly')

from sickness_classifier_defines import generateNgramModel, sicknessClassifier
from tweet_tokenizer import Tokenizer
from nltk.probability import LidstoneProbDist, WittenBellProbDist
from nltk.model import NgramModel
from nltk.tokenize import sent_tokenize, word_tokenize

healthy_f = open('healthy_tweets.txt', 'r')
sick_f = open('sick_tweets.txt','r')

validation_f = open('validation.txt','w')
healthy_training_f = open('healthy_training.txt', 'w')
sick_training_f = open('sick_training.txt', 'w')


counter = 0
counter_2 = 0
for line in healthy_f:
    if counter < 5:
        counter+= 1
        healthy_training_f.write(line)
    elif counter_2 < 20:
        validation_f.write(line)
        counter_2 += 1
        
counter = 0
counter_2 = 0

for line in sick_f:
    if counter < 5:
        counter+= 1
        sick_training_f.write(line)
    elif counter_2 < 20:
        validation_f.write(line)
        counter_2 += 1
        
sick_training_f.close()
healthy_training_f.close()
validation_f.close()
        
validation_f = open('validation.txt', 'r')

sickNgramModel = generateNgramModel('./', 'sick_training.txt')
healthyNgramModel = generateNgramModel('./', 'healthy_training.txt')


ark_tokenizer = Tokenizer()
    
number_correct = 0
line_number = 0
for line in validation_f:
    if line_number < 20:
        sick_perplexity = sickNgramModel.perplexity(ark_tokenizer.tokenize(line))
        healthy_perplexity = healthyNgramModel.perplexity(ark_tokenizer.tokenize(line))
        if(healthy_perplexity < sick_perplexity):
            number_correct+= 1
            print "yay"
        else:
            print "boo"
        line_number+= 1
    else:
        sick_perplexity = sickNgramModel.perplexity(ark_tokenizer.tokenize(line))
        healthy_perplexity = healthyNgramModel.perplexity(ark_tokenizer.tokenize(line))
        if(sick_perplexity < healthy_perplexity):
            number_correct+= 1
            print "yay"
        else:
            print "boo"
            
print number_correct