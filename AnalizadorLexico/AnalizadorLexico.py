from AnalizadorSintactico import AnalizadorSintactico
import Definitions
import Tables

line = []
tokens = []
temp = ""
id = ""
value = ""

#Tk().withdraw()
#filepath = askopenfilename()
#data = Definitions.fileToString(filepath)

try:
     data = Definitions.fileToString('/Users/alonsolarra/PycharmProjects/MaquinaDiscriminadora/TestFiles/Fibonacci.applescript')
except:
    path = '../MaquinaDiscriminadora/Fibonacci.applescript'
    data = Definitions.fileToString(path)

# try:
#     path = '../MaquinaDiscriminadora/TestFiles/TestOperacion'
#     data = Definitions.fileToString(path)
# except:
#     path = '../Compilador/TestFiles/TestOperacion'
#     data = Definitions.fileToString(path)


for x in range(0, len(data)):
    line.append(data[x][0])


for x in range(0, len(line)):
    for y in range(0, len(line[x])):

        temp = temp + line[x][y]

        if (str(temp) == 'VAR'):
            i = 2
            while (line[x][y + i] != "."):
                id = id + line[x][y+i]
                i = i + 1
            Tables.idVariables.append(id)
            id = ''
        id=''
        if (str(temp) == "="):
            flag1 = str(temp) + line[x][y + 1]
            flag2 = str(temp) + line[x][y - 1]
            if(flag1 != "==" and flag2 != "=="):
                i = 1
                while (line[x][y + i] != "."):
                    id = id + line[x][y+i]
                    i = i + 1
                    lex = Definitions.lexemCheck(id)
                    if(lex[0]):
                        id=''
                        break
                number = Definitions.lexemCheck(id)
                if not number[1] == 9:
                    Tables.values.append(id)
                    id = ''
            elif(flag1=="=="):
                temp = temp + line[x][y+1]
            elif(flag2=="=="):
                temp = ""

        if(temp == "CON"):
            var = str(temp) + line[x][y+1] + line[x][y+2] + line[x][y+3]
            if(var == "CONCYC"):
                temp = var
        if(temp == "CYC"):
            var =  line[x][y-5] + line[x][y-4] + line[x][y-3] + str(temp)
            if(var == "CONCYC"):
                temp = ""

        result = Definitions.lexemCheck(temp)

        try:
            impossibleLexem = Definitions.ImpossibleLexeme(temp + line[x][y + 1])
        except:
            impossibleLexem = True

        if (result[1]==9):
            number = Definitions.lexemCheck(line[x][y + 1])
            if not(number[1]==9):
                tokens.append([x, str(temp), (result[1])])
                temp = ""
        elif(result[0] == True and impossibleLexem == True ):
            tokens.append([x, str(temp),(result[1])])
            temp = ""
        elif((Definitions.ImpossibleLexeme(temp))):
            temp = ""

index = 0
Tokens = []
justTokens = []
while(index<len(line)):
    Tokens.append([])
    justTokens.append([])
    for x in range(len(tokens)):
        if tokens[x][0] == index:
            Tokens[index].append([tokens[x][1],tokens[x][2]])
            justTokens[index].append(tokens[x][2])
    index = index+1

AnalizadorSintactico.AnalizadorSintactico(Tokens, justTokens)