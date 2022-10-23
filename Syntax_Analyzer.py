#To do list 
#rewrite the grammar with removed left recursion 
#change the lexer so that is prints out token:followed by token and lememe
#print out the production rules used 
#handle the errors that come up with meaningful message
#
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

Keywords = ["integer", "boolean", "real", "if", "else", "endif", "while", "return",
            "get", "put", "true", "false", "function"]

#################### SEPERATORS ######################
Seperators = ',$(){};='

#################### OPERATORS #######################
Operators = ["==", "!=", ">", "<", "<=", "=>", "+", "-", "*", "/"]

#################### String with arrows #######################
def string_with_arrows(text, pos_start, pos_end):
    result = ''

    # Calculate indices
    idx_start = max(text.rfind('\n', 0, pos_start.idx), 0)
    idx_end = text.find('\n', idx_start + 1)
    if idx_end < 0: idx_end = len(text)
    
    # Generate each line
    line_count = pos_end.ln - pos_start.ln + 1
    for i in range(line_count):
        # Calculate line columns
        line = text[idx_start:idx_end]
        col_start = pos_start.col if i == 0 else 0
        col_end = pos_end.col if i == line_count - 1 else len(line) - 1

        # Append to result
        result += line + '\n'
        result += ' ' * col_start + '^' * (col_end - col_start)

        # Re-calculate indices
        idx_start = idx_end
        idx_end = text.find('\n', idx_start + 1)
        if idx_end < 0: idx_end = len(text)

    return result.replace('\t', '')

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
        answer += '\n\n' + string_with_arrows(self.position_begin.ftxt, self.position_begin, self.position_end)
        return answer

class IllegalCharOopsie(Oopsie):
    def __init__(self, position_begin, position_end, details):
        super().__init__(position_begin, position_end, 'Illegal Character', details)

#for wrong identifier message
class IllegalIdentifierOopsie(Oopsie):
    def __init__(self, position_begin, position_end, details):
        super().__init__(position_begin, position_end, 'Error', details)

class InvalidSyntaxError(Oopsie):
		def __init__(self, pos_start, pos_end, details=''):
				super().__init__(pos_start, pos_end, 'Invalid Syntax', details)


#################### POSITION ####################

class Position:
    def __init__(self, index, line, column, fn, ftxt):
        self.index = index
        self.line = line
        self.column = column
        self.fn = fn
        self.ftxt = ftxt

    def advance(self, current_char=None):
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
TOK_EQUALS = 'SEPARATOR'
TOK_TWOEQUALS = 'OPERATOR'
TOK_NOTEQUAL = 'OPERATOR'
TOK_EQUALGTR = 'OPERATOR'
TOK_EQUALLESS = 'OPERATOR'
TOK_EQUALEQUAL= 'OPERATOR'
TOK_LEFTARROW = 'OPERATOR'
TOK_RIGHTARROW = 'OPERATOR'
TOK_LPAREN   = 'SEPARATOR'
TOK_RPAREN   = 'SEPARATOR'
TOK_COMMA = 'SEPARATOR'
TOK_SEMICOLON = 'SEPARATOR'
TOK_DOLLAR = 'SEPARATOR'
TOK_LBRACKET = 'SEPARATOR'
TOK_RBRACKET = 'SEPARATOR'
TOK_KEY = 'KEYWORD'
TOK_ID = 'IDENTIFIERS'
TOK_EOF = 'EOF'


