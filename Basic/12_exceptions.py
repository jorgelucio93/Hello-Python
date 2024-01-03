# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=32030

### Exception Handling ###

numberOne = 5
numberTwo = 1
numberTwo = "1"

# Excepción base: try except

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    # Se ejecuta si se produce una excepción
    print("Se ha producido un error")

# Flujo completo de una excepción: try except else finally

try:#codigo a intentar correr   
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:#siempre va despues del try
    print("Se ha producido un error")
else:  # entra si el try no entra
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally:  # entra pase lo que pase
    # Se ejecuta siempre
    print("La ejecución continúa")

# Excepciones por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError:#error por valor
    print("Se ha producido un ValueError")
except TypeError:#error por tipo de valor
    print("Se ha producido un TypeError")

# Captura de la información de la excepción

try:#para ver mas a detalle la excepcion por consola
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as my_random_error_name:#exception si es un error no controlado
    print(my_random_error_name)
