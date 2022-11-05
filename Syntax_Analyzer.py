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
                
            #beginning of what Kaitlin added
            elif currentLexeme == "while (" or "while(":
                    Condition()
                    if currentLexeme == ")":
                        Statement()
            elif currentLexeme == "-":
                Factor()                        # Rule 27
            #end of what Kaitlin added

            #indented the else statement of the expected at line number, because it would stop iterating over the characters-- Kaitlin
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

# Rule 3
def FunctionDef():
    print("<Function Definitions>  ::= <Function> (<Function Definitions PRIME>)")

# Rule 3A
def FunctionDefPrime():
    print("<Function Definitions PRIME> ::= ε | <Function Definitions>")

# Rule 4
def Func():
    print("<Function> ::= function <identifer> (<Opt Parameter List>) <Opt Declaration List> <Body>")

# Rule 5
def OptParamList():
    print("<Opt Parameter List ::= <Parameter List> | <Empty>")

# Rule 6
def ParamList():
    print("<Parameter List>  ::=  <Parameter> ( <Parameter List PRIME> )")

# Rule 6A
def ParamListPrime():
    print("<Parameter List PRIME> ::= ε | , <Parameter List>")

# Rule 7
def Param():
    print("<Parameter> ::= <IDs> <Qualifier>")

# Rule 8
def Qualifier():
    print("<Qualifier> ::= integer | boolean | real")

# Rule 9
def Body():
    print("<Body> ::= { <Statement List> }")

# Rule 10
def OptDeclarList():
    print("<Opt Declaration List> ::= <Declaration List> | <Empty>")

# Rule 11
def DeclarationList():
    print("<Declaration List>  := <Declaration> ; (<Declaration List PRIME>)")

# Rule 11A
def DeclarationListPrime():
    print("<Declaration List PRIME> :=  ε |  <Declaration List>")

# Rule 12
def Declaration():
    print("<Declaration> ::= <Qualifier> <IDs>")

# Rule 13
def IDs():
    print("<IDs> ::= <Identifier> <IDs PRIME>")

# Rule 13A
def IDsPrime():
    print("<IDs PRIME> ::= ε | , <IDs>")

# Rule 14
def StatementList():
    print("<Statement List> ::= <Statement> <Statement List PRIME>")

# Rule 14A
def StatementListPrime():
    print("<Statement List PRIME> ::= ε | <Statement List>")

# Rule 15
def Statement():
    print("<Statement> ::= <Compound> | <Assign> | <if> | <Return> | <Print> | <Scan> | <While>")

# Rule 16
def Compound():
    print("<Compound> ::= { <Statement List> }")

# Rule 17
def Assign():
    print("<Assign> ::= <Identifier> = <Expression>;")

# Rule 18
def If():
    print("<If> ::= if (<Condition>) <Statement> <If PRIME>")

# Rule 18A
def IfPrime():
    print("<If PRIME> ::= endif | else  <Statement>  endif")

# Rule 19
def Return():
    print("<Return> ::=  return <Expression PRIME>")

# Rule 19A
def ReturnPrime():
    print("<Expression PRIME> ::= (; | <Expression> ;)")

# Rule 20 
def Print():
    print("<Print> ::= put(<Expression>);")

# Rule 21
def Scan():
    print("<Scan> ::= get( <IDs> );")

# Rule 22
def While():
    print("<While> ::= while( <Condition> ) <Statement>")

# Rule 23 
def Condition():
    print("<Condition> ::= <Expression> <Relop> <Expression>")

# Rule 24
def Relop():
    print("<Relop> ::= == | != | > | < | <= | =>")

# Rule 25
def Expression():
    print("<Expression>  ::= <Term> <Expression PRIME>")

# Rule 25A
def ExpressionPrime():
    print("<Expression PRIME>::= + <Term> <Expression PRIME> | - <Term> <Expression PRIME> | ε")

# Rule 26
def Term():
    print("<Term> ::= <Factor> <Term PRIME>")

# Rule 26A
def TermPrime():
    print("<Term PRIME> ::= * <Factor> <Term PRIME> | / <Factor> <Term PRIME> | ε")

# Rule 27 
def Factor(list_of_lines, list_of_lexemes, lineNumber):
    print("<Factor> ::= -<Primary> | <Primary>")

# Rule 28
def Primary():
    print("<Primary> ::= <Identifier> | <Integer> | <Identifier> ( <IDs> ) | ( <Expression> ) | <Real> | true | false")

# Rule 29 
def Empty():
    print("<Empty> ::= Epsilon")

