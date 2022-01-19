from polyglot_tokenizer import Tokenizer
from hindiwsd.CRF import CRF 
from sklearn.model_selection import train_test_split
from time import time
import numpy as np
import pickle
import logging
import argparse
import hindiwsd.writer as data_writer
from hindiwsd import generate_features, data_reader 
#import lstmcrf
from hindiwsd.utils import load_data_and_labels
from hindiwsd.wrapper import Sequence
import sys
import os.path as path
import os
sys.path.append(path.dirname(path.abspath(__file__)))

from twisted.python.modules import getModule

moduleDirectory = getModule("hindiwsd").filePath.parent()
crf_pos_model = str(moduleDirectory.child("crf.pos.utf.model"))[10:-2]


def pos_pipeline(sentence):

    f = open('./test.txt', 'w', encoding='utf8')
    f.write(sentence)
    f.close()

    curr_dir = path.dirname(path.abspath(__file__))
    args = {'pipeline_type': 'predict', 'language': 'hi', 'tag_type': 'pos',
            'model_type': 'crf', 'encoding': 'utf', 'data_format': 'txt', 'sent_split': True, 'test_data': './test.txt', 'output_path': './out.txt'}

    output_dir = path.join(path.dirname(path.abspath(__file__)), "outputs")
    # if not os.path.exists(output_dir):
    #     os.makedirs(output_dir)

    # data_writer.set_logger(args.model_type, output_dir)

    if True:
        model_path = "%s/indic_tagger/models/%s/%s.%s.%s.model" % (
            curr_dir, args['language'], args['model_type'], args['tag_type'], args['encoding'])
        if args['model_type'] == "lstm":
            if args['tag_type'] == "pos":
                model_path = "%s/models/%s/lstm/" % (
                    curr_dir, args['language'])
            elif args['tag_type'] == "chunk":
                model_path = "%s/models/%s/lstm/chunk/" % (
                    curr_dir, args['language'])
            elif args['tag_type'] == "ner":
                model_path = "%s/models/%s/lstm/ner/" % (
                    curr_dir, args['language'])
    # if args['tag_type'] != "parse":
    #     if not os.path.exists(model_path):
    #         os.makedirs(model_path)

    if args['pipeline_type'] == "predict":

        test_data_path = "%s" % (args['test_data'])
        test_sents = data_reader.load_data(
            args['data_format'], test_data_path, args['language'], tokenize_text=True, split_sent=args['sent_split'])
        if args['tag_type'] == "parse":
            # Pos tagging
            X_test = [generate_features.sent2features(
                s, "pos", args['model_type']) for s in test_sents]

            tag_model_path = "%s/indic_tagger/models/%s/%s.%s.%s.model" % (
                curr_dir, args['language'], args['model_type'], "pos", args['encoding'])
            chunk_model_path = "%s/indic_tagger/models/%s/%s.%s.%s.model" % (
                curr_dir, args['language'], args['model_type'], "chunk", args['encoding'])

            if args['model_type'] == "crf":
                tagger = CRF(crf_pos_model)
                tagger.load_model()
                y_pos = tagger.predict(X_test)

                test_sents_pos = generate_features.append_tags(
                    test_sents, "pos", y_pos)
                X_test = [generate_features.sent2features(
                    s, "chunk", args['model_type']) for s in test_sents_pos]

                chunker = CRF(chunk_model_path)
                chunker.load_model()
                y_chunk = chunker.predict(X_test)

                test_fname = path.basename(test_data_path)
                output_file = "%s/%s.parse" % (output_dir, test_fname)
                data_writer.write_anno_to_file(
                    output_file, test_sents_pos, y_chunk, "chunk")
                # logger.info("Output in: %s" % output_file)
                data_writer.write_to_screen(output_file)
        else:
            X_test = [generate_features.sent2features(
                s, args['tag_type'], args['model_type']) for s in test_sents]

            if args['model_type'] == "crf":
                tagger = CRF(crf_pos_model)
                tagger.load_model()
                y_pred = tagger.predict(X_test)
                # print("Y_PRED:", y_pred)
                data_writer.write_anno_to_file(
                    args['output_path'], test_sents, y_pred, args['tag_type'])
                tagged = data_writer.write_to_screen(args['output_path'])
                # logger.info("Output in: %s" % args.output_path)

    return tagged.split()


# tagged = pos_pipeline("कल मैं बाहर जाऊंगा")
# print(tagged)
