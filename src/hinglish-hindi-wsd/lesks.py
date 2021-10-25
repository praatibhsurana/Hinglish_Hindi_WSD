from indic_transliteration import sanscript
from indic_transliteration.sanscript import SchemeMap, SCHEMES, transliterate

from spello.model import SpellCorrectionModel
import pyiwn
import sys

from nltk.tag import tnt
from nltk.corpus import indian
import nltk

import wsd


def lesk(word, postag, sentence):

    # sentence - raw hinglish sentence to be transliterated to hindi and wsd carried out
    # returns each word and it's respective meaning

    # Transliterate
    # corrected_hindi = wsd.preprocess_transliterate(sentence)

    # POS tagging for words in the transliterated sentence
    # tags = wsd.POS_tagger(sentence)

    iwn = pyiwn.IndoWordNet()

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

    # Lesk's Algorithm

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

    if len(senses) > 0:
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

        print("Meaning of", word, " is:", result)

    else:
        print(word, "is not in wordnet")
