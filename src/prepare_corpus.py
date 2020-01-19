import nltk
from constants import Global, DataManagement
from nltk.tokenize import sent_tokenize
import re

#class PrepareCorpus():



def load_raw_data():

    # required
    nltk.download('punkt')

    # read raw text
    with open(Global.raw_text_url) as f:
        i = 0

        # iterate thru lines of raw text
        for line in f:
            if line:
                sentences = nltk.sent_tokenize(line)  # nltk not perfect here, makes some mistakes
                if sentences:

                    #print('SENTENCES:', sentences)
                    for idx, sentence in enumerate(sentences):
                        # remove appearances of [#] (wikipedia sources)
                        sentences[idx] = re.sub(r"\[[0-9]+\]", '', sentences[idx])

                        #print('SENTENCE: ', sentences[idx])

                        # append to begin and end of sentences
                        if sentences[idx] and not sentences[idx].isspace():
                            if sentences[idx][0] == ' ':
                                sentences[idx] = '<s>' + sentences[idx]
                            else:
                                sentences[idx] = '<s> ' + sentences[idx]

                            sentences[idx] += ' </s> '

                            print('\n\nSENTENCE:', sentences[idx])

                            print('TOKENS: ', nltk.word_tokenize(sentences[idx] + sentences[idx-1]))

            i += 1
            if i == 10:
                break

    f.close()

load_raw_data()