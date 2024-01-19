# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=9145

### Lambdas ### es una manera de crear una funcion muy concreta

def sum_two_values(
    first_value, second_value): return first_value + second_value
print(sum_two_values(2, 4))


def multiply_values(
    first_value, second_value): return first_value * second_value - 3
print(multiply_values(2, 4))


def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value #tambien puede usarse en el regreso de la info
print(sum_three_values(5)(2, 4))
