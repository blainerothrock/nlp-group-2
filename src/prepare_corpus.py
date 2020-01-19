import re
import nltk
from constants import Global
import time


class Corpus():
    """
    This class represents the Corpus for the project.
    """
    def __init__(self):
        # stores all the tokens from the text
        self.tokens = []
        self.count = 0

    def load_and_clean(self, test=False, subset=10):
        """
        This function loads the raw text, removes occurrences of [#], delineates sentences
        using <s> and </s> and tokenizes the text.

        Args:
            test (bool): whether to test the function or not
            subset (int): how many lines to view in the test

        Returns:

        """

        # required
        nltk.download('punkt')

        print('\nStarting cleaning and tokenizing...')
        start = time.time()

        # read raw text
        with open(Global.raw_text_url) as f:
            i = 0

            # iterate thru lines of raw text
            for line in f:
                if line:
                    sentences = nltk.sent_tokenize(line)  # nltk not perfect here, makes some mistakes
                    if sentences:
                        for idx, sentence in enumerate(sentences):
                            # remove appearances of [#] (wikipedia sources)
                            sentence = re.sub(r"\[[0-9]+\]", '', sentence)

                            if sentence and not sentence.isspace():
                                sentence_tokens = nltk.word_tokenize(sentence)

                                # append <s> and </s> to begin and end of sentences
                                sentence_tokens.insert(0, '<s>')
                                sentence_tokens.append('</s>')

                                self.tokens += sentence_tokens

                # TODO: remove this block eventually
                i += 1
                if test:
                    if i == subset:
                        print('TOKENS:', self.tokens)
                        break

        # close raw data file and report
        f.close()
        self.count = len(self.tokens)
        end = time.time()
        print('\nCleaning and tokenizing took ', round((end-start)/60, 4), ' minutes.')


    def train_valid_test_split(self):


"""
Run this file to test the Corpus code with a subset of data

TODO: remove this block eventually
"""
def test():
    c = Corpus()

    c.load_and_clean(test=True)


test()