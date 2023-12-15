# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=16335

### Sets ###

# Definición

my_set = set()##es igual de cualquiera de las dos formas de declarar
my_other_set = {}#definicion a nivel sintaxis

print(type(my_set))
print(type(my_other_set))  # Inicialmente es un diccionario cuando no tiene datos

my_other_set = {"Brais", "Moure", 35}
print(type(my_other_set))

print(len(my_other_set))

# Inserción

my_other_set.add("MoureDev")

print(my_other_set)  # Un set no es una estructura ordenada

my_other_set.add("MoureDev")  #para añadir un elemento pero no admite repetidos

print(my_other_set)

# Búsqueda

print("Moure" in my_other_set)#para encontrar elementos
print("Mouri" in my_other_set)

# Eliminación

my_other_set.remove("Moure")#remover un dato especifico
print(my_other_set)

my_other_set.clear()#vacia todos los datos
print(len(my_other_set))

del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

# Transformación a lista pd: se crea de diferente forma cada ves porque que el set no tiene una forma definida

my_set = {"Brais", "Moure", 35}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

# Otras operaciones

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))#si deja hacer la unionp porque son datos no repetidos, solo en el print y no se ha guardado en la variable.
print(my_new_set.difference(my_set))
