"""
May refactor and create Vocab class
"""
import pickle
import nltk
from constants import Global, DataManagement
from nltk.corpus import words

def create_vocab():
    """
    This function loads the train/valid/test tokens from the pickle files. It creates the vocabulary (unique tokens)
    based on the training set. It also creates the vocab_dict where the key is the token and the value is the
    index where the token appears in the vocab. E.g. vocab = ['cat', 'dog', ..] then vocab_dict = {'cat': 0, 'dog': 1}

    The function also replaces words from the validation and test sets that don't appear in the vocab with <unk>
    """
    # download English words
    # nltk.download('words')

    # read train tokens
    with open(Global.train_pickle_url, 'rb') as f:
        train_tokens = pickle.load(f)

    # not sure of a cheap way to check if words (if tok not in words.words() is quite expensive)
    vocab = list(set([tok for tok in train_tokens]))
    print('\nVOCAB:', vocab[:10])

    # vocab length is ~38,000 for now
    # print(len(vocab), vocab[:100])

    # read test and validation
    with open(Global.valid_pickle_url, 'rb') as f:
        valid_tokens = pickle.load(f)
    with open(Global.test_pickle_url, 'rb') as f:
        test_tokens = pickle.load(f)

    # replace out of vocab (OOV) words with <unk> in valid and test tokens
    print('\nReplacing OOV words with <unk>. This may take a minute or two...')
    for idx, tok in enumerate(valid_tokens):
        if tok not in vocab:
            valid_tokens[idx] = '<unk>'

    for idx, tok in enumerate(test_tokens):
        if tok not in vocab:
            test_tokens[idx] = '<unk>'

    print('\nVALID:', valid_tokens[:100])
    print('\nTEST:', test_tokens[:100])

    # add <unk> to the vocabulary
    vocab.append('<unk>')

    # create dictionary (might not need dict, could do vocab.index('cat') to get integer representations
    vocab_dict = {}
    for i, v in enumerate(vocab):
        vocab_dict[v] = i

    print('\nDICT:', dict(list(vocab_dict.items())[0:10]))

    # get integer representations
    print('\nCreating integer representations...')
    train_integer_untagged = create_integer_representations(train_tokens, vocab_dict)
    valid_integer_untagged = create_integer_representations(valid_tokens, vocab_dict)
    test_integer_untagged = create_integer_representations(test_tokens, vocab_dict)

    # TODO: Sundar add the "tagged" corpus to this (3 more calls)



    # write data
    DataManagement.save_vocab_data(vocab, vocab_dict)
    print('\nSaved vocab and integer representations to files.')

def create_integer_representations(token_list, vocab_dict):
    """
    This function creates 6 integers representations. For train/valid/test of untagged corpus and
    train/valid/test of tagged corpus. It uses the vocab_dict to do so.

    CURRENTLY: just does the representation for the untagged corpus

    Args:
        token_list (List): a list of words to be converted to integer using the vocab_dict

    Returns:
        integer_representation (List): a list of integers representing the original words
    """
    integer_representation = []
    for tok in token_list:
        integer_representation.append(vocab_dict[tok])

    return integer_representation