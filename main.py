from nltk.tokenize import sent_tokenize, word_tokenize
import nltk

sagan_quote = "Hello, my friend, how are you?"

words_in_sagan_quote = word_tokenize(sagan_quote)
print(nltk.pos_tag(words_in_sagan_quote))