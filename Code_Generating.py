import Lexical_Analyzer
from Stack import Stack

file = []                                                     # this file will be returned to main.py for it be tured into "parsedFile.txt"
Jump_Stack = Stack()

memory_address = 5000
input_filename = ''

Instruction_Table_Address_Array = []
Instruction_Table_Operation_Array = []
Instruction_Table_Operand_Array = []

Identifier_Array = []
Memory_Address_Array = []
TypeArray = []

def lexer(list_of_lexemes):
    """Will return the token based on the line number."""

    global lineNumber
    lineNumber += 2                                                  
    global line
    line += 1

    longLexeme = list_of_lexemes[lineNumber]                  # lexeme = "Lexeme:___" part from the from the file
    lexeme = longLexeme[7:]
    
    longToken = list_of_lexemes[lineNumber -1]
    token = longToken[6:]                                     # token  = the part after the colon ":" from the file 

    return lexeme, token

"""
Initializing what's needed? --kaitlin
"""
def __init__(self, lexer):
    self.lexer = lexer
    global currentLexeme
    global currentToken
    currentLexeme, currentToken = lexer(list_of_lexemes)
    self.symbolTable = [] # must hold: lexeme and memory address where identifier is in the table
    self.jumpAddress = []
    self.code = []
    self.startingAddress = 5000 # set memory address to 5000, says in the document
    self.declaration_type

def genInstruction(self, operation, operand):
    """self.code.append({
        "address": len(self.code) + 1, # increment by 1 when new identifier is declared and placed into the table
        "operation": operation,
        "operand": operand
    })"""
    pass

# Insert identifer into table
def insertToTable(self, indentifier):
    pass

# To check if particular identiifer is already in the table
def inTable(self, indentifier):
    #return indentifier
    #else return error
    pass

# increment address by 1 when new identifier is declared and placed into the table
def instructionAddress(self):
    return len(self.code) + 1

# if identifier is in table, return what's in the symbol table that's holding the identifier[1]
def getAddress(self, identifier):
    pass

# if identifier is in table, return what's in the symbol table that's holding the identifier[2]
def typeMatch(self, identifier):
    pass

def backPatch(self, jumpAddress):
    # pop from stack
    global Instruction_Table_Address_Array
    address = Jump_Stack.pop()
    Instruction_Table_Operand_Array[address] = jumpAddress + 1
    # get jump address from code list
    # create label
    pass

def print_assembly_code():
    assembly_output_file = open(input_filename + "_assembly_code" + ".txt", "w")

    i = 0
    while i < len(Instruction_Table_Address_Array):
        if Instruction_Table_Operand_Array[i] == None:
            assembly_output_file.write(
                str(Instruction_Table_Address_Array[i] + 1) + ". " + Instruction_Table_Operation_Array[i] + '\n')
        else:
            assembly_output_file.write(
                str(Instruction_Table_Address_Array[i] + 1) + ". " + Instruction_Table_Operation_Array[i] + " " + str(
                    Instruction_Table_Operand_Array[i]) + '\n')
        i += 1

def next_lexeme(lexer_table, i):
    j = -1
    token = ""
    lexeme = ""
    line_number = ""

    if (i < len(lexer_table)):
        while j < len(lexer_table[i]):
            while (True):
                j += 1
                if line_number == "":
                    if lexer_table[i][j] == "" or lexer_table[i][j] == "\t":
                        continue
                    elif lexer_table[i][j].isdigit():
                        line_number += str(lexer_table[i][j])
                else:
                    if lexer_table[i][j] == " " or lexer_table[i][j] == "\t":
                        break
                    else:
                        line_number += lexer_table[i][j]

            while (True):
                j += 1
                if token == "":
                    if lexer_table[i][j] == " " or lexer_table[i][j] == "\t":
                        continue
                    elif lexer_table[i][j].isalpha():
                        token += lexer_table[i][j]
                else:
                    if lexer_table[i][j] == " " or lexer_table[i][j] == "\t":
                        break
                    else:
                        token += lexer_table[i][j]

            while (True):
                j += 1
                if lexer_table[i][j] == " " or lexer_table[i][j] == "\t":
                    continue
                elif lexer_table[i][j] == "\n":
                    break
                else:
                    lexeme += lexer_table[i][j]
            break

        return line_number, token, lexeme, i
    else:
        print('\n\n*****    Parsing finished    *****')
        # Print Assembly Code
        print_assembly_code()
        exit()

