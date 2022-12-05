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
    OptFuncDef()                    # Rule 2 - for declaring functions before the main body of code
    if currentLexeme == "$":          # signifies the start of the main body of code
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])          
        OptDeclarList()                 # Rule 10 - list for declaring variables & etc
        StatementList()                 # Rule 14 - list for intializing variables into statements             
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])          
        if currentLexeme == "$":        # signifies the end of the main body of code
            file.append('\n All done parsing.')
        else:
            file.append('$ expected at line number {} for rat22f'.format(str(lineNumber)))
    else:
        file.append('$ expected at line number {} for rat22f'.format(str(lineNumber)))
        
    ################## End of Grammar rules ###################        

# Rule 2 
def OptFuncDef():

    file.append('<Opt Function Definitions> ::= <Function Definitions> | <Empty>')
    ###################### Grammar rules ######################
    FuncDef()       # Rule 3
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
    file.append('<Function Definition Prime> ::= <Empty> | <Function Definitions>')
    if currentLexeme != "function":
        Empty()
    else:
        FuncDef()

# Rule 4
def Func():
    global currentLexeme
    file.append('<Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>')
    if currentLexeme == "function":                                              
        global currentToken
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])          

        if currentToken != "IDENTIFIERS":
            file.append('IDENTIFIER expected at line number {}'.format(str(lineNumber)))
        elif currentToken == "IDENTIFIERS":
            currentLexeme, currentToken = lexer(list_of_lexemes)
            file.append('\n' + list_of_lines[line])          

            if currentLexeme != "(":
                file.append('( SEPARATOR expected at line number {}'.format(str(lineNumber)))
            elif currentLexeme == "(":    
                ###################### Grammar rules ######################
                currentLexeme, currentToken = lexer(list_of_lexemes)
                file.append('\n' + list_of_lines[line])   
                OptParaList()
                if currentLexeme == ")":
                    currentLexeme, currentToken = lexer(list_of_lexemes)
                    file.append('\n' + list_of_lines[line])   
                    OptDeclarList()
                    Body()
                ################## End of Grammar rules ###################

# Rule 5
def OptParaList():
    file.append('<Opt Parameter List> ::= <Parameter List> | <Empty>')
    ###################### Grammar rules ######################
    if ParaList():
        return
    else:
        Empty()
    ################## End of Grammar rules ###################


# Rule 6 (Back-Tracking)
def ParaList():
    file.append('<Parameter List> ::= <Parameter> ( <Parameter List Prime> )')
    global currentLexeme
    global currentToken
    ###################### Grammar rules ######################
    Para()
    if currentLexeme == ",":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])   
        ParaListPrime()
    ################## End of Grammar rules ###################

# Rule 6A
def ParaListPrime():
    global currentLexeme
    global currentToken
    file.append('<Parameter List Prime> ::= Epsilon | ,<Parameter List>')
    ###################### Grammar rules ######################
    #if currentLexeme == ",":
    if currentToken == "IDENTIFIERS":
        ParaList()
    else:
        Empty()
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
    global currentLexeme
    ###################### Grammar rules ######################
    if currentLexeme == "integer":
        file.append('<Qualifier> ::= integer')
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line]) 
    elif currentLexeme == "boolean":
        file.append('<Qualifier> ::= boolean')
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line]) 
    elif currentLexeme == "real":
        file.append('<Qualifier> ::= real')
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line]) 
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
            file.append('outer bracket expected at line number {}, instead of {} for Body()'.format(str(lineNumber), list_of_lines[line]))
    else:
        file.append('inner bracket expected, at line number {}, instead of {} for Body()'.format(str(lineNumber), list_of_lines[line]))
    ################## End of Grammar rules ###################

# Rule 10
def OptDeclarList():
    file.append('<Opt Declaration List> ::= <Declaration List> | <Empty>')
    global currentLexeme
    global currentToken
    DeclarList()
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
        DeclarListPrime()
    ################## End of Grammar rules ###################

# Rule 11A
def DeclarListPrime():
    file.append('<Declaration List Prime> ::= <Empty> | <Declaration List>')
    global currentLexeme
    global currentToken
    if currentLexeme == ";" or currentToken == "KEYWORD":
        DeclarList()
    else:
        Empty()

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
    global currentLexeme
    global currentToken
    if currentToken == "IDENTIFIERS":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])
        IDsPrime()
    

# Rule 13A
def IDsPrime():
    file.append('<IDs Prime> ::= Epsilon | , <IDs>')
    global currentLexeme
    global currentToken
    if currentLexeme == ",":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])
        if currentToken == "IDENTIFIERS":
            IDs()
        else:
            return   
    else:
        Empty()


# Rule 14(Back-Tracking)
def StatementList():
    file.append('<Statement List> ::= <Statement> <Statement List Prime>')
    ###################### Grammar rules ######################
    Statement()
    StatementListPrime()
    ################## End of Grammar rules ###################

# Rule 14A
def StatementListPrime():
    file.append('<Statement List Prime> ::= <Empty> | <Statement List>')
    global currentToken
    global currentLexeme
    if currentToken == "KEYWORD":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])  
        StatementList()
    else:
        Empty()

