def AnalizadorSintactico(Tokens):
    regla1 = [3,3,3,1]
    regla2 = [3,3,3,2]
    arr = [3,3,4,1]

    arrey = pop(arr)
    print arrey


def pop(arr):
    if len(arr)< 2:
        return arr
    else:
        arr.pop()
        pop(arr)