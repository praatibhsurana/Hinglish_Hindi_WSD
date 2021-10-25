from polyglot_tokenizer import Tokenizer
from indic_tagger.tagger.src.algorithm.CRF import CRF
from sklearn.model_selection import train_test_split
from time import time
import numpy as np
import pickle
import logging
import argparse
import indic_tagger.tagger.utils.writer as data_writer
import indic_tagger.tagger.src.generate_features as generate_features
import indic_tagger.tagger.src.data_reader as data_reader
# import lstmcrf
from indic_tagger.lstmcrf.utils import load_data_and_labels
from indic_tagger.lstmcrf.wrapper import Sequence
import sys
import os.path as path
import os
sys.path.append(path.dirname(path.abspath(__file__)))


def pos_pipeline(sentence):

    f = open('./src/test.txt', 'w', encoding='utf8')
    f.write(sentence)
    f.close()

    curr_dir = path.dirname(path.abspath(__file__))
    args = {'pipeline_type': 'predict', 'language': 'hi', 'tag_type': 'pos',
            'model_type': 'crf', 'encoding': 'utf', 'data_format': 'txt', 'sent_split': True, 'test_data': './src/test.txt', 'output_path': './src/out.txt'}

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
                tagger = CRF(tag_model_path)
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
                tagger = CRF(model_path)
                tagger.load_model()
                y_pred = tagger.predict(X_test)
                print("Y_PRED:", y_pred)
                data_writer.write_anno_to_file(
                    args['output_path'], test_sents, y_pred, args['tag_type'])
                tagged = data_writer.write_to_screen(args['output_path'])
                # logger.info("Output in: %s" % args.output_path)

            # if args['model_type'] == "lstm":
            #     model = Sequence().load(model_path+"/weights.h5", model_path +
            #                             "/params.json", model_path+"/preprocessor.json")
            #     f = open(args['test_data'], "r")
            #     sent = f.read()
            #     tok = Tokenizer(lang=args['language'], split_sen=True)
            #     tokenized_sents = tok.tokenize(sent)
            #     for tokens in tokenized_sents:
            #         for token in tokens:
            #             sent = sent + " " + token
            #         sent = sent.strip()
            #         print(model.analyze(sent))

    return tagged.split()


# tagged = pos_pipeline("कल मैं बाहर जाऊंगा")
# print(tagged)
