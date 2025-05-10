"""Cree un programa que muestre  las tablas de multiplicar 
2 X 1 = 2
2 X 2 = 4
"""
TABLAS = 4
for n in range(1,TABLAS+1):
    print(f"*** TABLA DEL {n} CON FOR***")
    for i in range(1,10+1):
        print(f'{n} x {i} = {n*i}')
print("********")
n = 1
while n <= TABLAS:
    print( f"TABLa del {n}  con WHILE")
    for i in range(1,11):
        print(f'{n} x {i} = {n*i}')
    n +=1
    
    