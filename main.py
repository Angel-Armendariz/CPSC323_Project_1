import Lexical_Analyzer

while True:
    text = input('Suffering > ')
    answer, oopsie = Lexical_Analyzer.run('<stdin>', text)

    if oopsie: print(oopsie.convert_string())
    else: print(answer)
