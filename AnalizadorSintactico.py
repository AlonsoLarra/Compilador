import ReglasDeProduccion

reglas = []

def AnalizadorSintactico(lexemsTokens, justTokens):
    for x in range(len(justTokens)):
        for y in range(len(ReglasDeProduccion.reglasDeProduccion)):
            if(set(justTokens[x]) == set(ReglasDeProduccion.reglasDeProduccion[y][1])):
                reglas.append([ReglasDeProduccion.reglasDeProduccion[y][0],justTokens[x]])


    Derivaciones(reglas)


def Derivaciones(reglas):
    print reglas