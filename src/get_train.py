from nltk import word_tokenize

PATH = 'data/group2.train.txt'

def get_train():
	f = open(PATH,'rU')
	raw = f.read()
	tokens = word_tokenize(raw)
	words = [w.lower() for w in tokens]
	words = list(set(words))

	return words