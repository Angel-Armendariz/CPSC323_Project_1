import Lexical_Analyzer
import Syntax_Analyzer
import Code_Generating
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
f = open("outputFile.txt", "w")
for item in answer:
    f.write("%s\n" % item)
f.close()

"""
file = open("testCase2.txt", "r")
inputText = file.read()
file.close()
answer, oopsie = Lexical_Analyzer.run('<stdin>', inputText)
f = open("outputFile2.txt", "w")
for item in answer:
    f.write("%s\n" % item)
f.close()

file = open("testCase3.txt", "r")
inputText = file.read()
file.close()
answer, oopsie = Lexical_Analyzer.run('<stdin>', inputText)
f = open("outputFile3.txt", "w")
for item in answer:
    f.write("%s\n" % item)
f.close()
"""

lexerFile = open("outputFile1.txt", "r")
parseFile = lexerFile.read()
lexerFile.close()
newFile = Syntax_Analyzer.parse(parseFile)
f = open("parsedFile1.txt", "w")
for item in newFile:
    f.write("%s\n" % item)
f.close()

lexerFile = open("outputFile2.txt", "r")
parseFile = lexerFile.read()
lexerFile.close()
newFile = Syntax_Analyzer.parse(parseFile)
f = open("parsedFile2.txt", "w")
for item in newFile:
    f.write("%s\n" % item)
f.close()

lexerFile = open("outputFile3.txt", "r")
parseFile = lexerFile.read()
lexerFile.close()
newFile = Syntax_Analyzer.parse(parseFile)
f = open("parsedFile3.txt", "w")
for item in newFile:
    f.write("%s\n" % item)
f.close()

lexerFile = open("parsedFile1.txt", "r")
parseFile = lexerFile.read()
lexerFile.close()
newFile = Code_Generating.parse(parseFile)

f = open("generatedFile1.txt", "w")
for item in newFile:
    f.write("%s\n" % item)
f.close()

lexerFile = open("parsedFile2.txt", "r")
parseFile = lexerFile.read()
lexerFile.close()
newFile = Code_Generating.parse(parseFile)

f = open("generatedFile2.txt", "w")
for item in newFile:
    f.write("%s\n" % item)
f.close()

lexerFile = open("parsedFile3.txt", "r")
parseFile = lexerFile.read()
lexerFile.close()
newFile = Code_Generating.parse(parseFile)

f = open("generatedFile3.txt", "w")
for item in newFile:
    f.write("%s\n" % item)
f.close()