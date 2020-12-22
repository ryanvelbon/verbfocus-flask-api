import nltk

f = open("cisemayaz.txt", "r", encoding="utf8")

text = f.read().lower()

tokens = nltk.word_tokenize(text)

len(tokens)

vocab = nltk.tokenize.word_tokenize(text)

fd = nltk.FreqDist(vocab)

for item in fd:
    print(item)