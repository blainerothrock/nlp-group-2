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
    vocab = set([tok for tok in train_tokens])

    print('\nVOCAB:', list(vocab)[:10])

    # vocab length is ~38,000 for now
    # print(len(vocab), vocab[:100])

    # read test and validation
    with open(Global.valid_pickle_url, 'rb') as f:
        valid_tokens = pickle.load(f)
    with open(Global.test_pickle_url, 'rb') as f:
        test_tokens = pickle.load(f)

    # replace out of vocab (OOV) words with <unk> in valid and test tokens
    print('\nReplacing OOV words with <unk>. This may take a minute or two...')

    test_tokens = [tok if tok in vocab else '<unk>' for tok in test_tokens]
    valid_tokens = [tok if tok in vocab else '<unk>' for tok in valid_tokens]

    print('\nVALID:', list(valid_tokens)[:100])
    print('\nTEST:', list(test_tokens)[:100])

    vocab.add('<unk>')

    # create dictionary (might not need dict, could do vocab.index('cat') to get integer representations
    vocab_dict = {}
    for i, v in enumerate(vocab):
        vocab_dict[v] = i

    print('\nDICT:', dict(list(vocab_dict.items())[0:10]))

    with open(Global.tagged_train_pickle_url, 'rb') as f:
        tagged_train_tokens = pickle.load(f)
    with open(Global.tagged_valid_pickle_url, 'rb') as f:
        tagged_valid_tokens = pickle.load(f)
    with open(Global.tagged_test_pickle_url, 'rb') as f:
        tagged_test_tokens = pickle.load(f)

    tagged_vocab = set([tok for tok in tagged_train_tokens])

    tagged_valid_tokens = [tok if tok in tagged_vocab else '<unk>' for tok in tagged_valid_tokens]
    tagged_test_tokens = [tok if tok in tagged_vocab else '<unk>' for tok in tagged_test_tokens]

    # add <unk> to the vocabulary
    tagged_vocab.add('<unk>')
    tagged_vocab.add('<year>')
    tagged_vocab.add('<month>')
    tagged_vocab.add('<country_name>')
    tagged_vocab.add('<realnumber>')

    # create tagged dictionary (might not need dict, could do vocab.index('cat') to get integer representations
    tagged_vocab_dict = {}
    for i, v in enumerate(list(tagged_vocab)):
        tagged_vocab_dict[v] = i

    # get integer representations
    print('\nCreating integer representations...')
    train_integer_untagged = create_integer_representations(train_tokens, vocab_dict)
    valid_integer_untagged = create_integer_representations(valid_tokens, vocab_dict)
    test_integer_untagged = create_integer_representations(test_tokens, vocab_dict)
    # TODO: Sundar add the "tagged" corpus to this (3 more calls)
    train_integer_tagged = create_integer_representations(tagged_train_tokens, tagged_vocab_dict)
    valid_integer_tagged = create_integer_representations(tagged_valid_tokens, tagged_vocab_dict)
    test_integer_tagged = create_integer_representations(tagged_test_tokens, tagged_vocab_dict)

    # write data
    DataManagement.save_vocab_data(vocab, vocab_dict)
    DataManagement.save_tagged_vocab_data(tagged_vocab, tagged_vocab_dict)
    DataManagement.save_integer_represented_vocab_data(train_integer_untagged, valid_integer_untagged, test_integer_untagged, train_integer_tagged, valid_integer_tagged, test_integer_tagged)
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