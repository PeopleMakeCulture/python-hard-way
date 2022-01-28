# takes in a string-ified function
# puts out a list of Tokens, each with type and value

import re

# TODOLATER: instead of using a new class/object,
# could I use a better data structure (eg named tuple)?

# use a list of tuples
# tuples are immutable strings
# only Tokenizer needs access
TOKEN_TYPES = [('def', r'\bdef\b'), ('end', r'\bend\b'),
               ('identifier', r'\b[a-zA-z]+\b'), ('integer', r'\b[0-9]+\b'),
               ('oparen', r'\('), ('cparen', r'\)'), ('comma', r',')]


# Tokens each have type and value
class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Tokenizer(object):

    def __init__(self, input_code):

        self.input_code = input_code
        self.tokens = []

    def tokenize(self):

        while self.input_code:

            self.tokenize_one_token()

        # FOR TESTING
        # for token in self.tokens:
        #     print(f"token_value: {token.value} AND token_type: {token.type}")

        return self.tokens

    def tokenize_one_token(self):
        # iternate over all token types
        for token_type, token_regex in TOKEN_TYPES:

            # see if token type matches start of code
            match = re.match(token_regex, self.input_code)

            if match:
                token_value = match.group()
                # create a token with value of regex
                new_token = Token(token_type, token_value)
                # and add it to self.tokens
                self.tokens.append(new_token)
                # shift the token off of the input
                self.input_code = self.input_code[len(token_value):].strip()
                # need to exit to return to start of token list for next token
                return

        # also handle errors
        # Q: What is this doing??
        raise RuntimeError(f"Couldn't match token at start{self.input_code!r}stop")
