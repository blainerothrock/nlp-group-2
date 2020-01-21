from nltk import word_tokenize

PATH = 'data/group2.valid.txt'

def get_valid():
	f = open(PATH,'rU')
	raw = f.read()
	tokens = word_tokenize(raw)
	words = [w.lower() for w in tokens]
	words = list(set(words))

	return words