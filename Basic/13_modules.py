# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=34583

### Modules ###

from math import pi as PI_VALUE#para mandar a llamar libereria interna y una funcion especifica 
import math#para mandar a llamar toda la libreria 
from my_module import sumValue, printValue #para mandar a llamar un modulo(osea cualquier libreria interna o externa) y una funcion en especifico
import my_module#para mandar a llamar todo el modulo y todo lo que contenga 

my_module.sumValue(5, 3, 1)
my_module.printValue("Hola Python!")


sumValue(5, 3, 1)
printValue("Hola python")

print()
print(math.pi)
print(math.pow(2, 8))

print(PI_VALUE)
