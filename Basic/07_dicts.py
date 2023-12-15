# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc

### Dictionaries ###

# Definición

my_dict = dict()#cualquiera de las dos formas de definir es valida
my_other_dict = {}#se usa el mismo que los sets a nivel sintaxis

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Brais",
                 "Apellido": "Moure", "Edad": 35, 1: "Python"}#esta es la forma de añadirle datos

my_dict = {
    "Nombre": "Brais",
    "Apellido": "Moure",
    "Edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"},#esta es otra forma de agregarle datos
    1: 1.77
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))#cuenta las variables que hay almacenadas en caso de que sea una con varias cosas dentro solo cuenta una variable por ejemplo "lenguajes"
print(len(my_dict))

# Búsqueda

print(my_dict[1]) #se diferencian los diccionarios por mayor accesibilidad de elementos
print(my_dict["Nombre"])#busqueda por elemento 

print("Moure" in my_dict)#busqueda por variable
print("Apellido" in my_dict)

# Inserción

my_dict["Calle"] = "Calle MoureDev"#agregar nueva variable y valores al diccionario
print(my_dict)

# Actualización

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

# Eliminación

del my_dict["Calle"]#eliminar una variable especifica 
print(my_dict)

# Otras operaciones

print(my_dict.items())#ver todo
print(my_dict.keys())#ver las variables
print(my_dict.values())#ver los valores

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))#crear un diccionario sin datos desde una lista
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict)#crear un diccionario desde otro diccionario conservando solo las variables
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "MoureDev")#agregar un valor a todas las variables pero no se puede asignar a una sola variable
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

##transformaciones##

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))#transformar en lista pero solo se trae las variables y no los valores
print(tuple(my_new_dict))
print(set(my_new_dict))
