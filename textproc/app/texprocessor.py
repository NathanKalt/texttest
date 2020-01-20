# -*- coding: utf-8 -*
from nltk.collocations import  BigramCollocationFinder, TrigramCollocationFinder, QuadgramCollocationFinder
from nltk.metrics import BigramAssocMeasures, TrigramAssocMeasures, QuadgramAssocMeasures
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk import everygrams
from six import iteritems
from nltk import ngrams
import pandas as pd
import numpy as np
import collections
import string
import nltk
import re

nltk.download('punkt')
nltk.download('stopwords')

class Text_Table:

    def __init__(self, text = ''):
        self.text = text
        self.text_df = None
        self.prepared_text = None
        self.grams_df = pd.DataFrame()
        self.pptext = ''
        self.ngrams = ""

    def index_text(self, text = ''):
        # if len(text) == 0: text = '-- text is empty --'
        text = text.split()
        self.text_df = pd.DataFrame(text)
        self.text_df.columns = ['text']
        # print(self.text_df.to_string())


    def tokenize(self, sentences):
        for sent in nltk.sent_tokenize(sentences.lower()):
            for word in nltk.word_tokenize(sent):
                # print(word)
                yield word

    def markup(self, row):
        points = []
        seq = []
        l = len(row) - 1
        for i in row:
            points.append(self.text_df.index[self.text_df['text'] == i].to_list())

        # for i in points[0]:
        #     r = [i]
        #     s = 0
        #     print (r)
        #     while s < l:
        #         s += 1
        #         for v in points[s]:
        #             # print (r[s-1],v)
        #             if v == r[s-1] or v == r[s-1]+1: r.append(v)

            # seq.append(r)


        # print(seq)
        return seq

    def prepare_text(self):
        regex_pat = r"\d+"
        self.text_df['prepared'] = self.text_df['text'].str.lower()
        self.text_df['prepared'] = self.text_df['prepared'].str.replace(' ', '')
        self.text_df['tokens'] = [nltk.word_tokenize(w) for w in self.text_df['prepared']]
        text = nltk.Text(''.join(tkn) for tkn in self.text_df['tokens'])
        stop_words = set(stopwords.words('english'))
        stop_punkt = re.compile('\.|;')

        gram_len = 10
        self.ngram_fd = everygrams(text, min_len=2, max_len=gram_len)
        everyg = list(self.ngram_fd)
        everyg = [item for item, count in collections.Counter(everyg).items() if count >= 3]
        everyg2 = []
        for i in everyg:
            k = re.split(stop_punkt,' '.join(i))
            everyg2 += k
        everyg2 = list(set(everyg2))
        everyg2 = [i.split() for i in everyg2 if len(i.split())>=2]
        ngramms = []
        for i in range(gram_len+1):
            for gram in everyg2:
                if gram[0] not in stop_words:
                    if gram[-1] not in stop_words:
                        if gram not in ngramms: ngramms.append(' '.join(gram))

        ngramms = list(set(ngramms))
        ngramms.sort(key=len, reverse=True)
        ngrams_df = pd.DataFrame(ngramms, columns=['ngram'])
        text = ' '.join(self.text_df['text'].to_list()).lower()
        ngrams_df['count'] = [text.count(i) for i in ngrams_df['ngram']]
        ngrams_df['links'] = ngrams_df['ngram'].str.split()
        # ngrams_df['points'] = ngrams_df['links'].apply(self.markup)
        self.ngrams = ngrams_df[['ngram', 'count']].to_string()

    def __repr__(self):
        return self.text_df.to_string()

class Phrase:
    def __init__(self, ngramm = [], oc=0):
        self.text = ' '.join(ngramm)
        self.len = len(ngramm)
        self.ngram = ngramm

class Word:
    def __init__(self):
        a = 0