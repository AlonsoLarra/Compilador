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
    count = 0
    id = 0
    if lexem in Tables.reservedWords:
        count = count+1
        id = 1
    if lexem in Tables.comparison:
        count = count+1
        id = 2
    if lexem in Tables.brackets:
        count = count+1
        id = 3
    if lexem in Tables.assignation:
        count = count+1
        id = 4
    if lexem in Tables.separators:
        count = count+1
        id = 5
    if lexem in Tables.terminators:
        count = count+1
        id = 6
    if lexem in Tables.idVariables:
        count = count+1
        id = 7
    if strRegex.match(lexem):
        count = count+1
        id = 8
    if numRegex.match(lexem):
        count = count+1
        id = 9
    if lexem in Tables.values:
        count = count+1
        id = 10
    if count == 1:
        return [True,id]
    elif count>1:
        print "count >1: " +lexem
        return [True,0]
    else:
        return [False,0]


#CHECK IF A WORD IS a possible RESERVED
def ImpossibleLexeme(word):
    flag = False
    count = 0

    for x in range(0,len(Tables.reservedWords)):
        if word in Tables.reservedWords[x]:
            count = count+1
            flag = True
        else:
            if not (flag):
                flag = False

    for x in range(0,len(Tables.idVariables)):
        if word in Tables.idVariables[x]:
            count = count + 1
            flag = True
        else:
            if not (flag):
                flag = False

    for x in range(0,len(Tables.values)):
        if word in Tables.values[x]:
            count = count + 1
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
