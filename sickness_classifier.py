import os
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.probability import LidstoneProbDist, WittenBellProbDist
from nltk.model import NgramModel
from nltk.tokenize import sent_tokenize, word_tokenize


corpusdir = 'corpora/' # Directory of corpus.
SickCorpus = PlaintextCorpusReader(corpusPath, 'sick_tweets.txt')
HealthyCorpus = PlaintextCorpusReader(corpusdir, 'healthy_tweets.txt')
estimator = lambda fdist, bins: LidstoneProbDist(fdist, 0.2)
    


estimator = lambda fdist, bins: LidstoneProbDist(fdist, 0.2)

sick_model_1 = NgramModel(1, SickCorpus.sents(), True, False, estimator)
sick_model_2 = NgramModel(2, SickCorpus.sents(), True, False, estimator)

healthy_model_1 = NgramModel(1, HealthyCorpus.sents(), True, False, estimator)
healthy_model_2 = NgramModel(2, HealthyCorpus.sents(), True, False, estimator)

tweet = "Remember when we were all diagnosed with Bieber fever ? Lol"

print "sick_model_1 is: " + str(sick_model_1.perplexity(word_tokenize(tweet)))
print "sick_model_2 is: " + str(sick_model_2.perplexity(word_tokenize(tweet)))
print "healthy_model_1 is: " + str(healthy_model_1.perplexity(word_tokenize(tweet)))
print "healthy_model_2 is: " + str(healthy_model_2.perplexity(word_tokenize(tweet)))
