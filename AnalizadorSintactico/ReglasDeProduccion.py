reglasDeProduccion = [
    ["s", [1, 3, 3, 3]],
    ["declaracion", [1, 7, 6]],
    ["asignacion", [7, 4, 7, 6]],
    ["asignacion", [7, 4, 9, 6]],
    ["asignacion", [7, 4, 10, 6]],
    ["asignacion",[7, 4, 1, 3, 7, 5, 7, 3, 6]],
    ["asignacion",[7, 4, 1, 3, 7, 5, 9, 3, 6]],
    ["asignacion", [7, 4, 1, 3, 9, 5, 7, 3, 6]],
    ["asignacion", [7, 4, 1, 3, 9, 5, 9, 3, 6]],
    ["ciclo",[1,3,9,3,3]],
    ["ciclo",[1,3,7,3,3]],
    ["condicional",[1,3,7,2,7,3,3]],
    ["condicional",[1,3,7,2,9,3,3]],
    ["condicional",[1,3,9,2,7,3,3]],
    ["condicional",[1,3,9,2,9,3,3]],
    ["operacionBasica",[1,3,7,7,3,6]],
    ["operacionBasica",[1,3,9,7,3,6]],
    ["operacionBasica",[1,3,7,9,3,6]],
    ["operacionBasica",[1,3,9,9,3,6]],
]

Derivaciones = {
    'declaracion': [1,2,6],
    'asignacion': [1,2,7],
    'ciclo':[1,2,3],
    'condicional':[1,2,4],
    'operacionBasica': [1,2,8]
}
