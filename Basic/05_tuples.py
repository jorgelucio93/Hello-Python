# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=14711

### Tuples ###

# Definición

my_tuple = tuple()##es igual de cualquiera de las dos formas de declarar
my_other_tuple = ()#definicion a nivel sintaxis

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")##agregar valores a la tupla
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

# Acceso a elementos y búsqueda

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError porque no existe el valor
# print(my_tuple[-6]) IndexError

print(my_tuple.count("Brais"))#funcion contar elementos del mismo
print(my_tuple.index("Moure"))#funcion ubicar el elemento en la tupla
print(my_tuple.index("Brais"))# y si hay 2 del mismo te regresa la ubicacion del primero que encuentra en la lista

# my_tuple[1] = 1.80 'tuple' object does not support item assignment

# Concatenación

my_sum_tuple = my_tuple + my_other_tuple##crear una concatenacion de tupla
print(my_sum_tuple)

# Subtuplas

print(my_sum_tuple[3:6])#crear subtupla entre esos valores ignorarndo el 6

# Tupla mutable con conversión a lista

my_tuple = list(my_tuple)#convertir la tupla a lista
print(type(my_tuple))

my_tuple[4] = "MoureDev"#asignar los nuevos valores a la lista
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)#y convertir de nuevo a tupla 
print(my_tuple)
print(type(my_tuple))#y se fijan los nuevos valores asignados a constantes, esto es la forma de modificar una tupla.

# Eliminación

# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple#eliminar la tupla por completo
# print(my_tuple) NameError: name 'my_tuple' is not defined
