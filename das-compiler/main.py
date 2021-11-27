# What are capitalization conventions in Python?

from tokenize import *

# import fs

# import generator

# from generator import *

test_func = 'def f() 1 end'
test_func_2 = "99 end f() def"

# TRANS this Ruby into Python
# instantiate new obj of class Tokenizer
# it takes one arg(source_code)
# it has one func tokenize() that will tokenize source code
# also need to pass in the source code && call "read"
# tokens = Tokenizer.new(file.read('test.src')).tokenize()

# for testing
func_1_tokens = Tokenizer(test_func).tokenize()

print(f"Function has {len(func_1_tokens)} tokens")
# func_2_tokens = Tokenizer(test_func_2).tokenize()
