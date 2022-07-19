"""This function will break up words for us."""
def break_words(stuff):
	words = stuff.split(' ')
	return words

def sort_words(words):
	return sorted(words)

def print_first_word(words):
	print(words.pop(0))

def print_last_word(words):
	print(words.pop(-1))

"""Sorts the words and then prints the first and last one"""
def print_first_and_last_sorted(sentence):
	words = sort_words(sentence)
	print_first_word(words)
	print_last_word(words)

