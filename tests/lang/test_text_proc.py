import pytest
import os

from pkgs.lang.text_proc import fix_casing, fix_punctuation, fix_spacing, fix_syntax, validate_syntax, validate_chars



def test_fix_casing():

	items = [
		("this sentence should start with an uppercase letter", "This sentence should start with an uppercase letter"),
		("hello. how are you?", "Hello. How are you?"),
		("there is ... no time", "There is ... no time"),
		("There is ... No time", "There is ... no time"),

	]

	for item in items:
		assert fix_casing(item[0]) == item[1]


def test_fix_punctuation():
	pass


def test_fix_spacing():

	items = [
		("This   has  extra  whitespace     all  over", "This has extra whitespace all over"),
		("  This starts with whitespace.", "This starts with whitespace."),
		("This ends with whitespace        ", "This ends with whitespace"),
	]

	for item in items:
		assert fix_spacing(item[0]) == item[1], "'{}' should have been processed into '{}'".format(item[0], item[1])

def test_fix_syntax():

	items = [
		("this     sentence has MANY mistakes", "This sentence has many mistakes."),
		("", ""),
		("", ""),
	]

	for item in items:
		assert fix_syntax(item[0]) == item[1], "'{}' should have been processed into '{}'".format(item[0], item[1])



if __name__ == "__main__":
	# test_fix_casing()
	# test_fix_punctuation()
	test_fix_spacing()
	# test_fix_syntax()
	# test_validate_syntax()
	# test_validate_chars()
	print("Everything passed")	