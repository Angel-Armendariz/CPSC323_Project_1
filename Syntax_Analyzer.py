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
    OptFuncDef()                    
    if currentLexeme == "$":          
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])          
        OptDeclarList()                 
        StatementList()                                        
        if currentLexeme == "$":        
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
    FuncDef()       
    Empty()         
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
    global currentToken
    file.append('<Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>')
    if currentLexeme == "function":                                              
        global currentToken
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])          

        if currentToken != "IDENTIFIERS":
            file.append('IDENTIFIER expected at line number {}'.format(str(lineNumber)))
        elif currentToken == "IDENTIFIERS":
        if currentToken == "IDENTIFIERS":
            currentLexeme, currentToken = lexer(list_of_lexemes)
            file.append('\n' + list_of_lines[line])          

            if currentLexeme != "(":
                file.append('( SEPARATOR expected at line number {}'.format(str(lineNumber)))
            elif currentLexeme == "(":    
                ###################### Grammar rules ######################
            file.append('\n' + list_of_lines[line]) 
            IDs()         
            if currentLexeme == "(":    
                currentLexeme, currentToken = lexer(list_of_lexemes)
                file.append('\n' + list_of_lines[line])   
                OptParaList()
@ -110,6 +104,10 @@ def Func():
                    file.append('\n' + list_of_lines[line])   
                    OptDeclarList()
                    Body()
            elif currentLexeme != "(":
                file.append('( SEPARATOR expected at line number {}'.format(str(lineNumber)))
        elif currentToken != "IDENTIFIERS":
            file.append('IDENTIFIER expected at line number {}'.format(str(lineNumber)))
                ################## End of Grammar rules ###################

# Rule 5
@ -402,226 +400,226 @@

# Rule 19A
def ReturnPrime():
    file.append('<Return Prime> ::= ; | <Expression> ;')
    global currentLexeme
    global currentToken
    if currentLexeme == "return":
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])   
        file.append('\n' + list_of_lines[line])
        file.append('<Return Prime> ::= ; | <Expression> ;')   
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
                currentLexeme, currentToken = lexer(list_of_lexemes)
                file.append('\n' + list_of_lines[line])
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
    if currentLexeme == "-":
        global currentToken
        currentLexeme, currentToken = lexer(list_of_lexemes)
        file.append('\n' + list_of_lines[line])
    Primary()
    return

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