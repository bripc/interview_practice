'''
Lisp parser

Write code that takes some Lisp code and returns an abstract syntax tree. The AST should represent the structure of the
code and the meaning of each token. For example, if your code is given "(first (list 1 (+ 2 3) 9))", it could return a
nested array like ["first", ["list", 1, ["+", 2, 3], 9]].

During your interview, you will pair on writing an interpreter to run the AST. You can start by implementing a single
built-in function (for example, +) and add more if you have time.
'''

'''
Lisp is made up of lists and atoms.
Atoms:
- numbers;   including decimals (.), fractions (/), positive/negative (+/-), or exponents (e)
- strings;   backslashes (\) are escaped characters as usual
- names;     any characters, can start with numbers, can contain periods but can't be entirely periods, reserved characters
             can be in names if they are escaped
- reserved;  ()"'`,:;\|

All unescaped characters will be turned into uppercase
|foo| is foo, as is \f\o\o
'''

import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='Options for creating an abstract syntax tree from a .lisp file.')
    parser.add_argument('filename', help='.lisp file to interpret')
    return parser.parse_args()


# return the symbol as a string, or as a number if it is one
def atomize(symbol):
    try:
        return int(symbol)
    except ValueError:
        try:
            float(symbol)
        except ValueError:
            return symbol


# tokenize takes a string of valid lisp and turns it into an array of tokens
# it returns a nested list structure of all the tokens
def tokenize(lisp):
    # lexical analysis - break string into tokens
    if not isinstance(lisp, list):
        # makes it so that the string is easy to split on whitespace by padding parens with spaces
        lisp = lisp.replace('(', ' ( ').replace(')', ' ) ').split()

    # syntactic analysis - assemble into tree

    # look at the first token, take it out of the lisp list as a recursive end condition
    token = lisp.pop(0)
    print('DEBUG: token | lisp:', token, '|', lisp)
    # is it the beginning of a new statement?
    if token == '(':
        # if so, create a new list to store the expression in
        new_expression = []

        # keep iterating through the tokens until the end of the current expression is found
        while lisp[0] != ')':
            # if the end of the expression is found, go deeper...
            # append the future nested structures to this outer list
            # lisp currently is the rest of the lisp code that hasn't been parsed
            new_expression.append(tokenize(lisp))

        # lisp[0] is ')', so take that out of the lisp list
        lisp.pop(0)
        # return the list we created holding the expressions
        return new_expression
    else:
        # this is not a paren, so it doesn't indicate any new statements to resolve
        # return just the symbol itself
        return atomize(token)


if __name__ == '__main__':
    # open lisp file specified in command line arguments
    args = parse_arguments()
    with open (args.filename) as file:
        lisp_string = file.read().replace('\n', ' ')
    ast = tokenize(lisp_string)
    print('AST', ast)
