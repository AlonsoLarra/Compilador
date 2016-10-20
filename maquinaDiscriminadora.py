import Definitions
from Tkinter import Tk
from tkFileDialog import askopenfilename
import Tables
import AnalizadorSintactico
import re


line = []
tokens = []
temp = ""
id = ""
value = ""

Tk().withdraw()
filepath = askopenfilename()
data = Definitions.fileToString(filepath)



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
        if (result[1]==9):
            number = Definitions.lexemCheck(line[x][y+1])
            if not(number[1]==9):
                tokens.append([str(temp), (result[1])])
                temp = ""
        elif(result[0] == True):
            tokens.append([str(temp),(result[1])])
            temp = ""
        elif((Definitions.ImpossibleLexeme(temp))):
            temp = ""

AnalizadorSintactico.AnalizadorSintactico(tokens);