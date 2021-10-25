from indic_transliteration import sanscript
from indic_transliteration.sanscript import SchemeMap, SCHEMES, transliterate

from spello.model import SpellCorrectionModel
import pyiwn
import sys

from nltk.tag import tnt
from nltk.corpus import indian
import nltk
from hipos import pos_pipeline

# Loading spell correction model
sp = SpellCorrectionModel(language='hi')
sp.load('./src/hi.pkl')

# Stopwords
# words = []
# with open('/content/drive/MyDrive/hinglish_stopwords.txt', 'r') as f:
#   words = f.readlines()

# stopwords = []
# for word in words:
#   stopwords.append(word[:-1])


def preprocess_transliterate(sentence):

    # sentence - hinglish sentence to be processed
    # Returns hinglish and hindi sentence after stopword removal, transliteration and spell check

    arr = sentence.split()

    # Correcting hinglish words to assist hindi correction model
    barr = []
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    # sarr_new = []

    for word in arr:

        # flag = 0

        # if word in sarr:
        #   flag = 1

        for i in range(1, len(word)-2):
            # and word[i+2] not in consonants:
            if len(word) > 3 and word[i-1] in consonants and word[i+1] in consonants and word[i] == 'a':
                word = word[:i] + 'a' + word[i:]
                break

        # if len(word) == 3:
        #     if word[1] == 'a' and word[0] in consonants and word[2] in consonants:
        #       word = word[0] + word[1] + 'a' + word[2]

        if word[len(word) - 1] == 'a' and word[len(word) - 2] != 'a':
            word = word + 'a'
            barr.append(word)
        else:
            barr.append(word)

        # if flag:
        #     sarr_new.append(word)

    # Transliteration
    hinglish = ' '.join(barr)
    hindi = transliterate(hinglish, sanscript.ITRANS, sanscript.DEVANAGARI)

    # hinglish_swr = ' '.join(sarr_new)
    # hindi_swr = transliterate(hinglish_swr, sanscript.ITRANS, sanscript.DEVANAGARI)

    # Spell correction
    tf = sp.spell_correct(hindi)
    corrected_hindi = tf['spell_corrected_text']

    # tf_swr = sp.spell_correct(hindi_swr)
    # corrected_hindi_swr = tf_swr['spell_corrected_text']

    return hinglish, corrected_hindi  # corrected_hindi_swr


def POS_tagger(sentence):

    # sentence - Hindi sentence for which POS is needed to be found
    # returns mapped POS such that they can be used with pyiwn

    tagged = pos_pipeline(sentence)

    print("Tagged:", tagged)

    words = []
    tags = []

    for i in range(len(tagged)):

        if i % 2 == 0:
            words.append(tagged[i])
        else:
            tags.append(tagged[i])

    pos = []

    for i in range(len(words)):

        if (tags[i].startswith('N')):
            pos.append((words[i], 'NOUN'))
        elif (tags[i].startswith('V')):
            pos.append((words[i], 'VERB'))
        elif (tags[i].startswith('J') or tags[i].startswith('Q')):
            pos.append((words[i], 'ADJECTIVE'))
        elif (tags[i].startswith('R')):
            pos.append((words[i], 'ADVERB'))

    return pos
