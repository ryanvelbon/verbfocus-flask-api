import pytest
import os

from pkgs.lang.wikt import exists

def test_exists():
	
	assert exists("cinta", "Catalan") == True
	assert exists("cinta", "Galician") == True
	assert exists("cinta", "Indonesian") == True
	assert exists("cinta", "Italian") == True
	assert exists("cinta", "Malay") == True
	assert exists("cinta", "Portuguese") == True
	assert exists("cinta", "Spanish") == True

	assert exists("cinta", "German") == False
	assert exists("cinta", "French") == False
	

if __name__ == "__main__":
	test_exists()
	print("Everything passed")