import re
import nltk
from constants import Global, DataManagement
import time


class Corpus():
    """
    This class represents the Corpus for the project.
    """
    def __init__(self):
        # stores all the tokens from the text
        self.tokens = []
        self.train_tokens = []
        self.valid_tokens = []
        self.test_tokens = []
        self.num_train = 0
        self.num_valid = 0
        self.num_test = 0
        self.count = 0

    def load_and_clean(self):
        """
        This function loads the raw text, removes occurrences of [#], delineates sentences
        using <s> and </s> and tokenizes the text.

        """
        # required
        nltk.download('punkt')

        print('\nStarting cleaning and tokenizing (should take <1 min)...')
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

        # close raw data file and report
        f.close()
        self.count = len(self.tokens)
        end = time.time()
        print('\nCleaning and tokenizing took', round(end-start, 2), ' seconds.')


    def train_valid_test_split(self):
        """
        Splits the tokens into train/valid/test sets based on train_percent (default is 90% or .9).
        The remaining tokens are split evenly into validation and test sets.

        """
        print('\nSplitting train and test data...')
        # store training tokens
        self.num_train = int(Global.train_percent * self.count)

        # probably best to cut it off at end a sentence (when we see </s>)
        end_of_sentence = False
        while not end_of_sentence:
            if self.tokens[self.num_train-1] != '</s>':
                self.num_train += 1
            else:
                end_of_sentence = True

        self.train_tokens = self.tokens[:self.num_train]

        # store valid
        self.num_valid = (self.count - self.num_train) // 2
        self.valid_tokens = self.tokens[self.num_train:(self.num_train+self.num_valid)]

        # store test
        self.num_test = self.count - (self.num_train+self.num_valid)
        self.test_tokens = self.tokens[(self.num_train+self.num_valid):]

        assert(self.num_train + self.num_valid + self.num_test == self.count)

        # combine the tokens into one large string and write to file
        print('\nWriting to files...')
        DataManagement.write_train_valid_test(" ".join(self.train_tokens), \
                                              " ".join(self.valid_tokens), \
                                              " ".join(self.test_tokens))
        print('\nDone.')