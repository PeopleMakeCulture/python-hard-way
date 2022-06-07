# What are capitalization conventions in Python?
"""
USAGE:
    Input: test_func in toy language =>
    Tokenizer => Parser => Generator =>
    Output: JS Code
"""

from parser import *
from tokenize import *

from generator import *

# NOTE: test_func is hard coded for now
# This repo also contains a test.src file

#TODO: update program to take one xarg--the name of a
# source file with a function to compile
test_func = 'def f(x, y) g(y,x) end'

token_list = Tokenizer(test_func).tokenize()
parse_tree = Parser(token_list).parse()

#This is the problem...
#TODO: Fix parse tree
print("PARSE TREE", parse_tree)
print(type(parse_tree))


code = Generator(parse_tree).generate(parse_tree)

# testing
print(f"CODE: {code}")
