import re
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))


def match_replace(vocabList):
    """
      This function uses regex pattern matching to identify selected key words and tags them in the
      list that was passes in.

        Iterate over the list using for loop and check for year
    """

    for word in vocabList:
        match = re.match(r'.*([1-3][0-9]{3})', word)
        if match is not None:
            print(match)

    for i, v in enumerate(vocabList):
        match = re.match(r'.*([1-3][0-9]{3})', v)
        if match is not None:
            vocabList[i] = vocabList[i] + ' <YEAR>'

    return vocabList


def match_replace_dict(wordDict):
    """
      This function uses regex pattern matching to identify selected key words and tags them in the
      dictionary that was passes in.

        Iterate over the list using for loop and check for year
    """

    for key in wordDict:
        match = re.match(r'.*([1-3][0-9]{3})', key)
        print(match)

    return wordDict


def match_stop_words(vocabList):
    """
      This function uses regex pattern matching to identify stop words and tags them in the
      list that was passes in.

      Iterate over the list using for loop and check for stop words and modify the list value to
      format -->  Word + <STOP WORD>

    """

    for i, v in enumerate(vocabList):
        if v in stop_words:
            vocabList[i] = vocabList[i] + ' <STOP WORD>'

    return vocabList
