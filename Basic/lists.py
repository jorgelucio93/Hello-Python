# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=10872

### Lists ###

# Definición

my_list = list()#cualquiera de los dos es lo mismo una lista.
my_other_list = [] #definicion a nivel sintaxis

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17] #añadiendo elementos a la lista

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Brais", "Moure"]

print(type(my_list))
print(type(my_other_list))

# Acceso a elementos y búsqueda

print(my_other_list[0])##para mandar a llamar objetos
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(30))#para ver cuantas veces se repite
# print(my_other_list[4]) IndexError cuando queda fuera de rango de la lista
# print(my_other_list[-5]) IndexError cuando queda fuera de rango de la lista 

print(my_other_list.index("Brais"))

age, height, name, surname = my_other_list#mala practica de desempaquetado
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]#mala practica
print(age)

# Concatenación

print(my_list + my_other_list) #para concatenar
#print(my_list - my_other_list) #tira error

# Creación, inserción, actualización y eliminación

my_other_list.append("MoureDev")#funcion agregar un valor a la lista
print(my_other_list)

my_other_list.insert(1, "Rojo")#funcion agregar un valor en una posicion especifica
print(my_other_list)

my_other_list[1] = "Azul"
print(my_other_list)

my_other_list.remove("Azul")#funcion eliminar el primer valor que ha encontrado
print(my_other_list)

my_list.remove(30)
print(my_list)

print(my_list.pop())#funcion para ocultar el ultimo elemento
print(my_list)

my_pop_element = my_list.pop(2)#funcion para ocultar y saber un elemento especifico
print(my_pop_element)
print(my_list)

del my_list[2]#funcion eliminar de la lista un dato especifico
print(my_list)

# Operaciones con listas

my_new_list = my_list.copy()#generar una copia de una lista para que quede temporal aunque la eliminemos

my_list.clear()#limpiar datos de la lista
print(my_list)
print(my_new_list)

my_new_list.reverse()#funcion invertir la lista
print(my_new_list)

my_new_list.sort()#ordena de mayor a menor la lista ya sea numerico o alfabetico
print(my_new_list)

# Sublistas

print(my_new_list[1:3])#generar sublista de la lista 1 y 3 ignorando el ultimo valor

# Cambio de tipo

my_list = "Hola Python"
print(my_list)
print(type(my_list))
