file = open("parsedFile.txt", "w")                                                    # this file will be returned to main.py for it be tured into "parsedFile.txt"
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

    file.write('\n <Rat22F> ::= <Opt Function Definitions> $ <Opt Declaration List> <Statement List> $')

    file.write('\n' + list_of_lines[line+1])                          # this will file.write out the Token:___ Lexeme:
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
            file.write('\n All done parsing.')
            file.close 
                                   # end of code from lexer
        else:
            file.write('\n $ expected at line number {}'.format(str(lineNumber)))
            file.close 
             
    else:
        file.write('\n $ expected at line number {}'.format(str(lineNumber)))
        file.close 
         
    ################## End of Grammar rules ###################        

# Rule 2 
def OptFuncDef():

    file.write('\n <Opt Function Definitions> ::= <Function Definitions> | <Empty>')
    ###################### Grammar rules ######################
    if currentLexeme == "function":
        FuncDef()       # Rule 3
    else:
        Empty()         # Rule 29
    ################## End of Grammar rules ###################

# Rule 3
def FuncDef():
    file.write('\n <Function Definitions>  ::= <Function> (<Function Definitions Prime>)')
    ###################### Grammar rules ######################
    Func()
    FuncDefPrime()
    ################## End of Grammar rules ###################

# Rule 3A
def FuncDefPrime():
    file.write('\n <Function Definition Prime> ::= Epilson | <Function Definitions>')
    if currentLexeme != "function":
        Empty()
    else:
        FuncDef()

# Rule 4
def Func():
    file.write('\n <Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>')

    global currentLexeme                                              
    global currentToken
    currentLexeme, currentToken = lexer(list_of_lexemes)

    file.write('\n' + list_of_lines[line])          

    if currentToken != "IDENTIFIERS":
        file.write('\n IDENTIFIER expected at line number {}'.format(str(lineNumber)))
        file.close
         
    
    IDs()

    if currentLexeme != "(":
        file.write('\n ( SEPARATOR expected at line number {}'.format(str(lineNumber)))
        file.close 
         

    ###################### Grammar rules ######################
    OptParaList()
    OptDeclarList()
    Body()
    ################## End of Grammar rules ###################

# Rule 5
def OptParaList():
    file.write('\n<Opt Parameter List> ::= <Parameter List> | <Empty>')

    ###################### Grammar rules ######################
    if currentLexeme == "(":
        ParaList()
    else:
        Empty()
    ################## End of Grammar rules ###################


# Rule 6 (Back-Tracking)
def ParaList():
    file.write('\n<Parameter List> ::= <Parameter> ( <Parameter List Prime> )')

    global currentLexeme
    global currentToken
    currentLexeme, currentToken = lexer(list_of_lexemes)

    file.write('\n' + list_of_lines[line])                                 

    if currentToken != "IDENTIFIERS":
        file.write('\nIdentifier token expected at line number {}'.format(str(lineNumber)))
        file.close 
         

    ###################### Grammar rules ######################
    Para()
    ParaListPrime()

    if currentLexeme != ")":
        file.write('\nexpected ), at line number {}'.format(str(lineNumber)))
        file.close 
         
    ################## End of Grammar rules ###################

# Rule 6A
def ParaListPrime():
    global currentLexeme
    global currentToken
    currentLexeme, currentToken = lexer(list_of_lexemes)

    file.write('\n' + list_of_lines[line]) 

    file.write('\n<Parameter List Prime> ::= Epsilon | ,<Parameter List>')

    ###################### Grammar rules ######################
    if currentLexeme != ",":
        Empty()
    else:
        ParaList()
    ################## End of Grammar rules ###################

# Rule 7
def Para():
    file.write('\n<Parameter> ::= <IDs> <Qualifier>')
    ###################### Grammar rules ######################
    IDs()
    Qual()
    ################## End of Grammar rules ###################

# Rule 8
def Qual():
    file.write('\n<Qualifier> ::= int | boolean | real')
    global currentToken
    ###################### Grammar rules ######################
    if currentToken == "INT":
        file.write('\n<Qualifier> ::= integer')
    elif currentToken == "BOOL":
        file.write('\n<Qualifier> ::= boolean')
    elif currentToken == "REAL":
        file.write('\n<Qualifier> ::= real')
    ################## End of Grammar rules ###################


