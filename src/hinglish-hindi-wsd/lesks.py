from statistics import mean
from indic_transliteration import sanscript
from indic_transliteration.sanscript import SchemeMap, SCHEMES, transliterate

from spello.model import SpellCorrectionModel
import pyiwn
import sys

from nltk.tag import tnt
from nltk.corpus import indian
import nltk

from hindiwsd import wsd
import pandas as pd

from twisted.python.modules import getModule

moduleDirectory = getModule("hindiwsd").filePath.parent()
dataset = str(moduleDirectory.child("Hindi_WSD_Dataset - Sheet1.tsv"))[10:-2]

def lesk(word, postag, sentence):

    # sentence - raw hinglish sentence to be transliterated to hindi and wsd carried out
    # returns each word and it's respective meaning

    # Transliterate
    # corrected_hindi = wsd.preprocess_transliterate(sentence)

    # POS tagging for words in the transliterated sentence
    # tags = wsd.POS_tagger(sentence)

    iwn = pyiwn.IndoWordNet()

    # Function for enhancing lesk
    
    def extra_overlap(ambword : str, input_sent : str):

        df = pd.read_csv(dataset, sep = '\t', encoding='utf8')
        #df.head()
        #print(ambword)

        word1 = list(df['Word'])
        sentence = list(df['Sentence'])
        synset = list(df['synset number'])
        words = [] #the words
        sent = [] #their particular sentences
        syn = []
  
        # print(word1)
        for i in range(len(word1)):
            #print(word1[i])
            if str(ambword) == str(word1[i]):
                sent.append(sentence[i])
                syn.append(synset[i])

            # elif str(ambword) != str(word1[i]):

        
        #print("Sentence:", sent)
        lis = list(input_sent.split())
        max_intersection = 0
        synset_final = -1
        meaning = ""

        for i in range(len(syn)):
            input_set = set()
            
            for x in lis:
                #print(x)
                input_set.add(x)
            
            sent_lis = sent[i].split()
            
            # print("Sent_Lis:", sent_lis)
            # print("Input_Set:", input_set)
            
            overlap = input_set.intersection(sent_lis)
            
            #print("Overlap:", overlap)
            
            # synset_final = 0
            if len(overlap) > max_intersection:
                max_intersection = len(overlap)
                synset_final = syn[i]
                if synset_final.startswith("N1"):
                    meaning = synset_final[3:]
            else:
                continue 

        
        return max_intersection, synset_final, meaning

    
    def scanLine(line, wordset):
        strings = line.split()

        for s in strings:
            size = len(s)
            if size <= 2:
                continue
            else:
                wordset[s] = 1


    def computeOverlap(sign, context):
        overlap = 0
        for word, val in sign.items():
            v = context.get(word, 0)
            if v != 0:
                overlap += 1
        return overlap

    #################### Lesk's Algorithm ####################

    context = {}
    scanLine(sentence, context)

    if postag == "NOUN":
        senses = iwn.synsets(word, pos=pyiwn.PosTag.NOUN)
    elif postag == "VERB":
        senses = iwn.synsets(word, pos=pyiwn.PosTag.VERB)
    elif postag == "ADVERB":
        senses = iwn.synsets(word, pos=pyiwn.PosTag.ADVERB)
    elif postag == "ADJECTIVE":
        senses = iwn.synsets(word, pos=pyiwn.PosTag.ADJECTIVE)

    if len(senses) >= 0:
        max_overlap = -1
        result = ''

        for s in senses:
            info = s.gloss()
            for e in s.examples():
                info = info + ' ' + e

            signature = {}

            scanLine(info, signature)
            overlap = computeOverlap(signature, context)
            if overlap > max_overlap:
                max_overlap = overlap
                result = s.gloss()

        intersection, syn_final, meaning = extra_overlap(word, sentence)

        #print("MAX OVERLAP:", max_overlap, "INTERSECTION:", intersection, "SYNSET:", syn_final)
        
        if str(syn_final).startswith("N1"):
            result = meaning
        
        else:
            if intersection>=max_overlap and intersection>0:
                result = iwn.synsets(word)[int(syn_final)].gloss()
                #result = senses[int(syn_final)].gloss()

            if result=="":
                result = "NOT available in wordnet"

        print("Meaning of", word, " is:", result)

    else:
        print(word, "is not in wordnet")




