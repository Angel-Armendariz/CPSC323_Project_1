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
file1 = open("testFile.txt", "r")
inputText = file1.read()
file1.close()
answer, oopsie = Lexical_Analyzer.run('<stdin>', inputText)
#Prints out the test file tokens out to outputFile.txt which gets overwritten each time 
f = open("outputFile.txt", "w")
for item in answer:
    f.write("%s\n" % item)
f.close()

<<<<<<< Updated upstream
=======
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

lexerFile = open("outputFile.txt", "r")
parseFile = lexerFile.read()
lexerFile.close()
newFile = Syntax_Analyzer.parse(parseFile)
"""
f = open("parsedFile.txt", "w")
for item in newFile:
    f.write("%s\n" % item)
f.close()
"""
"""
>>>>>>> Stashed changes
if oopsie: 
    print(oopsie.convert_string())
    f = open("outputFile.txt", "w")
    f.write(oopsie.convert_string())
    f.close()

else: 
    # print a token each row
    for x in range(len(answer)):
        print(answer[x])