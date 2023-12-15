# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=8643

### Strings ###

my_string = "Mi String" #cualquier de los dos es igual para declarar#
my_other_string = 'Mi otro String'#definicion a nivel sintaxis

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string) #concatenacion de strings#

my_new_line_string = "Este es un String\ncon salto de línea" #\n para salgo de linea        
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación" #\t para tabular
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado" # el segundo \cancela la accion
print(my_scape_string)

# Formateo

name, surname, age = "Brais", "Moure", 35
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))#metodo con format
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age)) #%s para formatear strings y %d para enteros
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))#manera incorrecta de hacerlo
print(f"Mi nombre es {name} {surname} y mi edad es {age}") #metodo de inferencia

# Desempaqueado de caracteres

language = "pytohn"
a, b, c, d, e, f = language
print(a)
print(e)

# División

language_slice = language[1:3] #se empieza a contar desde el 0 imprime la 
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones del lenguaje

print(language.capitalize())#al poner el punto puedes ejecutar una funcion, capitaliza empieza con mayuscula
print(language.upper())
print(language.count("t"))##sirve para contar 
print(language.isnumeric())##saber si es numerico
print("1".isnumeric())##saber si es numerico
print(language.lower())#hacer minuscula todo
print(language.lower().isupper())#isupper para comprobar si esta en mayuscula
print(language.startswith("Py"))#comprobar si empieza con PY
print("Py" == "py")  # No es lo mismo
