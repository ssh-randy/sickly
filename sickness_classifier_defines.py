import os
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.probability import LidstoneProbDist, WittenBellProbDist
from nltk.model import NgramModel
from nltk.tokenize import sent_tokenize, word_tokenize


def generateNgramModel(corpusPath, corpusName):
    corpusdir = 'corpora/' # Directory of corpus.
    generatedCorpus = PlaintextCorpusReader(corpusPath, corpusName)
    estimator = lambda fdist, bins: LidstoneProbDist(fdist, 0.2)
    ngrammodel = NgramModel(2, generatedCorpus.sents(), True, False, estimator) #uses bigrams just cause they BETTER
    return ngrammodel

#returns TRUE if the first ngrammodel has a lower perplexity than the second
def sicknessClassifier(SickNgramModel, HealthyNgramModel, tweet_string):
    sick_perplexity = SickNgramModel.perplexity(word_tokenize(tweet_string))
    healthy_perplexity = HealthyNgramModel.perplexity(word_tokenize(tweet_string))
    return ( sick_perplexity <= healthy_perplexity)