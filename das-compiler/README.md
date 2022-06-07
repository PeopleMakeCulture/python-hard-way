An work-in-progress (WIP) implementation of Destroy All Software's toy compiler in Python instead of Ruby. 

This program takes a single function definition in a Ruby-ish toy language and compiles it into Javascript.

The compiler runs the input code through three parts:

    Tokenizer => Parser => Generator

* a _Tokenizer_ that takes in a string of code in a toy language and outputs a list of Tokens, each with type and value. Each Token represents the smallest unit of meaning in the input language (eg "def", "end", "comma").

* a _Parser_ that takes in a list of Tokens and outputs a tree of Nodes. Each Node represents the smallest unit of meaning in the input code.

* a _Generator_ that takes in a tree of Nodes and outputs a string of compiled JavaScript code.

For the original screencast see: https://www.destroyallsoftware.com/screencasts/catalog/a-compiler-from-scratch. 

## Getting Started

To get started:
1. clone this repository onto your local machine
2. cd into the repository
3. run `python3 main.py`

## Recurse TODOS:

### Tokenize
Relatively bug-free and working as expected

### Parser

*Task1*: Debug `parse_function_call` in parser.py

### Generator
*Task*: Debug CallNode generator

### Main
*Task*: Refactor script to take input code as an xarg



