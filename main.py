import sys

import antlr4

from mathLexer import mathLexer
from mathParser import mathParser

from mathVisitor import mathVisitor as Visitor

sys.setrecursionlimit(3000)

def main():
    input_stream = antlr4.FileStream(sys.argv[1])
    lexer = mathLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = mathParser(stream)
    tree = parser.program()
    visitor = Visitor()
    visitor.visit(tree)

    out = str(visitor.out).replace('.', ',')
    print('Optimized function:')
    print(out)

    if len(sys.argv) > 2:
        with open(sys.argv[2], 'w') as f:
            f.write(out)

if __name__ == '__main__':
    main()