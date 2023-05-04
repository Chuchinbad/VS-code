import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


print("El siguiente programa te permite realizar operaciones con los conjuntos A y B mismos que seran definidos a continuación:")
print("Define los elementos del conjunto A")
setA = input(
    "¿Que elemenos deseas incluir en A? Ingresa los elementos separados por coma (,)")
A = set(setA.split(','))
print("Los elementos del conjunto A son:", A)
print("Define los elementos del conjunto B")
setB = input(
    "¿Que elemenos deseas incluir en B? Ingresa los elementos separados por coma (,)")
B = set(setB.split(','))
conjunto_universo = A | B
print("Los elementos del conjunto B son:", B)
print("El conjunto universo es", conjunto_universo)
answer = 9090
C = {}
while answer != 0:
    answer = input("Selecciona la operacion que quieres realizar con los conjuntos definidos:\n 1, Union de conjuntos A y B \n 2, Intersección de conjuntos A y B \n 3, Diferencia A-B \n 4, Diferencia B-A 5, Diferencia simetrica A B \n \n  0, Salir")
    answer = int(answer)
    if answer == 1:
        clear_screen()
        C = A.union(B)
        print("El conjunto resultante es:", C)
    if answer == 2:
        clear_screen()
        C = A.intersection(B)
        print("El conjunto resultante es:", C)
    if answer == 3:
        clear_screen()
        C = A.difference(B)
        print("El conjunto resultante es:", C)
    if answer == 4:
        clear_screen()
        C = B.difference(A)
        print("El conjunto resultante es:", C)
    if answer == 5:
        clear_screen()
        C = A.symmetric_difference(B)
        print("El conjunto resultante es:", C)

print("FIN DEL PROGRAMA")
