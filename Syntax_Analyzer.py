def lexer(lineNumber, list_of_lexemes):
    """Will return the token based on the line number."""
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

    list_of_lines = parseFile.splitlines()          # each line here is "Token: _____ Lexeme:______"
    list_of_lexemes = parseFile.split()             # each lexeme here is "Lexeme:______"
    lineNumber = 1

    rat22f(list_of_lines, list_of_lexemes, lineNumber)

# Rule 1 (<Rat22F>  ::=   <Opt Function Definitions>   $  <Opt Declaration List>  <Statement List>  $)
def rat22f(list_of_lines, list_of_lexemes, lineNumber):

    print("<Rat22F> ::= <Opt Function Definitions> $ <Opt Declaration List> <Statement List> $")  # only needs to be printed once

    print("\n" + list_of_lines[lineNumber-1])                                 # this will print out the Token:___ Lexeme:
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
            exit()                      # end of code from lexer
        else:
            print("$ expected at line number " + str(lineNumber))
            exit()
    else:
        print("$ expected at line number " + str(lineNumber))
        exit()
    ################## End of Grammar rules ###################        

# Rule 2 (<Opt Function Definitions> ::= <Function Definitions> 	|  <Empty>)
def OptFuncDef():

    print("<Opt Function Definitions> ::= <Function Definitions> | <Empty>")
    ###################### Grammar rules ######################
    if currentLexeme == "function":
        FuncDef()       # Rule 3
    else:
        Empty()         # Rule 29
    ################## End of Grammar rules ###################

# Rule 3 (<Function Definitions>  ::= <Function> (<Function Definitions PRIME>))
def FuncDef():
    print("<Function Definitions>  ::= <Function> (<Function Definitions Prime>)")
    ###################### Grammar rules ######################
    Func()
    FuncDefPrime()
    ################## End of Grammar rules ###################

# Rule 3A
def FuncDefPrime():
    print("<Function Definition Prime> ::= Epilson | <Function Definitions>")
    if currentLexeme != "function":
        Empty()
    else:
        FuncDef()

# Rule 4
def Func():
    print("<Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>")

    global lineNumber
    lineNumber += 2                                                  # Increment by 2 to get to the next token & lexeme
    global currentLexeme
    global currentToken
    currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    print("\n" + list_of_lines[lineNumber-2])                                 # this will print out the Token:___ Lexeme:

    ###################### Grammar rules ######################
    OptParaList()
    OptDeclarList()
    Body()
    ################## End of Grammar rules ###################

# Rule 5
def OptParaList():
    print("<Opt Parameter List> ::= <Parameter List> | <Empty>")

    global lineNumber
    lineNumber += 2                                                 # Increment by 2 to get to the next token & lexeme
    global currentLexeme
    global currentToken
    currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)

    ###################### Grammar rules ######################
    if currentLexeme == "(":
        ParaList()
    else:
        Empty()
    ################## End of Grammar rules ###################


# Rule 6 (LR)
def ParaList():
    print("<Parameter List> ::= <Parameter> ( <Parameter List Prime> )")

    global lineNumber
    lineNumber += 2                                                  # Increment by 2 to get to the next token & lexeme
    global currentLexeme
    global currentToken
    currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    print("\n" + list_of_lines[lineNumber-4])                                 # this will print out the Token:___ Lexeme:

    ###################### Grammar rules ######################
    Para()
    ParaListPrime()

    if currentLexeme != ")":
        print("expected ), on line number " + str(lineNumber))
        exit()
    ################## End of Grammar rules ###################

# Rule 6A
def ParaListPrime():
    print("<Parameter List Prime> ::= Episilon | ,<Parameter List>")

    ###################### Grammar rules ######################
    if currentLexeme != ",":
        Empty()
    else:
        ParaList()
    ################## End of Grammar rules ###################

# Rule 7
def Para():
    print("<Parameter> ::= <IDs> <Qualifier>")
    ###################### Grammar rules ######################
    IDs()
    Qual()
    ################## End of Grammar rules ###################