def create_symbol_table(input_filename):
    global Identifier_Array, Memory_Address_Array, TypeArray, memory_address

    # read from lexer.py output file
    lexer_output_file = open(input_filename + "_lexer_output" + ".txt", "r")
    lexer_table = lexer_output_file.readlines()
    output_file = open(input_filename + "_symbol_table" + ".txt", "w")

    i = 2
    while i < len(lexer_table) - 1:
        line_number, token, lexeme, i = next_lexeme(lexer_table, i)
        if (lexeme == "int") or (lexeme == "boolean"):
            tempType = lexeme
            line_number, token, lexeme, i = next_lexeme(lexer_table, i)
            while (lexeme != ";"):
                line_number, token, lexeme, i = next_lexeme(lexer_table, i)
                if (lexeme == ",") or (lexeme == ";") or (lexeme == tempType):
                    i += 1
                else:
                    if (lexeme in Identifier_Array):
                        print(lexeme + " has already been declared")
                        exit()
                    else:
                        Identifier_Array.append(lexeme)
                        Memory_Address_Array.append(memory_address)
                        memory_address += 1
                        TypeArray.append(tempType)
                        i += 1

def generate_assembly_instruction(operation_instr, operation):
    global Instruction_Table_Address_Array, Instruction_Table_Operation_Array, Instruction_Table_Operand_Array, instruction_table_address

    Instruction_Table_Address_Array.append(instruction_table_address)
    Instruction_Table_Operation_Array.append(operation_instr)
    Instruction_Table_Operand_Array.append(operation)

    instruction_table_address += 1

def get_memory_address(save):
    identifierPosition = 0
    if save in Identifier_Array:
        identifierPosition = Identifier_Array.index(save)

    return Memory_Address_Array[identifierPosition]

def next_lexeme(lexer_table, i):
    j = -1
    token = ""
    lexeme = ""
    line_number = ""

    if (i < len(lexer_table)):
        while j < len(lexer_table[i]):
            while (True):
                j += 1
                if line_number == "":
                    if lexer_table[i][j] == "" or lexer_table[i][j] == "\t":
                        continue
                    elif lexer_table[i][j].isdigit():
                        line_number += str(lexer_table[i][j])
                else:
                    if lexer_table[i][j] == " " or lexer_table[i][j] == "\t":
                        break
                    else:
                        line_number += lexer_table[i][j]

            while (True):
                j += 1
                if token == "":
                    if lexer_table[i][j] == " " or lexer_table[i][j] == "\t":
                        continue
                    elif lexer_table[i][j].isalpha():
                        token += lexer_table[i][j]
                else:
                    if lexer_table[i][j] == " " or lexer_table[i][j] == "\t":
                        break
                    else:
                        token += lexer_table[i][j]

            while (True):
                j += 1
                if lexer_table[i][j] == " " or lexer_table[i][j] == "\t":
                    continue
                elif lexer_table[i][j] == "\n":
                    break
                else:
                    lexeme += lexer_table[i][j]
            break

        return line_number, token, lexeme, i
    else:
        print('\n\n*****    Parsing finished    *****')
        # Print Assembly Code
        print_assembly_code()
        exit()

def parse(parseFile):
    """Will take the inputted file and parse based on grammar rules."""

    global list_of_lines
    global list_of_lexemes
    global lineNumber
    global line

    list_of_lines = parseFile.splitlines()           # each line here is "Token: _____ Lexeme:______"
    list_of_lexemes = parseFile.split()              # each lexeme here is "Lexeme:______"
    lineNumber = -1                                  # keeps track of the amount of "Lexeme:______"
    line = -1                                        # keeps track of the amount of "Token: _____ Lexeme:______"

    rat22f(list_of_lines, list_of_lexemes, lineNumber,  line)
    return file

