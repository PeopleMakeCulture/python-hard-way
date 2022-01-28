# What are capitalization conventions in Python?

# import fs

from parser import *
from tokenize import *

# from generator import *

test_func = 'def f() 1 end'
test_func_2 = "99 end f() def"

token_list = Tokenizer(test_func).tokenize()

parse_tree = Parser(token_list).parse()

# for testing
# print("Testing Part 2: Parser")
print(parse_tree)
