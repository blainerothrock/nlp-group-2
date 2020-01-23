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
