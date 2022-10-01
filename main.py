import Lexical_Analyzer

# Uncomment the block below if you want to go back to testing through command line.
# Then ident the rest of the code by one Tab Space because of Python's scope rules.
# Lastly comment out lines 13-16
"""
while True:
    text = input('Suffering > ')
    answer, oopsie = Lexical_Analyzer.run('<stdin>', text)
"""

# change paramater of testFile.txt to whatever input file you want to test
file = open("testFile.txt", "r")
inputText = file.read()
file.close()
answer, oopsie = Lexical_Analyzer.run('<stdin>', inputText)

if oopsie: print(oopsie.convert_string())
else: 
    # print a token each row
    for x in range(len(answer)):
        print(answer[x])