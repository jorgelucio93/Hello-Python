# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=29327

### Classes ###

# Definición

class MyEmptyPerson:#buena practica mayuscula cada palabra y todo junto
    pass  # Para poder dejar la clase vacía y se ejecute el codigo


print(MyEmptyPerson)
print(MyEmptyPerson())

# Clase con constructor, funciones y popiedades privadas y públicas


class Person:
    def __init__(self, name, surname, alias="Sin alias"):#init para constructor de clase y esta es la forma de asignar variables de la clase.
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública y modificable, self para asignar propiedades dentro de la clase
        self.__name = name  # Propiedad privada y no se pueda modificar pero podemos llamarlo por lectura

    def get_name(self):#forma de llamar por lectura una propiedad privada
        return self.__name
        
    def walk(self):
        print(f"{self.full_name} está caminando")


my_person = Person("Brais", "Moure")#al no definir alias toma la propiedad por defecto asignada
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()


my_other_person = Person("Brais", "Moure", "MoureDev")#asignacion de valores a la clase
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León (El loco de los perros)"#se le puede cambiar la propiedad aunque se haya definido antes otro valor
print(my_other_person.full_name)

my_other_person.full_name = [6,'10',"hola"]
print (type(my_other_person.full_name))
