# takes a string
# splits into list of tokens
# each token is a struct
# has a type and value

# import re
# required to use r'' syntax?

class Tokenizer:
    pass

# use a list of tuples
# tuples are immutable strings
# ALT: consider named tuples
# or obj {name: "", regex://}
# Q: for regex can I use // syntax

TOKEN_TYPES = [
('comma', /,/)
]

# ('def', //),
# ('end', //),
# ('identifier', //),
# ('integer', //),
# ('oparen', //,
# ('cparen', //),
