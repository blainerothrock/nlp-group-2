from nltk import word_tokenize

PATH = 'data/group2.test.txt'

def get_test():
	f = open(PATH,'rU')
	raw = f.read()
	tokens = word_tokenize(raw)
	words = set([w.lower() for w in tokens])

	return words


