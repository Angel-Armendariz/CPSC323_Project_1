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
file = open("testCase1.txt", "r")
inputText = file.read()
file.close()
answer, oopsie = Lexical_Analyzer.run('<stdin>', inputText)
#Prints out the test file tokens out to outputFile.txt which gets overwritten each time 
f = open("outputFile1.txt", "w")
for item in answer:
    f.write("%s\n" % item)
f.close()

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

if oopsie: 
    print(oopsie.convert_string())
    f = open("outputFile.txt", "w")
    f.write(oopsie.convert_string())
    f.close()

else: 
    # print a token each row
    for x in range(len(answer)):
        print(answer[x])