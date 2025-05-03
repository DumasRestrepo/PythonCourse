"""
tipo de Triangulo
"""
### Ingresar los lados
lado_a = int(input("ingrese la longitud del lado A: "))
lado_b = int(input("ingrese la longitud del lado B: "))
lado_c = int(input("ingrese la longitud del lado C: "))

## Determinaar si forman un triangulo
# a + b > c
# a + c > b
# b + c > a
if (lado_a + lado_b > lado_c) and (lado_a + lado_c > lado_b) and (lado_b + lado_c > lado_a):
# Determinar que tipo de triangulo es
# Equilatero : a ==b and b == c and c == a
# Isoceles (2 lados):
#               -  a == b and c != a
#               -  b == c and a != b
#               -  c == a and b != a   
# escaleno  a !=b and b!=c and a!=c  
    if lado_a == lado_b and lado_b == lado_c:
        print("El triangulo es equilatero")
    elif lado_a != lado_b and lado_b != lado_c and lado_a != lado_c:
        print("El triangulo es escaleno")
    elif (lado_a == lado_b and lado_b != lado_c) or (lado_b == lado_c  and lado_c != lado_a) or (lado_c == lado_a and lado_b != lado_a):
        print("El triangulo es isoceles")
else:
    print("Los lados no forman un triangulo")

           