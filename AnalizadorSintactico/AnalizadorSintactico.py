import ReglasDeProduccion
from AnalizadorSemantico import AnalizadorSemantico

reglas = []

def AnalizadorSintactico(lexemsTokens, justTokens):
    for x in range(len(justTokens)):
        for y in range(len(ReglasDeProduccion.reglasDeProduccion)):
            if(set(justTokens[x]) == set(ReglasDeProduccion.reglasDeProduccion[y][1])):
                for key in range(len(ReglasDeProduccion.Derivaciones.viewkeys())):
                    if(str(ReglasDeProduccion.Derivaciones.keys()[key])==str(
                            ReglasDeProduccion.reglasDeProduccion[y][0])):
                        reglas.append([ReglasDeProduccion.Derivaciones.values()[key], justTokens[x]])


    AnalizadorSemantico.AnalizadorSemantico(reglas,lexemsTokens)
