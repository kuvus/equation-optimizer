from Term import Type, Expression

# Generated from math.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .mathParser import mathParser
else:
    from mathParser import mathParser

# This class defines a complete generic visitor for a parse tree produced by mathParser.

class mathVisitor(ParseTreeVisitor):
    string = ""
    out = None

    # Visit a parse tree produced by mathParser#program.
    def visitProgram(self, ctx:mathParser.ProgramContext):
        children = self.visitChildren(ctx)
        self.string = str(children)
        self.out = Expression([children], Type.START)
        return children


    # Visit a parse tree produced by mathParser#Parenthesis.
    def visitParenthesis(self, ctx:mathParser.ParenthesisContext):
        child = self.visit(ctx.expression())
        if len(child.children) == 1:
            # print('b', child)
            return Expression(child.children, child.dtype)

        return Expression([child], Type.PAR)


    # Visit a parse tree produced by mathParser#Multiplication.
    def visitMultiplication(self, ctx:mathParser.MultiplicationContext):
        term1: Expression = self.visit(ctx.expression(0))
        term2: Expression = self.visit(ctx.expression(1))

        operator = ctx.op.text

        if term1.dtype == Type.NUM and term2.dtype == Type.NUM:
            if operator == '*':
                return Expression([term1.children[0] * term2.children[0]], Type.NUM)
            else:
                # print(term2)
                if term2.children[0] <= 0.001:
                    return Expression([term1.children[0]], Type.NUM)
                return Expression([term1.children[0] / term2.children[0]], Type.NUM)


        if operator == '*':
            return Expression([term1, term2], Type.MUL)
        else:
            return Expression([term1, term2], Type.DIV)


    # Visit a parse tree produced by mathParser#Addition.
    def visitAddition(self, ctx:mathParser.AdditionContext):
        term1: Expression = self.visit(ctx.expression(0))
        term2: Expression = self.visit(ctx.expression(1))

        operator = ctx.op.text

        if term1.dtype == Type.NUM and term2.dtype == Type.NUM:
            if operator == '+':
                # print(term1.children[0], term2.children[0])
                return Expression([term1.children[0] + term2.children[0]], Type.NUM)
            else:
                return Expression([term1.children[0] - term2.children[0]], Type.NUM)


        if operator == '+':
            # print('b', term1, term2)
            if term1.dtype == Type.NUM and term2.dtype == Type.PAR:
                x = term1.children[0]
                yy = term2.children[0]

                if hasattr(x, 'children'):
                    x = x.children[0]
                
                if yy.children[0].dtype == Type.NUM:
                    if yy.dtype == Type.ADD:
                        res = x + yy.children[0].children[0]
                        return Expression([Expression([res], Type.NUM), yy.children[1]], Type.ADD)
                    elif yy.dtype == Type.SUB:
                        res = x - yy.children[0].children[0]
                        if res < 0:
                            return Expression([yy.children[1], Expression([-res], Type.NUM)], Type.SUB)
                        else:
                            return Expression([Expression([res], Type.NUM), yy.children[1]], Type.ADD)
                        
                elif yy.children[1].dtype == Type.NUM:
                    if yy.dtype == Type.ADD:
                        res = x + yy.children[1].children[0]
                        return Expression([Expression([res], Type.NUM), yy.children[0]], Type.ADD)
                    elif yy.dtype == Type.SUB:
                        res = x - yy.children[1].children[0]
                        if res < 0:
                            return Expression([yy.children[0], Expression([-res], Type.NUM)], Type.SUB)
                        else:
                            return Expression([Expression([res], Type.NUM), yy.children[0]], Type.ADD)

    
            elif term1.dtype == Type.PAR and term2.dtype == Type.NUM:
                # print('b', term2.children)
                x = term2.children[0]
                yy = term1.children[0]

                if hasattr(x, 'children'):
                    x = x.children[0]
                
                if yy.children[0].dtype == Type.NUM:
                    if yy.dtype == Type.ADD:
                        res = x + yy.children[0].children[0]
                        return Expression([Expression([res], Type.NUM), yy.children[1]], Type.ADD)
                    elif yy.dtype == Type.SUB:
                        res = x - yy.children[0].children[0]
                        if res < 0:
                            return Expression([yy.children[1], Expression([-res], Type.NUM)], Type.SUB)
                        else:
                            return Expression([Expression([res], Type.NUM), yy.children[1]], Type.ADD)
                        
                elif yy.children[1].dtype == Type.NUM:
                    if yy.dtype == Type.ADD:
                        res = x + yy.children[1].children[0]
                        return Expression([Expression([res], Type.NUM), yy.children[0]], Type.ADD)
                    elif yy.dtype == Type.SUB:
                        res = x - yy.children[1].children[0]
                        if res < 0:
                            return Expression([yy.children[0], Expression([-res], Type.NUM)], Type.SUB)
                        else:
                            return Expression([Expression([res], Type.NUM), yy.children[0]], Type.ADD)

            return Expression([term1, term2], Type.ADD)
        else:
            return Expression([term1, term2], Type.SUB)


    # Visit a parse tree produced by mathParser#TermExpression.
    def visitTermExpression(self, ctx:mathParser.TermExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathParser#UnaryMinus.
    def visitUnaryMinus(self, ctx:mathParser.UnaryMinusContext):
        num = float(ctx.getText().replace(',', '.'))
        return Expression([num], Type.NUM)


    # Visit a parse tree produced by mathParser#NumberTerm.
    def visitNumberTerm(self, ctx:mathParser.NumberTermContext):
        num = float(ctx.getText().replace(',', '.'))
        return Expression([num], Type.NUM)


    # Visit a parse tree produced by mathParser#VariableTerm.
    def visitVariableTerm(self, ctx:mathParser.VariableTermContext):
        var = ctx.getText()
        return Expression([var], Type.VAR)


    # Visit a parse tree produced by mathParser#TrigTerm.
    def visitTrigTerm(self, ctx:mathParser.TrigTermContext):
        fun = self.visit(ctx.trig())
        exp = self.visit(ctx.expression())

        return Expression([exp], Type.SIN if fun == 'sin' else Type.COS)


    # Visit a parse tree produced by mathParser#trig.
    def visitTrig(self, ctx:mathParser.TrigContext):
        return ctx.getText()



del mathParser