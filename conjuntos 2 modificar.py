set_countries = {"col", "mex", "bol"}
print(set_countries)

# se puede pbtener el tamaño del conjunto con la funcion len
size = len(set_countries)
print(size)

# busqueda de elementos en el conjunto
print("col" in set_countries)  # true
print("pe" in set_countries)  # false

# agregar elementos al conjuntos
set_countries.add("pe")  # se agreda .add al nombre del set
print(set_countries)

# actualizar conjuntos
# la adicion de .update permite agregar un nuejo subconjunto o conjunto pequeño
# incluso si el nuevo conjunto tiene elementos preexistentes, estos no se repiten
set_countries.update({4, 5, 7, "mex", "bol"})
print(set_countries)

#remover elementos del conjunto
set_countries.remove("col") #con la adicion de .remove se eliminan elementos, si el elemento no existe, el programa hace un traceback (crsashea)
print(set_countries)

#se puede usar .discard para eliminar elementos y si estos no se encuentran no genera error
set_countries.discard("mex")
print(set_countries)

#eliminar los elementos del conjunto
set_countries.clear()
print(set_countries)






    















