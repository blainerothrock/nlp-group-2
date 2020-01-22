import pickle
from constants import Global, DataManagement
from typing import *


def assignment1_stats_summary():

    # TODO: Sundar to add tagged stats

    len_tokens_untagged_training = _len_pickle(Global.train_pickle_url)
    len_tokens_tagged_training = 0
    len_tokens_untagged_testing = _len_pickle(Global.test_pickle_url)
    len_tokens_tagged_testing = 0
    len_tokens_untagged_validation = _len_pickle(Global.valid_pickle_url)
    len_tokens_tagged_validation = 0

    print("Untagged training tokens:  %i" % len_tokens_untagged_training)
    print("Tagged training tokens:    %i" % len_tokens_tagged_training)
    print("Untagged testing tokens:   %i" % len_tokens_untagged_testing)
    print("Tagged training tokens:    %i" % len_tokens_tagged_testing)
    print("Untagged training tokens:  %i" % len_tokens_untagged_validation)
    print("Tagged training tokens:    %i" % len_tokens_tagged_validation)

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
