file = []                                                     # this file will be returned to main.py for it be tured into "parsedFile.txt"

def lexer(lineNumber, list_of_lexemes):
    """Will return the token based on the line number."""

    lineNumber += 2                                                  
    global line
    line += 1

    longLexeme = list_of_lexemes[lineNumber]                  # lexeme = "Lexeme:___" part from the from the file
    lexeme = longLexeme[7:]
    
    longToken = list_of_lexemes[lineNumber -1]
    token = longToken[6:]                                     # token  = the part after the colon ":" from the file 

    return lexeme, token

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

    rat22f(list_of_lines, list_of_lexemes, lineNumber, line)

    return file

# Rule 1 
def rat22f(list_of_lines, list_of_lexemes, lineNumber, line):

    file.append('<Rat22F> ::= <Opt Function Definitions> $ <Opt Declaration List> <Statement List> $')

    file.append('\n' + list_of_lines[line])                          # this will file.append out the Token:___ Lexeme:
    global currentLexeme
    global currentToken
    currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes) # get the first token and lexeme

    ###################### Grammar rules ######################
    if currentLexeme == "function":                        
        OptFuncDef()                    # Rule 2 - for declaring functions before the main body of code
    elif currentLexeme == "$":          # signifies the start of the main body of code
        OptDeclarList()                 # Rule 10 - list for declaring variables & etc
        StatementList()                 # Rule 14 - list for intializing variables into statements             
        if currentLexeme == "$":        # signifies the end of the main body of code
            file.append('\n All done parsing.')
            exit()                      # end of code from lexer
        else:
            file.append('$ expected at line number {}'.format(str(lineNumber)))
            exit()
    else:
        file.append('$ expected at line number {}'.format(str(lineNumber)))
        exit()
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

    global lineNumber                                                   # use these next four lines whenever
    global currentLexeme                                                # you want to the next token and lexeme
    global currentToken
    currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)

    file.append('\n' + list_of_lines[line])          

    if currentToken != "IDENTIFIERS":
        file.append('IDENTIFIER expected at line number {}'.format(str(lineNumber)))
        exit()
    
    IDs()

    if currentLexeme != "(":
        file.append('( SEPARATOR expected at line number {}'.format(str(lineNumber)))
        exit()

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


# Rule 6 (LR)
def ParaList():
    file.append('<Parameter List> ::= <Parameter> ( <Parameter List Prime> )')

    global lineNumber
    global currentLexeme
    global currentToken
    currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)

    file.append('\n' + list_of_lines[line])                                 

    if currentToken != "IDENTIFIERS":
        file.append('Identifier token expected at line number {}'.format(str(lineNumber)))
        exit()

    ###################### Grammar rules ######################
    Para()
    ParaListPrime()

    if currentLexeme != ")":
        file.append('expected ), at line number {}'.format(str(lineNumber)))
        exit()
    ################## End of Grammar rules ###################

# Rule 6A
def ParaListPrime():

    global lineNumber
    global currentLexeme
    global currentToken
    currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)

    file.append('\n' + list_of_lines[line]) 

    file.append('<Parameter List Prime> ::= Episilon | ,<Parameter List>')

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
        global lineNumber
        global currentToken
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)

        file.append('\n' + list_of_lines[line])

        StatementList()

        if currentLexeme == "}":
            currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
            file.append('\n' + list_of_lines[line])
            return
        else:
            file.append('}} expected at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
            
    else:
        file.append('{ expected, error in line ' + str(lineNumber) + ' , instead of ' + list_of_lines[line])
        exit()
    ################## End of Grammar rules ###################

# Rule 10
def OptDeclarList():
    global currentLexeme
    global lineNumber
    global currentToken
    currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)

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
        global lineNumber
        global currentToken
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)

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


# Rule 13(LR)
def IDs():
    file.append('<IDs> ::= <Identifier> <IDs Prime>')                              
    ###################### Grammar rules ######################
    IDsPrime()
    ################## End of Grammar rules ###################

# Rule 13A
def IDsPrime():
    file.append('<IDs Prime> ::= Epilson | , <IDs>')
    global currentLexeme
    
    if currentLexeme != ",":
        Empty()
        global lineNumber
        global currentToken
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)

        file.append('\n' + list_of_lines[line])   
    else:
        IDs()

# Rule 14(LR)
def StatementList():
    file.append('<Statement List> ::= <Statement> <Statement List Prime>')

    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
"""
# Rule 15
def Statement():
    for line in list_of_lines:
        file.append("<Statement> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    file.append("")                                         # line break

# Rule 16
def Compound():
    for line in list_of_lines:
        file.append("<Compound> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    file.append("")                                         # line break

# Rule 17
def Assign():
    for line in list_of_lines:
        file.append("<Assign> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    file.append("")                                         # line break

# Rule 18(LR)
def If():
    for line in list_of_lines:
        file.append("<If> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    file.append("")                                         # line break

# Rule 19(LR)
def Return():
    for line in list_of_lines:
        file.append("<Return> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    file.append("")                                         # line break

# Rule 20
def file.append():
    for line in list_of_lines:
        file.append("<file.append> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    file.append("")                                         # line break

# Rule 21
def Scan():
    for line in list_of_lines:
        file.append("<Scan> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    file.append("")                                         # line break

# Rule 22
def While():
    for line in list_of_lines:
        file.append("<While> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    file.append("")                                         # line break

# Rule 23
def Condition():
    for line in list_of_lines:
        file.append("<Condition> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    file.append("")                                         # line break

# Rule 24
def Relop():
    for line in list_of_lines:
        file.append("<Relop> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    file.append("")                                         # line break

# Rule 25(LR)
def Expression():
    for line in list_of_lines:
        file.append("<Expression> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    file.append("")                                         # line break

# Rule 26(LR)
def Term():
    for line in list_of_lines:
        file.append("<Term> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    file.append("")                                         # line break

# Rule 27
def Factor():
    for line in list_of_lines:
        file.append("<Factor> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    file.append("")                                         # line break

# Rule 28
def Primary():
    for line in list_of_lines:
        file.append("<Primary> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    file.append("")                                         # line break
"""
# Rule 29
def Empty():
    file.append("<Empty> ::= Epilson")
