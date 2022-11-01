def lexer(lineNumber, list_of_lexemes):
    """Will return the token based on the line number."""
    longLexeme = list_of_lexemes[lineNumber]                  # lexeme = "Lexeme:___" part from the from the file
    lexeme = longLexeme[7:]
    
    longToken = list_of_lexemes[lineNumber -1]
    token = longToken[6:]                                     # token  = the part after the colon ":" from the file 

    return lexeme, token

def parse(parseFile):
    """Will take the inputted file and parse based on grammar rules."""

    list_of_lines = parseFile.splitlines()
    list_of_lexemes = parseFile.split()
    lineNumber = 1

    rat22f(list_of_lines, list_of_lexemes, lineNumber)

# Rule 1
def rat22f(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:

        print("<Rat22F> ::= " + line + "\n")                                       # will print the Token:___ Lexeme:___
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)

        ###################### Grammar rules ######################
        if currentToken:
            OptFuncDef()                        # Rule 2
            if currentLexeme == "$":             
                OptDeclarList()                 # Rule 10
                StatementList()                 # Rule 14
                if currentToken == "$":
                    exit()                      # end of code from lexer
            else:
                print("$ expected at line number " + str(lineNumber))
                exit()

        ################## End of Grammar rules ###################
        lineNumber += 2                                   # Increment by 2 to get to the next token
        print("")                                         # line break

# Rule 2
def OptFuncDef(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:

        print("<Opt Function Definitions> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################
        if currentToken:
            FuncDef()       # Rule 3
        else:
            Empty()         # Rule 29
    ################## End of Grammar rules ###################
        lineNumber += 2                                   # Increment by 2 to get to the next token
        print("")                                         # line break

# Rule 3 (LR)
def FuncDef(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Function Definitions>  ::=" + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break
# Rule 4
def Func(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:

        print("<Function> ::=" + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break

# Rule 5
def OptParaList(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:

        print("<Opt Parameter List> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break

# Rule 6 (LR)
def ParaList(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:

        print("<Parameter List> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break

# Rule 7
def Para(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:

        print("<Parameter> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break

# Rule 8
def Qual(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:

        print("<Qualifier> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break

# Rule 9
def Body(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:

        print("<Body>  ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break

# Rule 10
def OptDeclarList(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Opt Declaration List> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break

# Rule 11(LR)
def DeclarList(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Declaration List> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break

# Rule 12
def Declar(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Declaration> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break

# Rule 13(LR)
def IDs(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<IDs> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break

# Rule 14(LR)
def StatementList(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Statement List> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break

# Rule 15
def Statement(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Statement> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break

# Rule 16
def Compound(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Compound> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break

# Rule 17
def Assign(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Assign> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break

# Rule 18(LR)
def If(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<If> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break

# Rule 19(LR)
def Return(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Return> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break

# Rule 20
def Print(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Print> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break

# Rule 21
def Scan(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Scan> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break

# Rule 22
def While(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<While> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break

# Rule 23
def Condition(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Condition> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break

# Rule 24
def Relop(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Relop> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break

# Rule 25(LR)
def Expression(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Expression> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break

# Rule 26(LR)
def Term(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Term> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break

# Rule 27
def Factor(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Factor> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break

# Rule 28
def Primary(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Primary> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break

# Rule 29
def Empty(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Empty> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

# Rule 14
def StatementList():
    print("<Statement List> ::= <Statement> | <Statement><Statement List>")
    print("gotta fix this left recursion")