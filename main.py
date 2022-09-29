import Lexical_Analyzer

while True:
    text = input('Suffering > ')
    answer, oopsie = Lexical_Analyzer.run('<stdin>', text)

    if oopsie: print(oopsie.convert_string())
    else: 
        # print a token each row
        for x in range(len(answer)):
            print(answer[x])