# Rule 9
def Body():
    global currentLexeme
    file.write('\n<Body>  ::= { <Statement List> }')
    ###################### Grammar rules ######################
    if currentLexeme == "{":
        global currentToken
        currentLexeme, currentToken = lexer(list_of_lexemes)

        file.write('\n' + list_of_lines[line])

        StatementList()

        if currentLexeme == "}":
            currentLexeme, currentToken = lexer(list_of_lexemes)
            file.write('\n' + list_of_lines[line])
            return
        else:
            file.write('\n}} expected at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
            file.close 
             
    else:
        file.write('\n{{} expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
        file.close 
         
    ################## End of Grammar rules ###################

# Rule 10
def OptDeclarList():
    global currentLexeme
    global currentToken
    currentLexeme, currentToken = lexer(list_of_lexemes)

    file.write('\n' + list_of_lines[line]) 

    if currentLexeme == ";":
        file.write('\n<Opt Declaration List> ::= <Declaration List> | <Empty>')
        DeclarList()
    else:
        Empty()

# Rule 11(LR)
def DeclarList():
    file.write('\n<Declaration List> ::= <Declaration> ; (<Declaration List Prime>)')
    Declar()
    global currentLexeme
    ###################### Grammar rules ######################
    if currentLexeme == ";":
        global currentToken
        currentLexeme, currentToken = lexer(list_of_lexemes)

        file.write('\n' + list_of_lines[line])
    else:
        DeclarListPrime()
    ################## End of Grammar rules ###################

# Rule 11A
def DeclarListPrime():
    file.write('\n<Declaration List Prime> ::= <Empty> | <Declaration List>')
    if currentLexeme != ";":
        Empty()
    else:
        DeclarList()

# Rule 12
def Declar():
    file.write('\n<Declaration> ::= <Qualifier> <IDs>')
    ###################### Grammar rules ######################
    Qual()
    IDs()
    ################## End of Grammar rules ###################


# Rule 13(Back-Tracking)
def IDs():
    file.write('\n<IDs> ::= <Identifier> <IDs Prime>')                              
    ###################### Grammar rules ######################
    IDsPrime()
    ################## End of Grammar rules ###################

# Rule 13A
def IDsPrime():
    file.write('\n<IDs Prime> ::= Epsilon | , <IDs>')
    global currentLexeme
    if currentLexeme != ",":
        Empty()
        global currentToken
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.write('\n' + list_of_lines[line])   
    else:
        IDs()

# Rule 14(Back-Tracking)
def StatementList():
    file.write('\n<Statement List> ::= <Statement> <Statement List Prime>')
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
    file.write('\n<Statement>::=   <Compound>  |  <Assign>  |   <If>  |  <Return>   | <Print>   |   <Scan>   |  <While>')
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
    file.write('\n<Compound> ::= { <Statement List> }')
    global currentLexeme
    global currentToken
    ###################### Grammar rules ######################
    if currentLexeme == "{":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.write('\n' + list_of_lines[line])   
        StatementList()
        if currentLexeme == "}":
            currentLexeme, currentToken = lexer(list_of_lexemes)
            file.write('\n' + list_of_lines[line])
            return
        else:
            file.write('\n}} expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
            file.close 
             
    else:
        file.write('\n{{ expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
        file.close 
         
    ################## End of Grammar rules ###################

# Rule 17
def Assign():
    file.write('\n<Assign> ::= <Identifier> = <Expression>;')
    global currentLexeme
    global currentToken
    ###################### Grammar rules ######################
    if currentToken == "IDENTIFIERS":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.write('\n' + list_of_lines[line])   
        if currentLexeme == "=":
            currentLexeme, currentToken = lexer(list_of_lexemes)
            file.write('\n' + list_of_lines[line])
            Expression()
            if currentLexeme == ";":
                currentLexeme, currentToken = lexer(list_of_lexemes)
                file.write('\n' + list_of_lines[line])
                return
            else:
                file.write('\n; expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
                file.close 
                 
        else:
            file.write('\n= expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
            file.close 
             
    else:
        file.write('\nIDENTIFIER expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
        file.close 
         
    ################## End of Grammar rules ###################

# Rule 18(Back-Tracking)
def If():
    file.write('\n<If> ::= if ( <Condition> ) <Statement> <If Prime>')
    global currentLexeme
    global currentToken
    ###################### Grammar rules ######################
    if currentLexeme == "if":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.write('\n' + list_of_lines[line]) 
        if currentLexeme == "(":
            currentLexeme, currentToken = lexer(list_of_lexemes)
            file.write('\n' + list_of_lines[line])
            Condition()
            if currentLexeme == ")":
                currentLexeme, currentToken = lexer(list_of_lexemes)
                file.write('\n' + list_of_lines[line])
                Statement()
                if currentLexeme == "endif" or currentLexeme == "else":
                    IfPrime()
                    return
                else:
                    file.write('\nendif expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
                    file.close 
                     
            else:
                file.write('\n) expected for end of Statement, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
                file.close 
                 
        else:
            file.write('\n( expected for condition, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
            file.close 
             
    else:
        file.write('\nif expected for if statement, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
        file.close 
         

    ################## End of Grammar rules ###################

def IfPrime():
    file.write('\n<If Prime> ::= endif | else <Statement> endif')
    global currentLexeme
    global currentToken
    currentLexeme, currentToken = lexer(list_of_lexemes)
    file.write('\n' + list_of_lines[line])
    if currentLexeme == "else":
        Statement()
        IfPrime()

# Rule 19(Back-Tracking)
def Return():
    file.write('\n<Return> ::= return <Return Prime>')
    ###################### Grammar rules ######################
    ReturnPrime()
    ################## End of Grammar rules ###################

# Rule 19A
def ReturnPrime():
    file.write('\n<Return Prime> ::= ; | <Expression> ;')
    global currentLexeme
    if currentLexeme == "return":
        global currentToken
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.write('\n' + list_of_lines[line])   
        Expression()
        if currentLexeme != ";":
            file.write('\n; expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
            file.close 
             
        else:
            currentLexeme, currentToken = lexer(list_of_lexemes)
            file.write('\n' + list_of_lines[line])   

# Rule 20
def ourPrint():
    file.write('\n<Print> ::= put ( <Expression>);')
    global currentLexeme
    global currentToken
    if currentLexeme == "put":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.write('\n' + list_of_lines[line])
        if currentLexeme == "(":
            currentLexeme, currentToken = lexer(list_of_lexemes)
            file.write('\n' + list_of_lines[line])
            Expression()
            if currentLexeme == ")":
                currentLexeme, currentToken = lexer(list_of_lexemes)
                file.write('\n' + list_of_lines[line])
                if currentLexeme == ";":
                    currentLexeme, currentToken = lexer(list_of_lexemes)
                    file.write('\n' + list_of_lines[line])
                    return
                else:
                    file.write('\n; expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
                    file.close 
                     
            else:
                file.write('\n) expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
                file.close 
                 
        else:
            file.write('\n( expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
            file.close 
             
    else:
        file.write('\nput expected for print statement, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
        file.close 
         

# Rule 21
def Scan():
    file.write('\n<Scan> ::= get ( <IDs> );')
    global currentLexeme
    global currentToken
    if currentLexeme == "get":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.write('\n' + list_of_lines[line])
        if currentLexeme == "(":
            currentLexeme, currentToken = lexer(list_of_lexemes)
            file.write('\n' + list_of_lines[line])
            IDs()
            if currentLexeme == ")":
                currentLexeme, currentToken = lexer(list_of_lexemes)
                file.write('\n' + list_of_lines[line])
                if currentLexeme == ";":
                    currentLexeme, currentToken = lexer(list_of_lexemes)
                    file.write('\n' + list_of_lines[line])
                    return
                else:
                    file.write('\n; expected for scan statement, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
                    file.close 
                     
            else:
                file.write('\n) expected for scan statement, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
                file.close 
                 
        else:
            file.write('\n( expected for scan statement, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
            file.close 
             
    else:
        file.write('\n"get" expected for scan statement, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
        file.close 
         

# Rule 22
def ourWhile():
    file.write('\n<While> ::=  while ( <Condition>  ) <Statement>')
    global currentLexeme
    global currentToken
    if currentLexeme == "while":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.write('\n' + list_of_lines[line])
        if currentLexeme == "(":
            currentLexeme, currentToken = lexer(list_of_lexemes)
            file.write('\n' + list_of_lines[line])
            Condition()
            if currentLexeme == ")":
                currentLexeme, currentToken = lexer(list_of_lexemes)
                file.write('\n' + list_of_lines[line])
                Statement()
                return
            else:
                file.write('\n) expected for while statement, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
                file.close 
                 
        else:
            file.write('\n( expected for while statement, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
            file.close 
             
    else:
        file.write('\nwhile expected for while statement, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
        file.close
         

"""
# Rule 23
def Condition():
    file.write('\n<Condition> ::= <Expression>  <Relop>   <Expression>')
    global currentLexeme
    global currentToken
    global lineNumber
    ###################### Grammar rules ######################
    if Expression():
        if Relop():
            if Expression():
                return True
            else:
                file.write('\nExpected <Expression> on line str(lineNumber)')
        else:
            file.write('\nExpected <Relop> on line str(lineNumber)')
    else:
        file.write('\nExpected <Expression> on line str(lineNumber)')
        return False
        file.close  
    ################## End of Grammar rules ###################
    lineNumber += 2                                   # Increment by 2 to get to the next token
    print("")                                         # line break
    
# Rule 24
def Relop():
    file.write('\n<Relop> ::= == | != |  > | < | <= | =>')
    global currentLexeme
    global currentToken
    ###################### Grammar rules ######################
    if currentLexeme == '==' or currentLexeme == '!=' or currentLexeme == '>' or currentLexeme == '<' or currentLexeme == '<=' or currentLexeme == '=>':
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.write('\n' + list_of_lines[line])
    else:
        file.close    
    ################## End of Grammar rules ###################
"""

# Rule 25(Left Recursion)
def Expression():
    file.write('\n<Expression> ::= <Term> <Expression Prime>')
    ###################### Grammar rules ######################
    Term()
    ExpressionPrime()
    ################## End of Grammar rules ###################

#Rule 25A
def ExpressionPrime():
    file.write('\n<Expression> ::= + <Term> <Expression Prime> | - <Term> <Expression Prime> | <Empty>')
    global currentLexeme
    global currentToken
    if currentLexeme == "+" or currentLexeme == "-":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.write('\n' + list_of_lines[line])   
        if Term():
            ExpressionPrime()
        else:
            file.write('\n+  or - expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
            file.close 
             
    else:
        Empty()

# Rule 26(Left Recursion)
def Term():
    file.write('\n<Term> ::= <Factor> <Term Prime>')
    ###################### Grammar rules ######################
    Factor()
    TermPrime()
    ################## End of Grammar rules ###################

# Rule 26A
def TermPrime():
    file.write('\n<Term Prime> ::= * <Factor> <Term Prime> | / <Factor> <Term Prime> | <Empty>')
    global currentLexeme
    global currentToken
    if currentLexeme == "*" or currentLexeme == "/":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.write('\n' + list_of_lines[line])
        Factor()
        TermPrime()
    else:
        Empty()

# Rule 27
def Factor():
    file.write('\n<Factor> ::= - <Primary> | <Primary>')
    global currentLexeme
    global currentToken
    ###################### Grammar rules ######################
    if currentLexeme == "-":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.write('\n' + list_of_lines[line])
    else:
        Primary()
    ################## End of Grammar rules ###################

# Rule 28
def Primary():
    file.write('\n<Primary> ::= <Identifier> | <Integer> | <Identifier> ( <IDs> ) | ( <Expression> ) | <Real> | true | false')
    global currentLexeme
    global currentToken
    ###################### Grammar rules ######################
    if currentToken == "INT" or currentToken == "REAL":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.write('\n' + list_of_lines[line])
    elif currentLexeme == "true":
        file.write('\n<Primary> ::= true')
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.write('\n' + list_of_lines[line])
    elif currentLexeme == "false":
        file.write('\n<Primary> ::= false')
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.write('\n' + list_of_lines[line])
    elif currentLexeme == "(":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.write('\n' + list_of_lines[line])
        Expression()
        if currentLexeme == ")":
            currentLexeme, currentToken = lexer(list_of_lexemes)
            file.write('\n' + list_of_lines[line])
            return
        else:
            file.write('\n) expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
            file.close 
             
    elif currentToken == "IDENTIFIERS":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.write('\n' + list_of_lines[line])
        if currentLexeme == "(":
            currentLexeme, currentToken = lexer(list_of_lexemes)
            file.write('\n' + list_of_lines[line])
            IDs()
            if currentLexeme == ")":
                currentLexeme, currentToken = lexer(list_of_lexemes)
                file.write('\n' + list_of_lines[line])
                return
            else:
                file.write('\n) expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
                file.close 
                 
        else:
            file.write('\n( expected, at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
            file.close 
             
    else:  
        file.write('\nError at line number {}, instead of {}'.format(str(lineNumber), list_of_lines[line]))
        file.close 
         
    ################## End of Grammar rules ###################
# Rule 29
def Empty():
    file.write('\n<Empty> ::= Epsilon')
