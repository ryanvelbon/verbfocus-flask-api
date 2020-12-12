
import nltk
from pkgs.lang.text_proc import get_vocab


def stats(txtfile):

	full_text = txtfile.read()
	lines = txtfile.readlines()
	vocab = get_vocab(full_text)

	print(vocab)

	# print("Character count   :  {}".format())
	# print("Word count   :  {}".format())
	# print("Total sentences           :  {}".format(len(lines)))
	print("Vocab (total unique words):  {}".format(len(vocab)))
	# print("Average line length   :  {}".format())

