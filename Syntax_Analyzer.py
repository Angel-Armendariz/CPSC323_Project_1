file = []                                                     # this file will be returned to main.py for it be tured into "parsedFile.txt"

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

    global currentLexeme                                              
    global currentToken
    currentLexeme, currentToken = lexer(list_of_lexemes)

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


# Rule 6 (Back-Tracking)
def ParaList():
    file.append('<Parameter List> ::= <Parameter> ( <Parameter List Prime> )')

    global currentLexeme
    global currentToken
    currentLexeme, currentToken = lexer(list_of_lexemes)

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
    global currentLexeme
    global currentToken
    currentLexeme, currentToken = lexer(list_of_lexemes)

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
            exit()
    else:
        file.append('{{} expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
        exit()
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
    file.append('<IDs Prime> ::= Epilson | , <IDs>')
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
    elif currentLexeme == "assign":
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
            exit()
    else:
        file.append('{{ expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
        exit()
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
                exit()
        else:
            file.append('= expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
            exit()
    else:
        file.append('IDENTIFIER expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
        exit()
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
                    exit()
            else:
                file.append(') expected for end of Statement, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
                exit()
        else:
            file.append('( expected for condition, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
            exit()
    else:
        file.append('if expected for if statement, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
        exit()

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
            exit()
        else:
            currentLexeme, currentToken = lexer(list_of_lexemes)
            file.append('\n' + list_of_lines[line])   
"""
# Rule 20
def ourPrint():
    print("put ( <Expression>);")

    global lineNumber
    lineNumber += 2                                                  # Increment by 2 to get to the next token & lexeme
    global line
    line += 1
    global currentLexeme
    global currentToken
    currentLexeme, currentToken = lexer(  list_of_lexemes)
    print("\n" + list_of_lines[line])                                

    if currentLexeme != "(":
        print("( SEPARATOR expected on line " + str(lineNumber))
        exit()
    ###################### Grammar rules ######################
    Expression()                                      # Rule 25

    if currentLexeme != ")":
        print("expected ), on line number " + str(lineNumber))
        exit()
    
    if currentLexeme != ";":
        print("expected ;, on line number " + str(lineNumber))
        exit()
    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    file.append("")                                         # line break

# Rule 21
def Scan():
    print("<Scan> ::=    get ( <IDs> );")

    global lineNumber
    lineNumber += 2                                                  # Increment by 2 to get to the next token & lexeme
    global line
    line += 1
    global currentLexeme
    global currentToken
    currentLexeme, currentToken = lexer(  list_of_lexemes)
    print("\n" + list_of_lines[line])                                

    if currentLexeme != "(":
        print("( SEPARATOR expected on line " + str(lineNumber))
        exit()
    ###################### Grammar rules ######################
    IDs()                                             # Rule 13

    if currentLexeme != ")":
        print("expected ), on line number " + str(lineNumber))
        exit()
    
    if currentLexeme != ";":
        print("expected ;, on line number " + str(lineNumber))
        exit()
    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    file.append("")                                         # line break

# Rule 22
def ourWhile():
    print("<While> ::=  while ( <Condition>  )  <Statement>")

    global lineNumber
    lineNumber += 2                                                  # Increment by 2 to get to the next token & lexeme
    global line
    line += 1
    global currentLexeme
    global currentToken
    currentLexeme, currentToken = lexer(  list_of_lexemes)
    print("\n" + list_of_lines[line])                                

    if currentLexeme != "(":
        print("( SEPARATOR expected on line " + str(lineNumber))
        exit()
    ###################### Grammar rules ######################
    Condition()                                       # Rule 23

    if currentLexeme != ")":
        print("expected ), on line number " + str(lineNumber))
        exit()
    
    Statement()
    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break
# Rule 23
def Condition():
    for line in list_of_lines:
        file.append("<Condition> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(  list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    file.append("")                                         # line break

# Rule 24
def Relop():
    for line in list_of_lines:
        file.append("<Relop> ::= " + line + "\n")
        currentLexeme, currentToken = lexer(  list_of_lexemes)
    ###################### Grammar rules ######################

    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    file.append("")                                         # line break

"""
# Rule 25(Left Recursion)
def Expression():
    file.append('<Expression> ::= <Term> <Expression Prime>')
    ###################### Grammar rules ######################
    Term()
    ExpressionPrime()
    ################## End of Grammar rules ###################

#Rule 25A
def ExpressionPrime():
    file.append('<Expression> ::= + <Term> <Expression Prime> | - <Term> <Expression Prime> | <Empty>')
    global currentLexeme
    global currentToken
    if currentLexeme == "+" or currentLexeme == "-":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])   
        if Term():
            ExpressionPrime()
        else:
            file.append('+  or - expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
            exit()
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
    file.append('<Factor> ::= - <Priamry> | <Primary>')
    global currentLexeme
    global currentToken
    ###################### Grammar rules ######################
    if currentLexeme == "-":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])
        Primary()
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
                return
            else:
                file.append(') expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
                exit()
        else:
            file.append('( expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
            exit()
    elif currentLexeme == "(":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])
        Expression()
        if currentLexeme == ")":
            currentLexeme, currentToken = lexer(list_of_lexemes)
            file.append('\n' + list_of_lines[line])
            return
        else:
            file.append(') expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
            exit()
    elif currentLexeme == "true":
        file.append('<Primary> ::= true')
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])
    elif currentLexeme == "false":
        file.append('<Primary> ::= false')
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])
    else:  
        file.append('Error at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
        exit()
    ################## End of Grammar rules ###################
# Rule 29
def Empty():
    file.append('<Empty> ::= Epilson')