# Rule 8
def Qual():
    print("<Qualifier> ::= integer | boolean | real")
    ###################### Grammar rules ######################
    if currentToken == "INT":
        print("integer")
    elif currentToken == "BOOL":
        print("boolean")
    elif currentToken == "REAL":
        print("real")
    ################## End of Grammar rules ###################


# Rule 9
def Body():

    print("<Body>  ::= { <Statement List> }")
    ###################### Grammar rules ######################
    if currentLexeme == "{":
        StatementList()
    else:
        print("{ expected, error in line " + str(lineNumber))
        exit()
    ################## End of Grammar rules ###################

# Rule 10
def OptDeclarList():
    print("<Opt Declaration List> ::= <Declaration List> | <Empty>")

    ###################### Grammar rules ######################
    if currentToken == "INT" or "BOOL" or "REAL":
        DeclarList()
    else:
        Empty()
    ################## End of Grammar rules ###################


# Rule 11(LR)
def DeclarList():

    print("<Declaration List> ::= <Declaration> ; (<Declaration List Prime>)")

    ###################### Grammar rules ######################
    Declar()
    DeclarListPrime()
    ################## End of Grammar rules ###################

# Rule 11A
def DeclarListPrime():
    if currentToken != "INT" or "BOOL" or "REAL" or "IDENTIFIERS":
        Empty()
    else:
        DeclarList()

# Rule 12
def Declar():
    print("<Declaration> ::= <Qualifier> <IDs>")
    ###################### Grammar rules ######################
    Qual()
    IDs()
    ################## End of Grammar rules ###################


# Rule 13(LR)
def IDs():
    print("<IDs> ::= <Identifier><IDs Prime>")

    global lineNumber
    lineNumber += 2                                                  # Increment by 2 to get to the next token & lexeme
    global currentLexeme
    global currentToken
    currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)

    ###################### Grammar rules ######################
    # note, the ID was already printed before this function call, therefore we do not need a Identifier() function
    IDsPrime()
    ################## End of Grammar rules ###################

# Rule 13A
def IDsPrime():
    print("<IDs Prime> ::= Epilson | ,<IDs>")
    if currentLexeme != ",":
        Empty()
    else:
        IDs()
        print("\n" + list_of_lines[lineNumber-6])                                 # this will print out the Token:___ Lexeme:

# Rule 14(LR)
def StatementList():
    print("<Statement List> ::= <Statement> <Statement List Prime>")

    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
"""
# Rule 15
def Statement():
    for line in list_of_lines:
        print("<Statement> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################
    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break
# Rule 16
def Compound():
    for line in list_of_lines:
        print("<Compound> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################
    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break
# Rule 17
def Assign():
    for line in list_of_lines:
        print("<Assign> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################
    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break
# Rule 18(LR)
def If():
    for line in list_of_lines:
        print("<If> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################
    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break
# Rule 19(LR)
def Return():
    for line in list_of_lines:
        print("<Return> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################
    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break
# Rule 20
def Print():
    for line in list_of_lines:
        print("<Print> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################
    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break
# Rule 21
def Scan():
    for line in list_of_lines:
        print("<Scan> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################
    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break
# Rule 22
def While():
    for line in list_of_lines:
        print("<While> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################
    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break
# Rule 23
def Condition():
    for line in list_of_lines:
        print("<Condition> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################
    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break
# Rule 24
def Relop():
    for line in list_of_lines:
        print("<Relop> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################
    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break
# Rule 25(LR)
def Expression():
    print('<Expression> ::= <Term> <Expression PRIME>')
    for line in list_of_lines:
        print("<Expression> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################
    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break
# Rule 26(LR)
def Term():
    print('<Term> ::= <Factor> <Term PRIME>')
    for line in list_of_lines:
        print("<Term> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################
    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break
# Rule 27
def Factor():
    for line in list_of_lines:
        print("<Factor> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################
    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break
# Rule 28
def Primary():
    for line in list_of_lines:
        print("<Primary> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################
    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break
"""
# Rule 29
def Empty():
    print("<Empty> ::= ")