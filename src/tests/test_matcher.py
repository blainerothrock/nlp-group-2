import sys
sys.path.append('..')
from matcher import match_replace, match_stop_words, match_replace_dict


def test_matcher():
    vocabList = ['hi', 'hello', 'this', 'that', 'is', 'of', 'the', '2000', '2100', '1800']
    _modifiedList_ = match_replace(vocabList)
    print(_modifiedList_)

def test_stop_words():
    vocabList = ['hi', 'hello', 'this', 'that', 'is', 'of', 'the', '2000', '2100', '1800']
    _modifiedList_ = match_stop_words(vocabList)
    print(_modifiedList_)
