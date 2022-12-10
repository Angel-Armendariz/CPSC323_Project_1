import Lexical_Analyzer
import Syntax_Analyzer

# Uncomment the block below if you want to go back to testing through command line.
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

# Prints out the test file tokens out to outputFile.txt which gets overwritten each time 
f = open("outputFile1.txt", "w")
for item in answer:
    f.write("%s\n" % item)
f.close()

lexerFile = open("outputFile1.txt", "r")
parseFile = lexerFile.read()
lexerFile.close()
newFile = Syntax_Analyzer.parse(parseFile)

f = open("parsedFile.txt", "w")
for item in newFile:
    f.write("%s\n" % item)
f.close()
