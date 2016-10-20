from numpy import *
import csv
import Tables
import re



possibleStrRegex =  re.compile(r'\"(.+?)')
strRegex = re.compile(r'\"(.+?)\"')
numRegex = re.compile('^-?[0-9]+$')
quotationRegex = re.compile('"')

#RETURN AN STRING ARRAY FROM A GIVEN .TXT
def fileToString (filepath):
    with open(filepath) as f:
        reader = csv.reader(f, delimiter="\t")
        data = list(reader)
        return data

#CHECK IF A WORD IS RESERVED
def lexemCheck(lexem):
    if lexem in Tables.reservedWords:
        return [True,1]
    elif lexem in Tables.comparison:
        return [True,2]
    elif lexem in Tables.brackets:
        return [True,3]
    elif lexem in Tables.assignation:
        return [True,4]
    elif lexem in Tables.separators:
        return [True,5]
    elif lexem in Tables.terminators:
        return [True,6]
    elif lexem in Tables.idVariables:
        return [True,7]
    elif strRegex.match(lexem):
        return [True,8]
    elif numRegex.match(lexem):
        return [True,9]
    elif lexem in Tables.values:
        return [True, 10]
    else:
        return [False,0]

#CHECK IF A WORD IS a possible RESERVED
def ImpossibleLexeme(word):
    flag = False

    for x in range(0,len(Tables.reservedWords)):
        if word in Tables.reservedWords[x]:
            flag = True
        else:
            if not (flag):
                flag = False

    for x in range(0,len(Tables.idVariables)):
        if word in Tables.idVariables[x]:
            flag = True
        else:
            if not (flag):
                flag = False

    for x in range(0,len(Tables.values)):
        if word in Tables.values[x]:
            flag = True
        else:
            if not (flag):
                flag = False

    if numRegex.match(word):
        flag = True

    if(flag):
        return False
    else:
        return True
