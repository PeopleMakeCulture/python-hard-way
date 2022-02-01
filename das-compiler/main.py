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

test_func = 'def f(x, y) g(y,x) end'

token_list = Tokenizer(test_func).tokenize()
parse_tree = Parser(token_list).parse()

#This is the problem...
print("PARSE TREE", parse_tree)
print(type(parse_tree))
code = Generator(parse_tree).generate(parse_tree)

# testing
print(f"CODE: {code}")
