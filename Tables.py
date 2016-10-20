#1
reservedWords = ["MAIN", "VAR", "SUM", "CYC", "CON", "CONCYC", "DIV", "MULT", "SUM", "SUB", "EXP", "SCIEXP"]
#2
comparison = ["<", ">", "<=", ">=", "==",]
#3
brackets = ["[", "]", "{", "}","(",")"]
#4
assignation = ["="]
#5
separators = [","]
#6
terminators = ["."]
#7
idVariables = []
#8 String
#9 Numeros
#10
values = []
quotations = [chr(34)]
#10
tokens = [["reservedWords", 1], ["comparison", 2], ["brackets", 3], ["assignation", 4],
          ["separators", 5], ["terminators", 6], ["idVariables", 7]]

s = [1,3,3,3,]

basicOp = [1,3,[7,9],5,[7,9],3,6]


