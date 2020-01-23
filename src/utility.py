import pickle
from constants import Global, DataManagement
from typing import *


def assignment1_stats_summary():

    # TODO: Sundar to add tagged stats

    len_tokens_untagged_training = _len_pickle(Global.train_pickle_url)
    len_tokens_tagged_training = _len_pickle(Global.tagged_train_pickle_url)
    len_tokens_untagged_testing = _len_pickle(Global.test_pickle_url)
    len_tokens_tagged_testing = _len_pickle(Global.tagged_test_pickle_url)
    len_tokens_untagged_validation = _len_pickle(Global.valid_pickle_url)
    len_tokens_tagged_validation = _len_pickle(Global.tagged_valid_pickle_url)


    len_tokens_untagged_vocab = _len_pickle(Global.vocab_pickle_url)
    len_tokens_tagged_vocab = _len_pickle(Global.tagged_vocab_pickle_url)


    len_tokens_untagged_vdict = _len_pickle(Global.vocab_dict_pickle_url)
    len_tokens_tagged_vdict = _len_pickle(Global.tagged_vocab_dict_pickle_url)

    print("Untagged training tokens:  %i" % len_tokens_untagged_training)
    print("Tagged training tokens:    %i" % len_tokens_tagged_training)
    print("Untagged testing tokens:   %i" % len_tokens_untagged_testing)
    print("Tagged training tokens:    %i" % len_tokens_tagged_testing)
    print("Untagged training tokens:  %i" % len_tokens_untagged_validation)
    print("Tagged training tokens:    %i" % len_tokens_tagged_validation)

    print("Untagged  vocab:  %i" % len_tokens_untagged_vocab)
    print("Tagged  vocab:    %i" % len_tokens_tagged_vocab)


    print("Untagged  vocab dict:  %i" % len_tokens_untagged_vdict)
    print("Tagged  vocab dict:    %i" % len_tokens_tagged_vdict)

    len_tokens_removed_a = 0
    len_tokens_removed_b = 0
    len_tokens_removed_c = 0
    len_tokens_removed_d = 0

    print("Number of tokens removed for A: %i" % len_tokens_removed_a)
    print("Number of tokens removed for B: %i" % len_tokens_removed_b)
    print("Number of tokens removed for C: %i" % len_tokens_removed_c)
    print("Number of tokens removed for D: %i" % len_tokens_removed_d)


def _len_pickle(pickle_url: str) -> int:
    f = open(pickle_url, 'rb')
    p = pickle.load(f)
    return len(p)