# Rule 15
def Statement():
    file.append('<Statement>::= <Compound> | <Assign> | <If> | <Return> | <Print> | <Scan> | <While>')
    global currentLexeme
    global currentToken
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
            file.append('outer bracket expected, at line number {}, instead of {} for Compound()'.format(str(lineNumber), list_of_lines[line]))
    else:
        file.append('inner bracket expected, at line number {}, instead of {} for Compound()'.format(str(lineNumber), list_of_lines[line]))
        
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
                file.append('; expected, at line number {}, instead of {} for Assign()'.format(str(lineNumber), list_of_lines[line]))
        else:
            file.append('= expected, at line number {}, instead of {} for Assign()'.format(str(lineNumber), list_of_lines[line]))
    else:
        file.append('IDENTIFIER expected, at line number {}, instead of {} for Assign()'.format(str(lineNumber), list_of_lines[line]))
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
                    file.append('endif expected at line number {}, instead of {} for If()'.format(str(lineNumber), list_of_lines[line]))
            else:
                file.append(') expected at line number {}, instead of {} for If()'.format(str(lineNumber), list_of_lines[line]))
        else:
            file.append('( expected for condition at line number {}, instead of {} for If()'.format(str(lineNumber), list_of_lines[line]))            
    else:
        file.append('if expected at line number {}, instead of {} for If()'.format(str(lineNumber), list_of_lines[line]))
    ################## End of Grammar rules ###################

def IfPrime():
    file.append('<If Prime> ::= endif | else <Statement> endif')
    global currentLexeme
    global currentToken
    
    if currentLexeme == "else":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])
        Statement()
        IfPrime()
        return
    return

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
    global currentToken
    if currentLexeme == "return":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])   
        Expression()
        if currentLexeme == ";":
            currentLexeme, currentToken = lexer(list_of_lexemes)
            file.append('\n' + list_of_lines[line])
            return
        else:
            file.append('; expected, at line number {}, instead of {} for ReturnPrime()'.format(str(lineNumber), list_of_lines[line]))   
    else:
        return
# Rule 20
def ourPrint():
    file.append('<Print> ::= put ( <Expression> );')
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
                    file.append('; expected, at line number {}, instead of {} for Print()'.format(str(lineNumber), list_of_lines[line]))
            else:
                file.append(') expected, at line number {}, instead of {} for Print()'.format(str(lineNumber), list_of_lines[line]))
        else:
            file.append('( expected, at line number {}, instead of {} for Print()'.format(str(lineNumber), list_of_lines[line]))    
    else:
        file.append('keyword put expected for print statement, at line number {}, instead of {} for Print()'.format(str(lineNumber), list_of_lines[line]))
        
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
                    file.append('; expected for scan statement, at line number {}, instead of {} for Scan()'.format(str(lineNumber), list_of_lines[line]))
            else:
                file.append(') expected for scan statement, at line number {}, instead of {} for Scan()'.format(str(lineNumber), list_of_lines[line]))
        else:
            file.append('( expected for scan statement, at line number {}, instead of {} for Scan()'.format(str(lineNumber), list_of_lines[line]))
    else:
        file.append('keyword get expected for scan statement, at line number {}, instead of {} for Scan()'.format(str(lineNumber), list_of_lines[line]))
        

# Rule 22
def ourWhile():
    file.append('<While> ::=  while ( <Condition> ) <Statement>')
    global currentLexeme
    global currentToken
    if currentLexeme == "while":
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
                return
            else:
                file.append(') expected for while statement, at line number {}, instead of {} for While()'.format(str(lineNumber), list_of_lines[line]))
        else:
            file.append('( expected for while statement, at line number {}, instead of {} for While()'.format(str(lineNumber), list_of_lines[line]))
    else:
        file.append('while expected for while statement, at line number {}, instead of {} for While()'.format(str(lineNumber), list_of_lines[line]))
        
# Rule 23
def Condition():
    global currentToken
    global currentLexeme
    file.append('<Condition> ::= <Expression> <Relop> <Expression Prime>')
    ###################### Grammar rules ######################
    Expression()
    Relop()
    currentLexeme, currentToken = lexer(list_of_lexemes)
    file.append('\n' + list_of_lines[line])
    ExpressionPrime()
    ################## End of Grammar rules ###################
    
# Rule 24
def Relop():
    file.append('<Relop> ::= == | != | > | < | <= | =>')
    global currentLexeme
    global currentToken
    ###################### Grammar rules ######################
    if currentLexeme == "==" or currentLexeme == ">" or currentLexeme == "<" or currentLexeme == "<=" or currentLexeme == "=>" or currentLexeme == "!=":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])
        return          
    ################## End of Grammar rules ###################


# Rule 25(Left Recursion)
def Expression():
    file.append('<Expression> ::= <Term> <Expression Prime>')
    ###################### Grammar rules ######################
    Term()
    ExpressionPrime()
    return
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
    return
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
    ###################### Grammar rules ######################
    if currentLexeme == "-":
        global currentToken
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])
    Primary()
    return
    ################## End of Grammar rules ###################

# Rule 28
def Primary():
    file.append('<Primary> ::= <Identifier> | <Integer> | <Identifier> ( <IDs> ) | ( <Expression> ) | <Real> | true | false')
    global currentLexeme
    global currentToken

    currentLexeme, currentToken = lexer(list_of_lexemes)
    file.append('\n' + list_of_lines[line])

    ###################### Grammar rules ######################
    if currentToken == "INT" or currentLexeme == "real" or currentLexeme == "true" or currentLexeme == "false":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])
        return   
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
                file.append(') expected, at line number {}, instead of {} for Primary()'.format(str(lineNumber), list_of_lines[line]))
        return
    elif currentLexeme == "(":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])
        Expression()
        if currentLexeme == ")":
            currentLexeme, currentToken = lexer(list_of_lexemes)
            file.append('\n' + list_of_lines[line])
            return
        else:
            file.append(') expected, at line number {}, instead of {} for Primary()'.format(str(lineNumber), list_of_lines[line]))                
    else:  
        return
        
    ################## End of Grammar rules ###################
# Rule 29
def Empty():
    file.append('<Empty> ::= Epsilon')
