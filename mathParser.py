# Generated from math.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,12,43,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,3,1,19,8,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,27,8,1,
        10,1,12,1,30,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,39,8,2,1,3,1,3,
        1,3,0,1,2,4,0,2,4,6,0,3,1,0,4,5,2,0,3,3,6,6,1,0,7,8,44,0,8,1,0,0,
        0,2,18,1,0,0,0,4,38,1,0,0,0,6,40,1,0,0,0,8,9,3,2,1,0,9,1,1,0,0,0,
        10,11,6,1,-1,0,11,12,5,1,0,0,12,13,3,2,1,0,13,14,5,2,0,0,14,19,1,
        0,0,0,15,16,5,3,0,0,16,19,3,2,1,4,17,19,3,4,2,0,18,10,1,0,0,0,18,
        15,1,0,0,0,18,17,1,0,0,0,19,28,1,0,0,0,20,21,10,3,0,0,21,22,7,0,
        0,0,22,27,3,2,1,4,23,24,10,2,0,0,24,25,7,1,0,0,25,27,3,2,1,3,26,
        20,1,0,0,0,26,23,1,0,0,0,27,30,1,0,0,0,28,26,1,0,0,0,28,29,1,0,0,
        0,29,3,1,0,0,0,30,28,1,0,0,0,31,39,5,10,0,0,32,39,5,9,0,0,33,34,
        3,6,3,0,34,35,5,1,0,0,35,36,3,2,1,0,36,37,5,2,0,0,37,39,1,0,0,0,
        38,31,1,0,0,0,38,32,1,0,0,0,38,33,1,0,0,0,39,5,1,0,0,0,40,41,7,2,
        0,0,41,7,1,0,0,0,4,18,26,28,38
    ]

class mathParser ( Parser ):

    grammarFileName = "math.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'-'", "'*'", "'/'", "'+'", 
                     "'sin'", "'cos'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "VAR", "NUMBER", "WHITESPACE", "NEWLINE" ]

    RULE_program = 0
    RULE_expression = 1
    RULE_term = 2
    RULE_trig = 3

    ruleNames =  [ "program", "expression", "term", "trig" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    VAR=9
    NUMBER=10
    WHITESPACE=11
    NEWLINE=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(mathParser.ExpressionContext,0)


        def getRuleIndex(self):
            return mathParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = mathParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return mathParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParenthesisContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mathParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(mathParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesis" ):
                listener.enterParenthesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesis" ):
                listener.exitParenthesis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesis" ):
                return visitor.visitParenthesis(self)
            else:
                return visitor.visitChildren(self)


    class MultiplicationContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mathParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mathParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(mathParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplication" ):
                listener.enterMultiplication(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplication" ):
                listener.exitMultiplication(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplication" ):
                return visitor.visitMultiplication(self)
            else:
                return visitor.visitChildren(self)


    class AdditionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mathParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mathParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(mathParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddition" ):
                listener.enterAddition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddition" ):
                listener.exitAddition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddition" ):
                return visitor.visitAddition(self)
            else:
                return visitor.visitChildren(self)


    class TermExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mathParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(mathParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermExpression" ):
                listener.enterTermExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermExpression" ):
                listener.exitTermExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermExpression" ):
                return visitor.visitTermExpression(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mathParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(mathParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinus" ):
                listener.enterUnaryMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinus" ):
                listener.exitUnaryMinus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinus" ):
                return visitor.visitUnaryMinus(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = mathParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = mathParser.ParenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 11
                self.match(mathParser.T__0)
                self.state = 12
                self.expression(0)
                self.state = 13
                self.match(mathParser.T__1)
                pass
            elif token in [3]:
                localctx = mathParser.UnaryMinusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 15
                self.match(mathParser.T__2)
                self.state = 16
                self.expression(4)
                pass
            elif token in [7, 8, 9, 10]:
                localctx = mathParser.TermExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 17
                self.term()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 28
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 26
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = mathParser.MultiplicationContext(self, mathParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 20
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 21
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==4 or _la==5):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 22
                        self.expression(4)
                        pass

                    elif la_ == 2:
                        localctx = mathParser.AdditionContext(self, mathParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 23
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 24
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==6):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 25
                        self.expression(3)
                        pass

             
                self.state = 30
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return mathParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TrigTermContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mathParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def trig(self):
            return self.getTypedRuleContext(mathParser.TrigContext,0)

        def expression(self):
            return self.getTypedRuleContext(mathParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrigTerm" ):
                listener.enterTrigTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrigTerm" ):
                listener.exitTrigTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrigTerm" ):
                return visitor.visitTrigTerm(self)
            else:
                return visitor.visitChildren(self)


    class NumberTermContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mathParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(mathParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberTerm" ):
                listener.enterNumberTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberTerm" ):
                listener.exitNumberTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberTerm" ):
                return visitor.visitNumberTerm(self)
            else:
                return visitor.visitChildren(self)


    class VariableTermContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mathParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(mathParser.VAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableTerm" ):
                listener.enterVariableTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableTerm" ):
                listener.exitVariableTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableTerm" ):
                return visitor.visitVariableTerm(self)
            else:
                return visitor.visitChildren(self)



    def term(self):

        localctx = mathParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_term)
        try:
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                localctx = mathParser.NumberTermContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.match(mathParser.NUMBER)
                pass
            elif token in [9]:
                localctx = mathParser.VariableTermContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.match(mathParser.VAR)
                pass
            elif token in [7, 8]:
                localctx = mathParser.TrigTermContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 33
                self.trig()
                self.state = 34
                self.match(mathParser.T__0)
                self.state = 35
                self.expression(0)
                self.state = 36
                self.match(mathParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TrigContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return mathParser.RULE_trig

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrig" ):
                listener.enterTrig(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrig" ):
                listener.exitTrig(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrig" ):
                return visitor.visitTrig(self)
            else:
                return visitor.visitChildren(self)




    def trig(self):

        localctx = mathParser.TrigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_trig)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            _la = self._input.LA(1)
            if not(_la==7 or _la==8):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