# Rule 1 
def rat22f(list_of_lines, list_of_lexemes, lineNumber, line):

    file.append('<Rat22F> ::= <Opt Function Definitions> $ <Opt Declaration List> <Statement List> $')

    file.append('\n' + list_of_lines[line+1])                          # this will file.append out the Token:___ Lexeme:
    global currentLexeme
    global currentToken
    currentLexeme, currentToken = lexer(list_of_lexemes) # get the first token and lexeme

    ###################### Grammar rules ######################
    #if currentLexeme == "function":                        
    OptFuncDef()                    # Rule 2 - for declaring functions before the main body of code
    if currentLexeme == "$":          # signifies the start of the main body of code
        OptDeclarList()                 # Rule 10 - list for declaring variables & etc
        StatementList()                 # Rule 14 - list for intializing variables into statements             
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\nToken:SEPARATOR        Lexeme:$')                         
        if currentLexeme == "$":        # signifies the end of the main body of code
            file.append('\n All done parsing.')
                                  # end of code from lexer
        else:
            file.append('$ expected at line number {}'.format(str(lineNumber)))
            
    else:
        file.append('$ expected at line number {}'.format(str(lineNumber)))
        
    ################## End of Grammar rules ###################        

# Rule 2 
def OptFuncDef():

    file.append('<Opt Function Definitions> ::= <Function Definitions> | <Empty>')
    ###################### Grammar rules ######################
    if currentLexeme == "function":
        FuncDef()       # Rule 3
    else:
        Empty()         # Rule 29
    ################## End of Grammar rules ###################

# Rule 3
def FuncDef():
    file.append('<Function Definitions>  ::= <Function> (<Function Definitions Prime>)')
    ###################### Grammar rules ######################
    Func()
    FuncDefPrime()
    ################## End of Grammar rules ###################

# Rule 3A
def FuncDefPrime():
    file.append('<Function Definition Prime> ::= Epilson | <Function Definitions>')
    if currentLexeme != "function":
        Empty()
    else:
        FuncDef()

# Rule 4
def Func():
    file.append('<Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>')

    global currentLexeme                                              
    global currentToken
    currentLexeme, currentToken = lexer(list_of_lexemes)

    file.append('\n' + list_of_lines[line])          

    if currentToken != "IDENTIFIERS":
        file.append('IDENTIFIER expected at line number {}'.format(str(lineNumber)))
        
    
    IDs()

    if currentLexeme != "(":
        file.append('( SEPARATOR expected at line number {}'.format(str(lineNumber)))
        

    ###################### Grammar rules ######################
    OptParaList()
    OptDeclarList()
    Body()
    ################## End of Grammar rules ###################

# Rule 5
def OptParaList():
    file.append('<Opt Parameter List> ::= <Parameter List> | <Empty>')

    ###################### Grammar rules ######################
    if currentLexeme == "(":
        ParaList()
    else:
        Empty()
    ################## End of Grammar rules ###################


# Rule 6 (Back-Tracking)
def ParaList():
    file.append('<Parameter List> ::= <Parameter> ( <Parameter List Prime> )')

    global currentLexeme
    global currentToken
    currentLexeme, currentToken = lexer(list_of_lexemes)

    file.append('\n' + list_of_lines[line])                                 

    if currentToken != "IDENTIFIERS":
        file.append('Identifier token expected at line number {}'.format(str(lineNumber)))
        

    ###################### Grammar rules ######################
    Para()
    ParaListPrime()

    if currentLexeme != ")":
        file.append('expected ), at line number {}'.format(str(lineNumber)))
        
    ################## End of Grammar rules ###################

# Rule 6A
def ParaListPrime():
    global currentLexeme
    global currentToken
    currentLexeme, currentToken = lexer(list_of_lexemes)

    file.append('\n' + list_of_lines[line]) 

    file.append('<Parameter List Prime> ::= Epsilon | ,<Parameter List>')

    ###################### Grammar rules ######################
    if currentLexeme != ",":
        Empty()
    else:
        ParaList()
    ################## End of Grammar rules ###################

# Rule 7
def Para():
    file.append('<Parameter> ::= <IDs> <Qualifier>')
    ###################### Grammar rules ######################
    IDs()
    Qual()
    ################## End of Grammar rules ###################

# Rule 8
def Qual():
    file.append('<Qualifier> ::= int | boolean | real')
    global currentToken
    ###################### Grammar rules ######################
    if currentToken == "INT":
        file.append('<Qualifier> ::= integer')
    elif currentToken == "BOOL":
        file.append('<Qualifier> ::= boolean')
    elif currentToken == "REAL":
        file.append('<Qualifier> ::= real')
    ################## End of Grammar rules ###################


