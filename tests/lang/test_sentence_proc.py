import pytest
import os

from pkgs.lang.sentence_proc import sentences_count


def test_sentences_count():
	
	filepath = os.path.join(os.path.dirname(__file__), 'dummy-data/id_sentences.txt')
	f = open(filepath, 'r')
	assert sentences_count(f) == 200


if __name__ == "__main__":
	test_sentences_count()
	print("Everything passed")