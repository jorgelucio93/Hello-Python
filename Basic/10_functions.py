# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=26619

### Functions ###

# Definición

def my_function():
    print("Esto es una función")


my_function()#mandar a llamar una funcion 
my_function()
my_function()

# Función con parámetros de entrada/argumentos


def sum_two_values(first_value: int, second_value):#ignora el tipado de las variables
    print(first_value + second_value)


sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)

# Función con parámetros de entrada/argumentos y retorno


def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value # en el tipo con retorno hay que asignar el resultado a una variable
    return my_sum


my_result = sum_two_values(1.4, 5.2)
print(my_result)

my_result = sum_two_values_with_return(10, 5)
print(my_result)

# Función con parámetros de entrada/argumentos por clave


def print_name(name, surname):
    print(f"{name} {surname}")#f es para acceder a los valores


print_name(surname="Moure", name="Brais")

# Función con parámetros de entrada/argumentos por defecto


def print_name_with_default(name, surname, alias="Sin alias"):#se pueden fijar valores para argumentos y toma ese valor si no esta definido
    print(f"{name} {surname} {alias}")


print_name_with_default("Brais", "Moure")
print_name_with_default("Brais", "Moure", "MoureDev")

# Función con parámetros de entrada/argumentos arbitrarios


def print_upper_texts(*texts):#*texts para recibir x cantidad de variables de ese tipo
    print(type(texts))
    for text in texts:
        print(text.upper())


print_upper_texts("Hola", "Python", "MoureDev")
print_upper_texts("Hola")
