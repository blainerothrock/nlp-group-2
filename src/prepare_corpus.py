import re
import nltk
from nltk.tokenize import RegexpTokenizer, WordPunctTokenizer
from constants import Global, DataManagement
import time
import pycountry


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
        self.tagged_tokens = []
        self.tagged_train_tokens = []
        self.tagged_valid_tokens = []
        self.tagged_test_tokens = []
        self.num_train = 0
        self.num_valid = 0
        self.num_test = 0
        self.count = 0

    def load_and_clean(self):
        """
        This function loads the raw text, tokenizes using RegexpTokenizer which removes
        punctuation and things like wikipedia sources in brackets, e.g. [7]. It converts
        words to lowercase and adds <s> and </s> to dilineate the beginning of sentences.

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
                            #sentence = re.sub(r"\[[0-9]+\]", '', sentence)

                            if sentence and not sentence.isspace():
                                sentence = sentence.lower()

                                # create tokens and remove punctuation
                                # tokenizer = RegexpTokenizer(r'\w+')
                                # sentence_tokens = tokenizer.tokenize(sentence)
                                tokenizer = WordPunctTokenizer()
                                sentence_tokens = tokenizer.tokenize(sentence)

                                # append <s> and </s> to begin and end of sentences
                                sentence_tokens.insert(0, '<s>')
                                sentence_tokens.append('</s>')
                                self.tokens += sentence_tokens


        # remove one letter words that are not 'a', 'i'
        for idx, tok in enumerate(self.tokens):
            if len(tok) <= 1 and not tok.isalnum() and tok not in ['a', 'i']:
                del self.tokens[idx]

        # remove tokens with freq < vocab_freq_threshold
        tok_freq = {}
        for tok in self.tokens:
            tok_freq[tok] = self.tokens.count(tok)

        self.tokens = [tok for tok in filter(lambda x: tok_freq[x] >= Global.vocab_freq_threshold, self.tokens)]

        country_list = []
        for x in pycountry.countries:
            country_list.append(x.name)

        tagged_tokens = self.tokens
        # tag tokens for year, real number, month name, country name
        for idx, tok in enumerate(tagged_tokens):
            if re.match(r'.*([1-3][0-9]{3})', tok) is not None:
                tagged_tokens[idx] = '<year>'
            elif re.match(r'.*([0-9]\.?[0-9]?)', tok) is not None:
                tagged_tokens[idx] = '<realnumber>'
            if re.match(
                    r'.*(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|(Nov|Dec)(?:ember)?)',
                    tok, re.IGNORECASE) is not None:
                tagged_tokens[idx] = '<month>'
            if tok.casefold() in (name.casefold() for name in country_list):
                tagged_tokens[idx] = '<country_name>'

        self.tagged_tokens = tagged_tokens
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

        self.tagged_train_tokens = self.tagged_tokens[:self.num_train]

        # store valid
        self.num_valid = (self.count - self.num_train) // 2
        self.valid_tokens = self.tokens[self.num_train:(self.num_train+self.num_valid)]

        self.tagged_valid_tokens = self.tokens[self.num_train:(self.num_train+self.num_valid)]

        # store test
        self.num_test = self.count - (self.num_train+self.num_valid)
        self.test_tokens = self.tokens[(self.num_train+self.num_valid):]

        self.tagged_test_tokens = self.tokens[(self.num_train+self.num_valid):]

        assert(self.num_train + self.num_valid + self.num_test == self.count)

        # combine the tokens into one large string and write to file
        print('\nWriting to files...')
        DataManagement.write_train_valid_test(self.train_tokens, self.valid_tokens, self.test_tokens)
        DataManagement.write_tagged_train_valid_test(self.tagged_train_tokens, self.tagged_valid_tokens, self.tagged_test_tokens)
        print('\nDone.')


# def test():
#     c = Corpus()
#
#     c.load_and_clean()
#
#     print(c.tokens[:500])
#
# test()

