# Generated from math.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .mathParser import mathParser
else:
    from mathParser import mathParser

# This class defines a complete generic visitor for a parse tree produced by mathParser.

class mathVisitor(ParseTreeVisitor):
    string = ""

    # Visit a parse tree produced by mathParser#program.
    def visitProgram(self, ctx:mathParser.ProgramContext):
        children = self.visitChildren(ctx)
        self.string = str(children)
        return children


    # Visit a parse tree produced by mathParser#Parenthesis.
    def visitParenthesis(self, ctx:mathParser.ParenthesisContext):
        child = self.visit(ctx.expression())
        self.string = str(child)
        return child


    # Visit a parse tree produced by mathParser#Multiplication.
    def visitMultiplication(self, ctx:mathParser.MultiplicationContext):
        term1 = self.visit(ctx.expression(0))
        term2 = self.visit(ctx.expression(1))

        operator = ctx.op.text

        # if term1 and term2 are both numbers, multiply them
        if isinstance(term1, float) and isinstance(term2, float):
            if operator == '*':
                self.string = str(term1 * term2)
                return term1 * term2
            else:
                if term2 <= 0.001:
                    self.string = str(term1)
                    return term1

                self.string = str(term1 / term2)
                return term1 / term2


        if operator == '*':
            self.string = "({} * {})".format(term1, term2)
            return "({} * {})".format(term1, term2)
        else:
            self.string = "({} / {})".format(term1, term2)
            return "({} / {})".format(term1, term2)


    # Visit a parse tree produced by mathParser#Addition.
    def visitAddition(self, ctx:mathParser.AdditionContext):
        term1 = self.visit(ctx.expression(0))
        term2 = self.visit(ctx.expression(1))

        operator = ctx.op.text


        if isinstance(term1, float) and isinstance(term2, float):
            if operator == '+':
                self.string = str(term1 + term2)
                return term1 + term2
            else:
                self.string = str(term1 - term2)
                return term1 - term2

        if operator == '+':
            self.string = "({} + {})".format(term1, term2)
            return "({} + {})".format(term1, term2)
        else:
            self.string = "({} - {})".format(term1, term2)
            return "({} - {})".format(term1, term2)


    # Visit a parse tree produced by mathParser#TermExpression.
    def visitTermExpression(self, ctx:mathParser.TermExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathParser#UnaryMinus.
    def visitUnaryMinus(self, ctx:mathParser.UnaryMinusContext):
        return float(ctx.getText().replace(',', '.'))


    # Visit a parse tree produced by mathParser#NumberTerm.
    def visitNumberTerm(self, ctx:mathParser.NumberTermContext):
        return float(ctx.getText().replace(',', '.'))


    # Visit a parse tree produced by mathParser#VariableTerm.
    def visitVariableTerm(self, ctx:mathParser.VariableTermContext):
        return ctx.getText()


    # Visit a parse tree produced by mathParser#TrigTerm.
    def visitTrigTerm(self, ctx:mathParser.TrigTermContext):
        fun = self.visit(ctx.trig())
        exp = self.visit(ctx.expression())
    
        string = "{}({})".format(fun, exp)
        self.string = string
        return string


    # Visit a parse tree produced by mathParser#trig.
    def visitTrig(self, ctx:mathParser.TrigContext):
        return ctx.getText()



del mathParser