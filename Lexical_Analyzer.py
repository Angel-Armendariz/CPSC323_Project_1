#################### To-do list
# make the identifiers not also trip the integers section 
# make the file read from the source testing code instead of the input for testing 
# make a section for recogizing the keywords 

#################### CONSTANTS ####################


Numbers = '0123456789'

#################### IDENTIFIERS ####################

Letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
Identifiers = '_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
Underscore = '_'


#################### KEYWORDS #######################

Keywords = ["break", "bool", "case", "char", "const", "continue", "default", "do",
            "double", "else", "long", "register", "for", "if", "short", "sizeof", "static"
            "signed", "unsigned", "struct", "return", "switch", "typedef", "void", "return"
            "while", "string", "int", "true", "false"]

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
TOK_PLUS     = 'PLUS'
TOK_MINUS    = 'MINUS'
TOK_MUL      = 'MUL'
TOK_DIV      = 'DIV'
TOK_LPAREN   = 'LPAREN'
TOK_RPAREN   = 'RPAREN'
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

    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in Numbers and self.text not in Letters and self.current_char not in Underscore:
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Token(TOK_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TOK_MINUS))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TOK_MUL))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TOK_DIV))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TOK_LPAREN))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TOK_RPAREN))
                self.advance()

            elif self.current_char in Keywords:
                self.advance() 
                tokens.append(Token(TOK_KEY, self.text))

            elif self.current_char in Letters and self.text not in Keywords :
                while self.current_char != None and self.current_char in Identifiers:
                    self.advance()
                tokens.append(Token(TOK_ID, self.text))
                    
                

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
