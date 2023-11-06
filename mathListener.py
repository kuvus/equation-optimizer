# Generated from math.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .mathParser import mathParser
else:
    from mathParser import mathParser

# This class defines a complete listener for a parse tree produced by mathParser.
class mathListener(ParseTreeListener):

    # Enter a parse tree produced by mathParser#program.
    def enterProgram(self, ctx:mathParser.ProgramContext):
        pass

    # Exit a parse tree produced by mathParser#program.
    def exitProgram(self, ctx:mathParser.ProgramContext):
        pass


    # Enter a parse tree produced by mathParser#Parenthesis.
    def enterParenthesis(self, ctx:mathParser.ParenthesisContext):
        pass

    # Exit a parse tree produced by mathParser#Parenthesis.
    def exitParenthesis(self, ctx:mathParser.ParenthesisContext):
        pass


    # Enter a parse tree produced by mathParser#Multiplication.
    def enterMultiplication(self, ctx:mathParser.MultiplicationContext):
        pass

    # Exit a parse tree produced by mathParser#Multiplication.
    def exitMultiplication(self, ctx:mathParser.MultiplicationContext):
        pass


    # Enter a parse tree produced by mathParser#Addition.
    def enterAddition(self, ctx:mathParser.AdditionContext):
        pass

    # Exit a parse tree produced by mathParser#Addition.
    def exitAddition(self, ctx:mathParser.AdditionContext):
        pass


    # Enter a parse tree produced by mathParser#TermExpression.
    def enterTermExpression(self, ctx:mathParser.TermExpressionContext):
        pass

    # Exit a parse tree produced by mathParser#TermExpression.
    def exitTermExpression(self, ctx:mathParser.TermExpressionContext):
        pass


    # Enter a parse tree produced by mathParser#UnaryMinus.
    def enterUnaryMinus(self, ctx:mathParser.UnaryMinusContext):
        pass

    # Exit a parse tree produced by mathParser#UnaryMinus.
    def exitUnaryMinus(self, ctx:mathParser.UnaryMinusContext):
        pass


    # Enter a parse tree produced by mathParser#NumberTerm.
    def enterNumberTerm(self, ctx:mathParser.NumberTermContext):
        pass

    # Exit a parse tree produced by mathParser#NumberTerm.
    def exitNumberTerm(self, ctx:mathParser.NumberTermContext):
        pass


    # Enter a parse tree produced by mathParser#VariableTerm.
    def enterVariableTerm(self, ctx:mathParser.VariableTermContext):
        pass

    # Exit a parse tree produced by mathParser#VariableTerm.
    def exitVariableTerm(self, ctx:mathParser.VariableTermContext):
        pass


    # Enter a parse tree produced by mathParser#TrigTerm.
    def enterTrigTerm(self, ctx:mathParser.TrigTermContext):
        pass

    # Exit a parse tree produced by mathParser#TrigTerm.
    def exitTrigTerm(self, ctx:mathParser.TrigTermContext):
        pass


    # Enter a parse tree produced by mathParser#trig.
    def enterTrig(self, ctx:mathParser.TrigContext):
        pass

    # Exit a parse tree produced by mathParser#trig.
    def exitTrig(self, ctx:mathParser.TrigContext):
        pass



del mathParser