# Rule 9
def Body():
    global currentLexeme
    file.append('<Body>  ::= { <Statement List> }')
    ###################### Grammar rules ######################
    if currentLexeme == "{":
        global currentToken
        currentLexeme, currentToken = lexer(list_of_lexemes)

        file.append('\n' + list_of_lines[line])

        StatementList()

        if currentLexeme == "}":
            currentLexeme, currentToken = lexer(list_of_lexemes)
            file.append('\n' + list_of_lines[line])
            return
        else:
            file.append('}} expected at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
            
    else:
        file.append('{{} expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
        
    ################## End of Grammar rules ###################

# Rule 10
def OptDeclarList():
    global currentLexeme
    global currentToken
    currentLexeme, currentToken = lexer(list_of_lexemes)

    file.append('\n' + list_of_lines[line]) 

    if currentLexeme == ";":
        file.append('<Opt Declaration List> ::= <Declaration List> | <Empty>')
        DeclarList()
    else:
        Empty()

# Rule 11(LR)
def DeclarList():
    file.append('<Declaration List> ::= <Declaration> ; (<Declaration List Prime>)')
    Declar()
    global currentLexeme
    ###################### Grammar rules ######################
    if currentLexeme == ";":
        global currentToken
        currentLexeme, currentToken = lexer(list_of_lexemes)

        file.append('\n' + list_of_lines[line])
    else:
        DeclarListPrime()
    ################## End of Grammar rules ###################

# Rule 11A
def DeclarListPrime():
    file.append('<Declaration List Prime> ::= <Empty> | <Declaration List>')
    if currentLexeme != ";":
        Empty()
    else:
        DeclarList()

# Rule 12
def Declar():
    file.append('<Declaration> ::= <Qualifier> <IDs>')
    ###################### Grammar rules ######################
    Qual()
    IDs()
    ################## End of Grammar rules ###################


# Rule 13(Back-Tracking)
def IDs():
    file.append('<IDs> ::= <Identifier> <IDs Prime>')                              
    ###################### Grammar rules ######################
    IDsPrime()
    ################## End of Grammar rules ###################

# Rule 13A
def IDsPrime():
    file.append('<IDs Prime> ::= Epsilon | , <IDs>')
    global currentLexeme
    if currentLexeme != ",":
        Empty()
        global currentToken
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])   
    else:
        IDs()

# Rule 14(Back-Tracking)
def StatementList():
    file.append('<Statement List> ::= <Statement> <Statement List Prime>')
    global currentToken
    ###################### Grammar rules ######################
    Statement()
    StatementListPrime()
    ################## End of Grammar rules ###################

# Rule 14A
def StatementListPrime():
    global currentToken
    if currentToken != "KEYWORD":
        Empty()
    else:
        StatementList()

# Rule 15
def Statement():
    file.append('<Statement>::=   <Compound>  |  <Assign>  |   <If>  |  <Return>   | <Print>   |   <Scan>   |  <While>')
    global currentLexeme
    ###################### Grammar rules ######################
    if currentLexeme == "compound":
        Compound()
    elif currentToken == "IDENTIFIERS":
        Assign()
    elif currentLexeme == "if":
        If()
    elif currentLexeme == "return":
        Return()
    elif currentLexeme == "print":
        ourPrint()
    elif currentLexeme == "scan":
        Scan()
    elif currentLexeme == "while":
        ourWhile()
    ################## End of Grammar rules ###################

