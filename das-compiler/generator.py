# Input: a tree of nodes
# Output: JavaScript code as a string

class Generator(object):
    # is init necessary??
    # I do call self.generate...
    # def __init__(self):
    #     pass

    def generate(self, node):
        # Def Node
        if type(node).__name__ == 'DefNode':

            def_function_name = node.name
            def_arg_names = ','.join(node.args)
            body = self.generate(node.body) # recursively generate code
            return "function {name}({args}){\nreturn {body};\n}".format(name=def_function_name, args=def_arg_names, body=body)
            # TODO: there's a cleaner way to format string

        # Call Node
        elif type(node).__name__ == 'CallNode':
            call_arg_names = node.arg_exprs # what is this a list? string?
            # recursively generate code
            call_function_name = node.name
            code = "{name} {args}".format(name=call_function_name, args=call_arg_names)
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
