# Input: list of Tokens
# Ouput: a tree of Nodes

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

    # destructively returns next token (eg "token_list[0]")
    # NOTE: Python doesn't have a list shift method
    def consume(self, expected_type):
        # this does the same thing as `.shift()`
        current_token = self.token_list[0]
        self.token_list = self.token_list[1:]
        if current_token.type == expected_type:
            return current_token
        else:
            # print(f"Exoected token type {expected_type} but got {current_token.type}")
            # better error handling
            raise RuntimeError(f"Expected token type {expected_type} but got {current_token.type}")

    #TODO: this was just for testing -can remove later
    def print_token_list(self):
        print("TOKEN LIST: ")
        for token in self.token_list:
            print(f"token_value: {token.value} AND token_type: {token.type}")

    # returns parse tree
    def parse(self):
        parse_tree = self.parse_def()
        # print(parse_tree)
        return parse_tree
        #TODOLATER: can we add more logic here to differetiate parse def vs parse function call?

    # called by parse
    # returns a DefNode
    def parse_def(self):
        self.consume('def')

        name = self.consume('identifier').value # name of function
        arg_names = self.parse_arg_names()
        body = self.parse_expr()

        self.consume('end')

        new_def_node = DefNode(name, arg_names, body)
        return new_def_node


    # called by parse_def
    # returns list of an arbitrary # of arg names
        """
        # after consuming oparen, keep consuming identifiers and commas
        # after last comma and identifier, consume cparens
        """
    def parse_arg_names(self):

        self.consume('oparen')

        arg_names = []
        if self.peek('identifier'):
            arg_names.append(self.consume('identifier').value)
            while self.peek('comma'):
                self.consume('comma')
                arg_names.append(self.consume('identifier').value)

        self.consume('cparen')
        return arg_names

    # called by parse_def
    # recursively returns sub-tree of nodes to represent function expression
    def parse_expr(self):
        if self.peek('integer'):
            return self.parse_int() # simplest case for now
        elif self.peek('identifier') and self.peek('oparen', 1):
            return self.parse_function_call()
        else:
            return self.parse_var_ref() # HUH?

############################################################
# TODO: PARSE FUNCTION CALL

    # called in parse_expr
    def parse_function_call(self):

        name = self.consume('identifier').value
        arg_exprs = self.parse_arg_exprs()

        return CallNode(name, arg_exprs)

    # like parse_arg_names EXCEPT instead of building list of token values
    # we build a list of sub-trees of nodes
    def parse_arg_exprs(self):
        arg_exprs = []

        self.consume('oparen')

        if not self.peek('cparen'):
            arg_exprs.append(self.parse_expr())

            while(self.peek('comma')):
                self.consume('comma');
                arg_exprs.append(self.parse_expr())

        self.consume('cparen')

        return arg_exprs

############################################################

    def parse_int(self):
        new_int_node = IntegerNode(int(self.consume('integer').value))
        return new_int_node

    def parse_var_ref(self):
        name = self.consume('identifier').value
        return VarRefNode(name)