# Rule 16
def Compound():
    file.append('<Compound> ::= { <Statement List> }')
    global currentLexeme
    global currentToken
    ###################### Grammar rules ######################
    if currentLexeme == "{":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])   
        StatementList()
        if currentLexeme == "}":
            currentLexeme, currentToken = lexer(list_of_lexemes)
            file.append('\n' + list_of_lines[line])
            return
        else:
            file.append('}} expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
            
    else:
        file.append('{{ expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
        
    ################## End of Grammar rules ###################

# Rule 17
def Assign():
    file.append('<Assign> ::= <Identifier> = <Expression>;')
    global currentLexeme
    global currentToken
    ###################### Grammar rules ######################
    if currentToken == "IDENTIFIERS":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])   
        if currentLexeme == "=":
            currentLexeme, currentToken = lexer(list_of_lexemes)
            file.append('\n' + list_of_lines[line])
            Expression()
            if currentLexeme == ";":
                currentLexeme, currentToken = lexer(list_of_lexemes)
                file.append('\n' + list_of_lines[line])
                return
            else:
                file.append('; expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
                
        else:
            file.append('= expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
            
    else:
        file.append('IDENTIFIER expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
        
    ################## End of Grammar rules ###################

# Rule 18(Back-Tracking)
def If():
    file.append('<If> ::= if ( <Condition> ) <Statement> <If Prime>')
    global currentLexeme
    global currentToken
    ###################### Grammar rules ######################
    if currentLexeme == "if":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line]) 
        if currentLexeme == "(":
            currentLexeme, currentToken = lexer(list_of_lexemes)
            file.append('\n' + list_of_lines[line])
            Condition()
            if currentLexeme == ")":
                currentLexeme, currentToken = lexer(list_of_lexemes)
                file.append('\n' + list_of_lines[line])
                Statement()
                if currentLexeme == "endif" or currentLexeme == "else":
                    IfPrime()
                    return
                else:
                    file.append('endif expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
                    
            else:
                file.append(') expected for end of Statement, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
                
        else:
            file.append('( expected for condition, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
            
    else:
        file.append('if expected for if statement, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
        

    ################## End of Grammar rules ###################

def IfPrime():
    file.append('<If Prime> ::= endif | else <Statement> endif')
    global currentLexeme
    global currentToken
    currentLexeme, currentToken = lexer(list_of_lexemes)
    file.append('\n' + list_of_lines[line])
    if currentLexeme == "else":
        Statement()
        IfPrime()

# Rule 19(Back-Tracking)
def Return():
    file.append('<Return> ::= return <Return Prime>')
    ###################### Grammar rules ######################
    ReturnPrime()
    ################## End of Grammar rules ###################

# Rule 19A
def ReturnPrime():
    file.append('<Return Prime> ::= ; | <Expression> ;')
    global currentLexeme
    if currentLexeme == "return":
        global currentToken
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])   
        Expression()
        if currentLexeme != ";":
            file.append('; expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
            
        else:
            currentLexeme, currentToken = lexer(list_of_lexemes)
            file.append('\n' + list_of_lines[line])   

# Rule 20
def ourPrint():
    file.append('<Print> ::= put ( <Expression>);')
    global currentLexeme
    global currentToken
    if currentLexeme == "put":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])
        if currentLexeme == "(":
            currentLexeme, currentToken = lexer(list_of_lexemes)
            file.append('\n' + list_of_lines[line])
            Expression()
            if currentLexeme == ")":
                currentLexeme, currentToken = lexer(list_of_lexemes)
                file.append('\n' + list_of_lines[line])
                if currentLexeme == ";":
                    currentLexeme, currentToken = lexer(list_of_lexemes)
                    file.append('\n' + list_of_lines[line])
                    return
                else:
                    file.append('; expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
                    
            else:
                file.append(') expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
                
        else:
            file.append('( expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
            
    else:
        file.append('put expected for print statement, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
        

# Rule 21
def Scan():
    file.append('<Scan> ::= get ( <IDs> );')
    global currentLexeme
    global currentToken
    if currentLexeme == "get":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])
        if currentLexeme == "(":
            currentLexeme, currentToken = lexer(list_of_lexemes)
            file.append('\n' + list_of_lines[line])
            IDs()
            if currentLexeme == ")":
                currentLexeme, currentToken = lexer(list_of_lexemes)
                file.append('\n' + list_of_lines[line])
                if currentLexeme == ";":
                    currentLexeme, currentToken = lexer(list_of_lexemes)
                    file.append('\n' + list_of_lines[line])
                    return
                else:
                    file.append('; expected for scan statement, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
                    
            else:
                file.append(') expected for scan statement, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
                
        else:
            file.append('( expected for scan statement, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
            
    else:
        file.append('"get" expected for scan statement, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
        

# Rule 22
def ourWhile():
    file.append('<While> ::=  while ( <Condition>  ) <Statement>')
    global currentLexeme
    global currentToken
    if currentLexeme == "while":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])
        if currentLexeme == "(":
            currentLexeme, currentToken = lexer(list_of_lexemes)
            file.append('\n' + list_of_lines[line])
            Condition()
            currentLexeme, currentToken = lexer(list_of_lexemes)
            file.append('\n' + list_of_lines[line])
            if currentLexeme == ")":
                currentLexeme, currentToken = lexer(list_of_lexemes)
                file.append('\n' + list_of_lines[line])
                Statement()
            else:
                file.append(') expected for while statement, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
                
        else:
            file.append('( expected for while statement, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
            
    else:
        file.append('while expected for while statement, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
        


# Rule 23
def Condition():
    file.append('<Condition> ::= <Expression>  <Relop>   <Expression>')
    global currentLexeme
    global currentToken
    global lineNumber
    ###################### Grammar rules ######################
    Expression()
    Relop()
    ExpressionPrime()
    ################## End of Grammar rules ###################

    
# Rule 24
def Relop():
    file.append('<Relop> ::= == | != |  > | < | <= | =>')
    global currentLexeme
    global currentToken
    ###################### Grammar rules ######################
    if currentLexeme == "==" or currentLexeme == "=" or currentLexeme == ">" or currentLexeme == "<" or currentLexeme == "<=" or currentLexeme == "=>":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])
    #else:
          
    ################## End of Grammar rules ###################


# Rule 25(Left Recursion)
def Expression():
    file.append('<Expression> ::= <Term> <Expression Prime>')
    ###################### Grammar rules ######################
    Term()
    ExpressionPrime()
    ################## End of Grammar rules ###################

#Rule 25A
def ExpressionPrime():
    file.append('<Expression Prime> ::= + <Term> <Expression Prime> | - <Term> <Expression Prime> | <Empty>')
    global currentLexeme
    global currentToken
    if currentLexeme == "+" or currentLexeme == "-":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])   
        Term()
        ExpressionPrime()
    else:
        Empty()

# Rule 26(Left Recursion)
def Term():
    file.append('<Term> ::= <Factor> <Term Prime>')
    ###################### Grammar rules ######################
    Factor()
    TermPrime()
    ################## End of Grammar rules ###################

# Rule 26A
def TermPrime():
    file.append('<Term Prime> ::= * <Factor> <Term Prime> | / <Factor> <Term Prime> | <Empty>')
    global currentLexeme
    global currentToken
    if currentLexeme == "*" or currentLexeme == "/":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])
        Factor()
        TermPrime()
    else:
        Empty()

# Rule 27
def Factor():
    file.append('<Factor> ::= - <Primary> | <Primary>')
    global currentLexeme
    global currentToken
    ###################### Grammar rules ######################
    if currentLexeme == "-":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])
    else:
        Primary()
    ################## End of Grammar rules ###################

# Rule 28
def Primary():
    file.append('<Primary> ::= <Identifier> | <Integer> | <Identifier> ( <IDs> ) | ( <Expression> ) | <Real> | true | false')
    global currentLexeme
    global currentToken
    ###################### Grammar rules ######################
    if currentToken == "INT" or currentToken == "REAL":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])
    elif currentLexeme == "true":
        file.append('<Primary> ::= true')
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])
    elif currentLexeme == "false":
        file.append('<Primary> ::= false')
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])
    elif currentLexeme == "(":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])
        Expression()
        if currentLexeme == ")":
            currentLexeme, currentToken = lexer(list_of_lexemes)
            file.append('\n' + list_of_lines[line])
        else:
            file.append(') expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
            
    elif currentToken == "IDENTIFIERS":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])
        if currentLexeme == "(":
            currentLexeme, currentToken = lexer(list_of_lexemes)
            file.append('\n' + list_of_lines[line])
            IDs()
            if currentLexeme == ")":
                currentLexeme, currentToken = lexer(list_of_lexemes)
                file.append('\n' + list_of_lines[line])
            else:
                file.append(') expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
                
    else:  
        file.append('Error at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
        
    ################## End of Grammar rules ###################
# Rule 29
def Empty():
    file.append('<Empty> ::= Epsilon')
