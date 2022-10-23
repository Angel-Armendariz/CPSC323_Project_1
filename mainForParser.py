import Syntax_Analyzer

parserFile = open("testCase1.txt", "r")
inputText = parserFile.read()
parserFile.close()
answer, oopsie = Syntax_Analyzer.run('<stdin>', inputText)

f = open("parserFile.txt", "w")
for item in answer:
    f.write("%s\n" % item)
f.close()

if oopsie: 
    print(oopsie.convert_string())
    f = open("parserFile.txt", "w")
    f.write(oopsie.convert_string())
    f.close()

else: 
    # print a token each row
    for x in range(len(answer)):
        print(answer[x])