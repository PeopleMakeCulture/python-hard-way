# takes in a list of Tokens
# puts out a tree of Nodes

# from tokenize import Token # is this necessary?

# Def nodes are function defs
class DefNode(object):
    def __init__(self, name, args, body):
        self.name = name
        self.args = args
        self.body = body


# Good Ol' Ints
class IntegerNode(object):
    def __init__(self, value):
        self.value = value


# Call nodes represent just the function call
class CallNode(object):
    def __init__(self, name, arg_exprs):
        self.name = name
        self.arg_exprs = arg_exprs


# Just a var
class VarRefNode(object):
    def __init__(self, name):
        self.name = name


# Main
class Parser(object):
    def __init__(self, token_list):
        self.token_list = token_list

    def peek(self, expected_type, offset=0):
        return self.token_list[offset].type == expected_type

    # Python doesn't have a list shift method
    def consume(self, expected_type):
        # this should do the same thing as `.shift()`
        current_token = self.token_list[0]
        token_list = self.token_list[1:]

        if current_token.type == expected_type:
            return current_token
        else:
            # print(f"Exoected token type {expected_type} but got {current_token.type}")
            # better error handling
            raise RuntimeError(f"Exoected token type {expected_type} but got {current_token.type}")

    # returns parse tree
    def parse(self):
        # print(self.token_list)
        # for token in token_list:
        #     print(f"token_value: {token.value} AND token_type: {token.type}")
        while self.token_list:
            if self.peek('def'): # if next token is def
                yield self.parse_def() # are we sure yield > return?
            else:
                yield self.parse_call()


    # don't remember what this does
    def parse_def(self):


    def parse_arg_names(self, arg_names):
        pass

    def parse_expr(self):
        pass

    def parse_int(self):
        # am I constructing node types? I think YES
        # do I return this?
        IntegerNode(value)  # cast as python int

    def parse_call(self):
        CallNode(value, exprs)

    def parse_var_ref(self):
        VarRefNode(name)
