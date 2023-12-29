# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=23822

### Loops ###

# While

my_condition = 0

while my_condition < 10:#te permite repetir el ciclo hasta que la condicion se cumpla
    print(my_condition)
    my_condition += 2#para autoincrementar un valor
else:  # Es opcional
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break##detiene todo el ciclo hasta su else 
    print(my_condition)

print("La ejecución continúa")

# For

my_list = [35, 24, 62, 52, 30, 30, 17]#en una lista

for element in my_list:#elemen es para nombrar a la lista pero no es forzosa la palabra
    print(element)

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")

for element in my_tuple:#en un tuple
    print(element)

my_set = {"Brais", "Moure", 35}#en un set

for element in my_set:
    print(element)

my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}#en un dictado

for element in my_dict:
    print(element)
    if element == "Edad":
        break #detiene todo el ciclo hasta su else
else:
    print("El bluce for para diccionario ha finalizado")

print("La ejecución continúa")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue#regresa al inicio del for sin ejecutar lo que sigue dentro del for
    print("Se ejecuta")
else:
    print("El bluce for para diccionario ha finalizado")