class Token:
    def __init__(self, type_, value=None, position_begin=None, position_end=None):
            self.type = type_
            self.value = value

            if position_begin:
                self.position_begin = position_begin.copy()
                self.position_end = position_begin.copy()
                self.position_end.advance()

            if position_end:
                self.position_end = position_end
    
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
        count = []  # for relation operator counter =>
        count2 = [] # for relation operator counter <=

        while self.current_char != None:
            if self.current_char in ' \t \n':
                self.advance()
            elif self.current_char == '/':
                self.advance()
                if self.current_char == '*':
                    self.advance()
                    while self.current_char != '*':
                        self.advance()
                    self.advance()
                else:
                    tokens.append(Token(TOK_DIV, "/"))
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
                for x in range(len(self.text)):
                    if self.text[x] == self.current_char:
                        count.append(x)
                c = count[0]
                if(self.text[c+1] == '>'):
                    tokens.append(Token(TOK_EQUALGTR, "=>"))
                    self.advance()
                    self.advance()
                    count.remove(count[0])
                elif(self.text[c+1] == '='):
                    tokens.append(Token(TOK_EQUALEQUAL, "=="))
                    self.advance()
                    self.advance()
                    count.remove(count[0])
                elif(self.text[c+1] == ' '):
                    tokens.append(Token(TOK_EQUALS, "="))
                    self.advance()

            elif self.current_char == '<':
                for y in range(len(self.text)):
                    if self.text[y] == self.current_char:
                        count2.append(y)
                c = count2[0]
                if(self.text[c+1] == '='):
                    tokens.append(Token(TOK_EQUALLESS, "<="))
                    self.advance()
                    self.advance()
                    count2.remove(count2[0])
                else:
                    tokens.append(Token(TOK_LEFTARROW, "<"))
                    self.advance()
            elif self.current_char == '>':
                tokens.append(Token(TOK_RIGHTARROW, ">"))
                self.advance()
            elif self.current_char == '!':
                tokens.append(Token(TOK_NOTEQUAL, "!="))
                self.advance()
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
            elif self.current_char == '$':
                tokens.append(Token(TOK_DOLLAR, "$"))
                self.advance()
            elif self.current_char == '{':
                tokens.append(Token(TOK_LBRACKET, "{"))
                self.advance()
            elif self.current_char == '}':
                tokens.append(Token(TOK_RBRACKET, "}"))
                self.advance()

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
                    tokens.append(Token(TOK_KEY, holder))

                else:
                    tokens.append(Token(TOK_ID, holder))           

            else:
                position_begin = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], IllegalCharOopsie(position_begin, self.pos, "'" + char + "'")

        tokens.append(Token(TOK_EOF, position_begin=self.pos))
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

#######################################
# NODES
#######################################

class NumberNode:
	def __init__(self, tok):
		self.tok = tok

	def __repr__(self):
		return f'{self.tok}'

class BinOpNode:
	def __init__(self, left_node, op_tok, right_node):
		self.left_node = left_node
		self.op_tok = op_tok
		self.right_node = right_node

	def __repr__(self):
		return f'({self.left_node}, {self.op_tok}, {self.right_node})'

class UnaryOpNode:
	def __init__(self, op_tok, node):
		self.op_tok = op_tok
		self.node = node

	def __repr__(self):
		return f'({self.op_tok}, {self.node})'

#######################################
# PARSE RESULT
#######################################

class ParseResult:
	def __init__(self):
		self.error = None
		self.node = None

	def register(self, res):
		if isinstance(res, ParseResult):
			if res.error: self.error = res.error
			return res.node

		return res

	def success(self, node):
		self.node = node
		return self

	def failure(self, error):
		self.error = error
		return self

#######################################
# PARSER
#######################################

class Parser:
	def __init__(self, tokens):
		self.tokens = tokens
		self.tok_idx = -1
		self.advance()

	def advance(self, ):
		self.tok_idx += 1
		if self.tok_idx < len(self.tokens):
			self.current_tok = self.tokens[self.tok_idx]
		return self.current_tok

	def parse(self):
		res = self.expr()
		if not res.error and self.current_tok.type != TOK_EOF:
			return res.failure(InvalidSyntaxError(
				self.current_tok.postion_begin , self.current_tok.position_end,
				"Expected '+', '-', '*' or '/'"
			))
		return res

	###################################

	def factor(self):
		res = ParseResult()
		tok = self.current_tok

		if tok.type in (TOK_PLUS, TOK_MINUS):
			res.register(self.advance())
			factor = res.register(self.factor())
			if res.error: return res
			return res.success(UnaryOpNode(tok, factor))
		
		elif tok.type in (TOK_INT, TOK_REAL):
			res.register(self.advance())
			return res.success(NumberNode(tok))

		elif tok.type == TOK_LPAREN:
			res.register(self.advance())
			expr = res.register(self.expr())
			if res.error: return res
			if self.current_tok.type == TOK_RPAREN:
				res.register(self.advance())
				return res.success(expr)
			else:
				return res.failure(InvalidSyntaxError(
					self.current_tok.position_begin, self.current_tok.position_end,
					"Expected ')'"
				))

		return res.failure(InvalidSyntaxError(
			tok.position_begin, tok.position_end,
			"Expected int or float"
		))

	def term(self):
		return self.bin_op(self.factor, (TOK_MUL, TOK_DIV))

	def expr(self):
		return self.bin_op(self.term, (TOK_PLUS, TOK_MINUS))

	###################################

	def bin_op(self, func, ops):
		res = ParseResult()
		left = res.register(func())
		if res.error: return res

		while self.current_tok.type in ops:
			op_tok = self.current_tok
			res.register(self.advance())
			right = res.register(func())
			if res.error: return res
			left = BinOpNode(left, op_tok, right)

		return res.success(left)

#################### RUN ####################

def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, oopsie = lexer.make_tokens()
    if oopsie: return None, oopsie
	# Generate AST
    parser = Parser(tokens)
    ast = parser.parse()
    return ast.node, ast.oopsie
