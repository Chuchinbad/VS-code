def permutaciones(cadena):
    p = factorial(len(cadena))  # Numero de permutaciones
    # print(p)
    n = len(cadena)  # longitud de la cadena
    # print(n)
    # print(factorial(len(cadena)-1))
    i = 0  # contador de indices, llegara hasta p (de 0 a p-1)
    # se crea la lista con el numero de espacios a llenar por las p permutaciones
    char_list = [" "]*p
    #print(char_list)

    """for j in range (1,n+1):
        for x in range(n):
            for i in range(x*factorial(n-j), (x+1)*factorial(n-j)):
                if cadena[x] not in char_list[i]:
                    char_list[i] = char_list[i]+cadena[x]"""
    new_char_list = arreglos(cadena, n, char_list)

    # x=0
    #char_list[i] = cadena[x] + cadena[x]

    return new_char_list


def arreglos(cadena, n, char_list):
    for j in range(1, n+1):
        for x in range(n):
            for i in range(x*factorial(n-j), (x+1)*factorial(n-j)):
                if cadena[x] not in char_list[i]:
                    char_list[i] = char_list[i]+cadena[x]
    if n == 0:
        return char_list
    arreglos(cadena, n-1, char_list)
    return char_list


def factorial(n):
    f = 1
    for i in range(1, n+1):
        f = f*i
    return f


cadena = ("abcd")

resultado = permutaciones(cadena)

print(resultado)
