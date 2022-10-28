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
            FuncDef()
        #TO-DO: elif for Empty(R29)? 
        
        lineNumber += 2                                   # Increment by 2 to get to the next token
        print("")                                         # line break
    ################## End of Grammar rules ###################

# Rule 3 (LR)
def FuncDef(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Function Definitions>  ::=")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
# Rule 4
def Func(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:

        print("<Function> ::=")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################

# Rule 5
def OptParaList(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:

        print("<Opt Parameter List> ::= ")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################

# Rule 6 (LR)
def ParaList(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:

        print("<Parameter List> ::= ")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################

# Rule 7
def Para(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:

        print("<Parameter> ::= ")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################

# Rule 8
def Qual(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:

        print("<Qualifier> ::= ")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################

# Rule 9
def Body(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:

        print("<Body>  ::= ")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################

# Rule 10
def OptDeclarList(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Opt Declaration List> ::= ")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################

# Rule 11(LR)
def DeclarList(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Declaration List> ::= ")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################

# Rule 12
def Declar(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Declaration> ::= ")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################

# Rule 13(LR)
def IDs(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<IDs> ::= ")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################

# Rule 14(LR)
def StatementList(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Statement List> ::= ")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################

# Rule 15
def Statement(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Statement> ::= ")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################

# Rule 16
def Compound(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Compound> ::= ")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################

# Rule 17
def Assign(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Assign> ::= ")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################

# Rule 18(LR)
def If(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<If> ::= ")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################

# Rule 19(LR)
def Return(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Return> ::= ")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################

# Rule 20
def Print(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Print> ::= ")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################

# Rule 21
def Scan(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Scan> ::= ")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################

# Rule 22
def While(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<While> ::= ")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################

# Rule 23
def Condition(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Condition> ::= ")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################

# Rule 24
def Relop(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Relop> ::= ")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################

# Rule 25(LR)
def Expression(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Expression> ::= ")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################

# Rule 26(LR)
def Term(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Term> ::= ")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################

# Rule 27
def Factor(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Factor> ::= ")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################

# Rule 28
def Primary(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Primary> ::= ")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################

# Rule 29
def Empty(list_of_lines, list_of_lexemes, lineNumber):
    for line in list_of_lines:
        print("<Empty> ::= ")
        currentLexeme, currentToken = lexer(lineNumber, list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################