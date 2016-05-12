#------------------------------------------------------------
# HMM tokenizer
# ------------------------------------------------------------

import ply.lex as lex
import lis

# Reserved words
reserved = {
    'IF'     : 'if',
    'IFF'    : 'iff',
    'ELSE'   : 'else',
    'WHILE'  : 'while',
    'FOR'    : 'for',
    'INT'    : 'int',
    'FLOAT'  : 'float',
    'BOOL'   : 'bool',
    'VOID'   : 'void',
    'LIST'   : 'list',
    'TUPLE'  : 'tuple',
    'OBJECT' : 'object',
    'STRING' : 'string',
    'RETURN' : 'return',
    'TRUE'   : 'TRUE',
    'FALSE'  : 'FALSE',
    'VAR'    : 'var',
    'LET'    : 'let',
    'FUNC'   : 'func',
    'PRINT'  : 'print'
}


# List of token names.
tokens = [
          'AND_OP', 'OR_OP', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LCURLY', 'RCURLY', \
          'SEMI', 'EQ_OP', 'NE_OP', 'LE_OP', 'GE_OP', 'ELEM', 'PIPE', 'EQUALS', \
          'LT_OP', 'GT_OP', 'PLUS', 'MINUS', 'MULT', 'DIV', 'PRCNT', 'BANG', \
          'COMMA', 'SQUOTE', 'LAMBDA', 'MAP_TO', \
          'newline','COLON','BACKSLASH',\
          'INTEGER', 'IDENTIFIER', 'CLFLOAT', 'CLSTRING' \
          ] + list(reserved.keys())

# Regular expression rules for simple tokens

def t_CLFLOAT(t):
    r'[0-9]+[\.][0-9]*'
    return t

t_AND_OP = r'&&'
t_OR_OP  = r'\|\|'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\['
t_RBRACE = r']'
t_LCURLY = r'{'
t_RCURLY = r'}'
t_SEMI   = r';'
t_EQ_OP  = r'=='
t_NE_OP  = r'!='
t_LE_OP  = r'<='
t_GE_OP  = r'>='
t_ELEM   = r'<-'
t_PIPE   = r'\|'
t_EQUALS = r'='
t_LT_OP  = r'<'
t_GT_OP  = r'>'
t_MINUS  = r'-'
t_PLUS   = r'\+'
t_MULT   = r'\*'
t_DIV    = r'/'
t_PRCNT  = r'%'
t_BANG   = r'!'
t_COMMA  = r','
t_SQUOTE = r"'"
#t_DOT    = r'.'
t_LAMBDA = r'\(\\'
t_MAP_TO = r'->'
t_COLON = r'\:'
t_BACKSLASH = r'\\'

def t_INTEGER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print "Line %d: Number %s is too large!" % (t.lineno,t.value)
        t.value = 0
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reserved:
        #print "In t_IDENTIFIER, saw: ", t.value.upper()
        t.type = t.value.upper()
    return t

def t_CLSTRING(t):
    r'"[a-zA-Z0-9_+\*\- :,]*"'
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    return t
    #t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
lex.lex()

# BNF Parsing rules

def p_program(p):
    '''program : expressions'''
    p[0]=p[1]

def p_prints(p):
    '''expression : PRINT LPAREN expression RPAREN'''
    p[0] = ['print'] + [p[3]]
#    print(p[0])
#    lis.eval(p[0])


def p_expressions(p):
    '''expressions : expression newline
                   | expression expressions'''
    if isinstance(p[2],list):
        p[0] = [p[1],p[2]]
    else:
        p[0] = p[1]
#    print("AST:",p[0])


def p_letdeclarations(p):
    '''letdeclarations : LET IDENTIFIER EQUALS expression'''

    a = lis.eval(p[4])
    p[0] = ['let'] + [p[2]] + [a]
#    print p[0]
#    lis.eval(p[0])

def p_expression(p):
    '''expression : statement 
                  | letdeclarations'''
    p[0] = p[1]
#    print p[0]
#    print lis.eval(p[0])

def p_statement(p):
    '''statement : primary
                 | literal'''
    p[0]=p[1]

def p_str(p):
    '''str : SQUOTE IDENTIFIER SQUOTE'''
    p[0] = p[2]
#
#def p_strexps(p):
#    '''strexps : strexp
#               | strexp strexps '''
#    if len(p)==2:
#        p[0]= p[1]
#    else:
#        p[0]= p[1]+p[2]
#
#def p_strexp(p):
#    '''strexp : CHARS
#              | BACKSLASH LPAREN expression RPAREN'''
#    if len(p) == 2:
#        p[0]=p[1]
#    else:
#        p[0]=str(lis.eval(expression))


precedence = (
    ('left','PLUS','MINUS'),
    ('left','MULT','DIV')
)


def p_primary_binop(p):
    '''primary : primary PLUS primary
                  | primary MINUS primary
                  | primary MULT primary
                  | primary DIV primary'''
    if p[3][0] in ['+','-','*','/'] and p[1][0] in ['+','-','*','/']:
        if p[2] == '+'  : p[0] = ['+'] + [p[1]] + [p[3]]
        elif p[2] == '-': p[0] = ['-'] + [p[1]] + [p[3]]
        elif p[2] == '*': p[0] = ['*'] + [p[1]] + [p[3]]
        elif p[2] == '/': p[0] = ['/'] + [p[1]] + [p[3]]
    elif p[3][0] in ['+','-','*','/'] and p[1][0] not in ['+','-','*','/']:
        if p[2] == '+'  : p[0] = ['+'] + p[1] + [p[3]]
        elif p[2] == '-': p[0] = ['-'] + p[1] + [p[3]]
        elif p[2] == '*': p[0] = ['*'] + p[1] + [p[3]]
        elif p[2] == '/': p[0] = ['/'] + p[1] + [p[3]]
    elif p[3][0] not in ['+','-','*','/'] and p[1][0] in ['+','-','*','/']:
        if p[2] == '+'  : p[0] = ['+'] + [p[1]] + p[3]
        elif p[2] == '-': p[0] = ['-'] + [p[1]] + p[3]
        elif p[2] == '*': p[0] = ['*'] + [p[1]] + p[3]
        elif p[2] == '/': p[0] = ['/'] + [p[1]] + p[3]
    else:
        if p[2] == '+'  : p[0] = ['+'] + p[1] + p[3]
        elif p[2] == '-': p[0] = ['-'] + p[1] + p[3]
        elif p[2] == '*': p[0] = ['*'] + p[1] + p[3]
        elif p[2] == '/': p[0] = ['/'] + p[1] + p[3]


def p_expression_group(p):
    "primary : LPAREN primary RPAREN"
    if isinstance(p[2],list):
        p[0] = p[2]
    else:
        p[0] = [p[2]]

def p_expression_number(p):
    "primary : literal"
    p[0] = [p[1]]



def p_type(p):
    '''type : INT
            | FLOAT
            | BOOL
            | LIST
            | TUPLE
            | OBJECT
            | CLSTRING'''


def p_literal(p):
    '''literal : INTEGER
               | IDENTIFIER
               | TRUE
               | FALSE
               | CLFLOAT
               | str'''
    p[0] = p[1]

def emptyline(self):
    """Do nothing on empty input line"""
    pass# Error handling rule

def p_error(p):
    print "At line: ", p.lexer.lineno,
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
yacc.yacc()

#with open('testfile.c', 'r') as content_file:
#    content = content_file.read()
#print(content)
#a = yacc.parse(content)
#print('FINAL AST: ',a)

#flag = True

#while(flag):
#    lis.eval(a[0])
#    if len(a)==2 and isinstance(a[0],list): 
#        a = a[1]
#    else:
#        flag = False

