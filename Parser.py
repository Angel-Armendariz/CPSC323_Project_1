Keywords = ["integer", "boolean", "real", "if", "else", "endif", "while", "return",
            "get", "put", "true", "false", "function"]

Letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

Seperators = ',$(){};='

Operators = ["==", "!=", ">", "<", "<=", "=>", "+", "-", "*", "/"]

def parse(textToParse):
    list_of_strings = textToParse.splitlines()
    list_of_lexemes = textToParse.split()
    x = 1

    for line in list_of_strings:
        print(line)                                  # will print the Token:___ Lexeme:___

        lexeme = list_of_lexemes[x]                  # this block will grab the Lexeme:___
        edittedLexeme = lexeme[7:]                   # and make print out the part after the :
        #print(edittedLexeme)                        # this is just to see where we are while we code

        ################## Grammar rules ###################
        if(edittedLexeme in Keywords):
            print("<Keyword> =:: <Example>")
        elif(edittedLexeme in Letters):
            print("<Letter/Expression> =:: <Example>")
        elif(edittedLexeme in Seperators):
            print("<Seperator> =:: <Example>")
        elif(edittedLexeme in Operators):
            print("<Operator> =:: <Example>")
        else:
            print("<Identifier/Numbers Rule> =:: <Example>")            # not sure how to check for Identifiers
                                                                # this is placeholder text for Identifiers
        
        x += 2
        print("")