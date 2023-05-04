# conjunto, set de elementos sin orden, no repetibles, si modificables
set_countries = {"col", "mex", "bol"}
print(set_countries)
print(type(set_countries))  # los conjuntos tienen type "set"

set_numbers = {1, 4, 6, 3, 6, 7, 5, 8, 9}
print(set_numbers)
# los conjuntos pueden tener varios tipos de datos
set_types = {"hola", True, 34.45, False}
print(set_types)

# se puede crear un set a partir de otras estrucuturas de datos
set_from_string = set("holllaaaa")
# los elementos del strin "hola" se separaron y definieron como elementos del set_from_string y se eliminan elementos duplicados
print(set_from_string)

# tambien se puede descomponer una tupla en sus elementos
set_from_tuple = set(("ebc", "dor", "diy", "jdh"))
print(set_from_tuple)

# al transformar una lista en conjunto, se resuelve el eliminar elementos repetidos
numbers = [4, 54, 65, 3, 4, 2, 4, 5, 6, 5, 4, 3, 54, 76, 8, 6, 98, 2]
print(set(numbers))
numbers_set = set(numbers)
print(numbers_set)
numbers_list = list(numbers_set)
# con esto volvemos a transformar el nuevo set en lista ya con los elementos repetidos eliminados
print(numbers_list)

