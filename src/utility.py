from typing import *
import pickle
from constants import Global


class Assignment1Stats(object):

    def __init__(self):
        self.untagged_training_count: int = 0
        self.tagged_training_count: int = 0
        self.untagged_testing_count: int = 0
        self.tagged_testing_count: int = 0
        self.untagged_validation: int = 0
        self.tagged_validation: int = 0

        self.untagged_vocab_count: int = 0
        self.tagged_vocab_count: int = 0

        self.tokens_removed_a_count: int = 0
        self.tokens_removed_b_count: int = 0
        self.tokens_removed_c_count: int = 0
        self.tokens_removed_d_count: int = 0

        self.populate()

    def populate(self):
        print('prepping stats')
        tagged_train_tokens = pickle.load(open(Global.tagged_train_pickle_url, 'rb'))
        tagged_test_tokens = pickle.load(open(Global.tagged_test_pickle_url, 'rb'))
        tagged_valid_tokens = pickle.load(open(Global.tagged_valid_pickle_url, 'rb'))
        tagged_vocab = pickle.load(open(Global.tagged_vocab_pickle_url, 'rb'))
        untagged_vocab = pickle.load(open(Global.vocab_pickle_url, 'rb'))

        a_tokens_train = tagged_train_tokens.count('<year>')
        a_tokens_test = tagged_test_tokens.count('<year>')
        a_tokens_valid = tagged_valid_tokens.count('<year>')

        b_tokens_train = tagged_train_tokens.count('<realnumber>')
        b_tokens_test = tagged_test_tokens.count('<realnumber>')
        b_tokens_valid = tagged_valid_tokens.count('<realnumber>')

        c_tokens_train = tagged_train_tokens.count('<month>')
        c_tokens_test = tagged_test_tokens.count('<month>')
        c_tokens_valid = tagged_valid_tokens.count('<month>')

        d_tokens_train = tagged_train_tokens.count('<country_name>')
        d_tokens_test = tagged_test_tokens.count('<country_name>')
        d_tokens_valid = tagged_valid_tokens.count('<country_name>')

        self.tokens_removed_a_count = a_tokens_train + a_tokens_test + a_tokens_valid
        self.tokens_removed_b_count = b_tokens_train + b_tokens_test + b_tokens_valid
        self.tokens_removed_c_count = c_tokens_train + c_tokens_test + c_tokens_valid
        self.tokens_removed_d_count = d_tokens_train + d_tokens_test + d_tokens_valid

        self.untagged_training_count = len(tagged_train_tokens) - a_tokens_train - b_tokens_train - c_tokens_train - d_tokens_train
        self.tagged_training_count = a_tokens_train + b_tokens_train + c_tokens_train + d_tokens_train
        self.untagged_testing_count = len(tagged_test_tokens) - a_tokens_test - b_tokens_test - c_tokens_test - d_tokens_test
        self.tagged_testing_count = a_tokens_test + b_tokens_test + c_tokens_test + d_tokens_test
        self.untagged_validation = len(tagged_valid_tokens) - a_tokens_valid - b_tokens_valid - c_tokens_valid - d_tokens_valid
        self.tagged_validation = a_tokens_valid + b_tokens_valid + c_tokens_valid + d_tokens_valid

        self.untagged_vocab_count = len(untagged_vocab)
        self.tagged_vocab_count = len(tagged_vocab)

    def __str__(self):
        s: str = "-- Assignment 1 Statistics --\n"

        s += "  Untagged training tokens:  %i\n" % self.untagged_training_count
        s += "  Tagged training tokens:    %i\n" % self.tagged_training_count
        s += "  Untagged testing tokens:   %i\n" % self.untagged_testing_count
        s += "  Tagged training tokens:    %i\n" % self.tagged_testing_count
        s += "  Untagged training tokens:  %i\n" % self.untagged_validation
        s += "  Tagged training tokens:    %i\n" % self.tagged_validation

        s += "  Untagged  vocab:           %i\n" % self.untagged_vocab_count
        s += "  Tagged  vocab:             %i\n" % self.tagged_vocab_count

        s += "  tokens removed for A:      %i\n" % self.tokens_removed_a_count
        s += "  tokens removed for B:      %i\n" % self.tokens_removed_b_count
        s += "  tokens removed for C:      %i\n" % self.tokens_removed_c_count
        s += "  tokens removed for D:      %i\n" % self.tokens_removed_d_count

        return s

# def assignment1_stats_summary():
#
#     # TODO: Sundar to add tagged stats
#
#     len_tokens_untagged_training = _len_pickle(Global.train_pickle_url)
#     len_tokens_tagged_training = _len_pickle(Global.tagged_train_pickle_url)
#     len_tokens_untagged_testing = _len_pickle(Global.test_pickle_url)
#     len_tokens_tagged_testing = _len_pickle(Global.tagged_test_pickle_url)
#     len_tokens_untagged_validation = _len_pickle(Global.valid_pickle_url)
#     len_tokens_tagged_validation = _len_pickle(Global.tagged_valid_pickle_url)
#
#
#     len_tokens_untagged_vocab = _len_pickle(Global.vocab_pickle_url)
#     len_tokens_tagged_vocab = _len_pickle(Global.tagged_vocab_pickle_url)
#
#
#     len_tokens_untagged_vdict = _len_pickle(Global.vocab_dict_pickle_url)
#     len_tokens_tagged_vdict = _len_pickle(Global.tagged_vocab_dict_pickle_url)
#
#     print("Untagged training tokens:  %i" % len_tokens_untagged_training)
#     print("Tagged training tokens:    %i" % len_tokens_tagged_training)
#     print("Untagged testing tokens:   %i" % len_tokens_untagged_testing)
#     print("Tagged training tokens:    %i" % len_tokens_tagged_testing)
#     print("Untagged training tokens:  %i" % len_tokens_untagged_validation)
#     print("Tagged training tokens:    %i" % len_tokens_tagged_validation)
#
#     print("Untagged  vocab:  %i" % len_tokens_untagged_vocab)
#     print("Tagged  vocab:    %i" % len_tokens_tagged_vocab)
#
#
#     print("Untagged  vocab dict:  %i" % len_tokens_untagged_vdict)
#     print("Tagged  vocab dict:    %i" % len_tokens_tagged_vdict)
#
#     len_tokens_removed_a = 0
#     len_tokens_removed_b = 0
#     len_tokens_removed_c = 0
#     len_tokens_removed_d = 0
#
#     print("Number of tokens removed for A: %i" % len_tokens_removed_a)
#     print("Number of tokens removed for B: %i" % len_tokens_removed_b)
#     print("Number of tokens removed for C: %i" % len_tokens_removed_c)
#     print("Number of tokens removed for D: %i" % len_tokens_removed_d)
#
#
# def _len_pickle(pickle_url: str) -> int:
#     f = open(pickle_url, 'rb')
#     p = pickle.load(f)
#     return len(p)
