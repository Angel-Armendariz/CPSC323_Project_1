#################### To-do list########################
# 1.) throw an error when a nonletter is in front of an identifier; ex: >1hello, >true 1hello --> should throw an error
# -- for this, we need to do something for self.current_char to read if it is an integer
#  2.) FSM implementation of states in 2d array????

#################### CONSTANTS ####################


from ast import Num
from lib2to3.pytree import convert
from tkinter import E
from winreg import HKEY_LOCAL_MACHINE


Numbers = '0123456789'
Underscore = '_'

#################### IDENTIFIERS ####################

Letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
Identifiers = '_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

#################### KEYWORDS #######################

Keywords = ["break", "boolean", "case", "char", "const", "continue", "default", "do",
            "double", "else", "false", "float", "function", "long", "register", "for", "if", 
            "int", "short", "sizeof", "static", "signed", "unsigned", "struct", "return", 
            "switch", "typedef", "void", "return", "while", "string", "true"]

#################### FOR WHEN WE MAKE OOPSIE DAISISES/ERRORS ####################

class Oopsie:
    def __init__(self, position_begin, position_end, oopsie_name, details):
        self.position_begin = position_begin
        self.position_end = position_end
        self.oopsie_name = oopsie_name
        self.details = details
    
    def convert_string(self):
        answer  = f'{self.oopsie_name}: {self.details}\n'
        answer += f'File {self.position_begin.fn}, line {self.position_begin.line + 1}'
        return answer

class IllegalCharOopsie(Oopsie):
    def __init__(self, position_begin, position_end, details):
        super().__init__(position_begin, position_end, 'Illegal Character', details)

#for wrong identifier message
class IllegalIdentifierOopsie(Oopsie):
    def __init__(self, position_begin, position_end, details):
        super().__init__(position_begin, position_end, 'Error', details)


#################### POSITION ####################

class Position:
    def __init__(self, index, line, column, fn, ftxt):
        self.index = index
        self.line = line
        self.column = column
        self.fn = fn
        self.ftxt = ftxt

    def advance(self, current_char):
        self.index += 1
        self.column += 1

        if current_char == '\n':
            self.line += 1
            self.column = 0

        return self

    def copy(self):
        return Position(self.index, self.line, self.column, self.fn, self.ftxt)

#################### TOKENS ####################

TOK_INT		= 'INT'
TOK_REAL    = 'REAL'
TOK_PLUS     = 'OPERATOR'
TOK_MINUS    = 'OPERATOR'
TOK_MUL      = 'OPERATOR'
TOK_DIV      = 'OPERATOR'
TOK_EQUALS = 'OPERATOR'
TOK_LEFTARROW = 'OPERATOR'
TOK_RIGHTARROW = 'OPERATOR'
TOK_LPAREN   = 'SEPARATOR'
TOK_RPAREN   = 'SEPARATOR'
TOK_COMMA = 'SEPARATOR'
TOK_SEMICOLON = 'SEPARATOR'
TOK_KEY = 'KEYWORD'
TOK_ID = 'IDENTIFIERS'


class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value
    
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'

#################### LEXER ####################

class Lexer:
    def __init__(self, fn, text):
        self.fn = fn
        self.text = text
        self.pos = Position(-1, 0, -1, fn, text)
        self.current_char = None
        self.advance()
    
    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.index] if self.pos.index < len(self.text) else None
    
    #Needs work, but splits string, commented for now
    '''def check_identifier(self):
        tokens = []
        for value in self.text.split():
            tokens.append(value)
            print(value)
            if value in Numbers:
                print('yes')
            else:
                print('Value: {} is not an identifier'.format(value))'''

    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            #self.check_identifier(), if wanted to use another function to check for identifiers

            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in Numbers:
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Token(TOK_PLUS, "+"))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TOK_MINUS, "-"))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TOK_MUL, "*"))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TOK_DIV, "/"))
                self.advance()
            elif self.current_char == '=':
                tokens.append(Token(TOK_EQUALS, "="))
                self.advance()
            elif self.current_char == '<':
                tokens.append(Token(TOK_LEFTARROW, "<"))
                self.advance()
            elif self.current_char == '>':
                tokens.append(Token(TOK_RIGHTARROW, ">"))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TOK_LPAREN, "("))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TOK_RPAREN, ")"))
                self.advance()
            elif self.current_char == ',':
                tokens.append(Token(TOK_COMMA, ","))
                self.advance()
            elif self.current_char == ';':
                tokens.append(Token(TOK_SEMICOLON, ";"))
                self.advance()

            #Not sure, but able to give error only if first input string starts w number
                    #Then it will output the whole input string as an error
            elif self.text[0] in Numbers:
                position_begin = self.pos.copy()
                error = self.text
                self.advance()
                return [], IllegalIdentifierOopsie(position_begin, self.pos, "'" + error + "'")

            elif self.text in Keywords:
                holder= ''
                while self.current_char != None:
                    while self.current_char in ' \t':
                        self.advance()
                    holder += self.current_char
                    self.advance()
                tokens.append(Token(TOK_KEY, holder))

            elif self.current_char in Letters and self.text not in Keywords:
                holder=''
                while self.current_char != None and self.current_char in Identifiers:
                    while self.current_char in ' \t':
                        self.advance()
                    holder += self.current_char
                    self.advance()

                if holder in Keywords:
                    # when i do print(holder) to check string split, it outputs the keywords correctly
                    # but if holder in Numbers, it does not identify it
                    # if condition might need to change for holder to hold strings w numbers too??
                    tokens.append(Token(TOK_KEY, holder))

                else:
                    tokens.append(Token(TOK_ID, holder))           

            else:
                position_begin = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], IllegalCharOopsie(position_begin, self.pos, "'" + char + "'")

        return tokens, None

    def make_number(self):
        num_str = ''
        dot_count = 0

        while self.current_char != None and self.current_char in Numbers + '.':
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

        if dot_count == 0:
            return Token(TOK_INT, int(num_str))
        else:
            return Token(TOK_REAL, float(num_str))
#################### RUN ####################

def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, oopsie = lexer.make_tokens()
    return tokens, oopsie
