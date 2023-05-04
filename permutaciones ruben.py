def rest(principal, restando):
    for i in restando:
        if i in principal:
            temporal = principal.partition(i)
            principal = temporal[0] +temporal[2]
        else:
            return -1
            break;            
    return principal




def recursiva(lista, cadena):
    old_list = lista
    new_list = list('')
    for i in old_list:
        temporal = rest(cadena,i)
        if temporal == '':
            
            return old_list
        else:
            temporal =list(temporal)
            for j in temporal:
                new_list.append(i+j)
    recursiva(new_list, cadena)
    print(new_list)

    
cadena = input('Ingresa tu cadena: ')
lista = list(cadena)
resultado = recursiva(lista, cadena)
print(resultado)