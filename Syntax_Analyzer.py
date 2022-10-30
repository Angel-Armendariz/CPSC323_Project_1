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
def OptFuncDef():
    print("<Opt Function Definitions> ::= <Function Definitions> | <Empty>")

# Rule 10
def OptDeclarList():
    print("<Opt Declaration List> ::= <Declaration List> | <Empty>")

# Rule 14
def StatementList():
    print("<Statement List> ::= <Statement> | <Statement><Statement List>")
    print("<Statement List> ::= <Empty> | <Statement List>")
    print("gotta fix this left recursion")