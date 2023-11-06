import sys

import antlr4

from mathLexer import mathLexer
from mathParser import mathParser

from mathVisitor import mathVisitor as Visitor

def main():
    input_stream = antlr4.FileStream(sys.argv[1])
    lexer = mathLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = mathParser(stream)
    tree = parser.program()
    visitor = Visitor()
    visitor.visit(tree)

    print(visitor.string.replace('.', ','))

if __name__ == '__main__':
    main()