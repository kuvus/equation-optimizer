grammar math;

program: expression;

expression
    : '(' expression ')' # Parenthesis
    | '-' expression # UnaryMinus
    | expression op=('*'|'/') expression # Multiplication
    | expression op=('+'|'-') expression # Addition
    | term # TermExpression
    ;

term
    : NUMBER # NumberTerm
    | VAR # VariableTerm
    | trig '(' expression ')' # TrigTerm
    ;

VAR: [A-Z][0-9]+;
NUMBER: [0-9]+ (','|'.') [0-9]+;
trig: 'sin' | 'cos';

WHITESPACE : [ \t]+ -> skip;
NEWLINE: '\r'? '\n' -> skip;
