# Input: a tree of nodes
# Output: JavaScript code as a string

class Generator(object):
    # is init necessary??
    def __init__(self, parse_tree):
        self.parse_tree = parse_tree # why tho?

    # should we make this a static method?
    # @staticmethod
    def generate(self, node):
        # testing
        print("IN GENERATE")
        print("NODE TYPE", type(node).__name__)

        # Def Node
        # Compile basic structure of JS func with name, args, body
        if type(node).__name__ == 'DefNode':

            def_function_name = node.name
            def_arg_names = ','.join(node.args)
            body = self.generate(node.body) # recursively generate code
            # TODO: find a cleaner way to format string
            code = "function {name}({args}) {{ \n return {body};\n}}".format(name=def_function_name, args=def_arg_names, body=body)
            return code

        # Call Node
        # Compile
        elif type(node).__name__ == 'CallNode':
            call_function_name = node.name
            #TODO: Debug this -- we should output the arg names, NOT the nodes!
            """
                # recursively generate code
                # from list of nodes => list of names
                # create a list of arg names
                # for each expr in arg exprs
                # recursively generate code (self.generate(arg_expr))
                # join list with comma
            """
            # take arg_exprs and recursively return JS syntax for arg_exprs
            call_arg_exprs = ",".join(map(self.generate, node.arg_exprs))
            code = "{name}({args})".format(name=call_function_name, args=call_arg_exprs)
            return code

        # Int Node
        elif type(node).__name__ == 'IntegerNode':
            return node.value

        # Var Ref Node
        elif type(node).__name__ == 'VarRefNode':
            return node.name

        # Error Handling
        else:
            raise RuntimeError(f'Unexpected node type: {type(node).__name__} {node.value}')
