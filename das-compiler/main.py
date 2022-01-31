# What are capitalization conventions in Python?

from parser import *
from tokenize import *

from generator import *

test_func = 'def f(x, y) g(x) end'

token_list = Tokenizer(test_func).tokenize()

# TODO: uncomment the parse function
# AND the Generator when Parser is done
parse_tree = Parser(token_list)  # .parse()

# code = Generator.generate(parse_tree)

# for testing
# print(token_list)
# print("token_list is a ", type(token_list))
print("Testing Part 2: Parser")
# print("parse_tree is a ", type(parse_tree))
print(parse_tree.parse())
