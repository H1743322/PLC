import ply.lex as lex
import re
import sys

tokens = ['INT','STR','NUM','ID',
'MAIN','END',
'PRINT','READ',
'IF','ELSE',
'REPEATE','UNTIL','WHILE','DO',
'AND','OR','NOT',
'EQUALS','GREATER','LESSER','GREATERQ','LESSERQ'
]
literals = ['%','*', '+' ,'/', '-', '=', '(', ')', '.', '<', '>', ',', '!', '{', '}', '[', ']']

def t_INT(t):
    r'Int'
    return t
def t_STR(t):
    r'"[^"]+"' 
    return t  
def t_NUM(t):
    r'-?\d+'
    #t.value = int(t.value)
    return t
def t_MAIN(t):
    r'MAIN'
    return t
def t_END(t):
    r'END'
    return t
def t_PRINT(t):
    r'Print'
    return t
def t_READ(t):
    r'Read'
    return t    
def t_IF(t):
    r'If'
    return t    
def t_ELSE(t):
    r'Else'
    return t       
def t_REPEATE(t):
    r'Repeat'
    return t   
def t_UNTIL(t):
    r'Until'
    return t
def t_WHILE(t):
    r'While'
    return t
def t_DO(t):
    r'Do'
    return t        
def t_AND(t):
    r'AND'
    return t 
def t_OR(t):
    r'OR'
    return t      
def t_NOT(t):
    r'!'
    return t
def t_GREATERQ(t):
    r'>='
    return t
def t_LESSERQ(t):
    r'<='
    return t  

def t_EQUALS(t):
    r'=='
    return t 
    return t  
def t_GREATER(t):
    r'>'
    return t
def t_LESSER(t):
    r'<'
    return t 
      
def t_ID(t):
    r'\w+'
    return t

t_ignore = " \t\n"
def t_error(t):
    print('Illegal character: ', t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
        