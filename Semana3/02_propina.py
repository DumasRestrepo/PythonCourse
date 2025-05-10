" Ncesito calcular la factura + propina"
propina = 0.10 # 10%
valor_cena = float(input("Ingrse el costo de la cena: "))
costo_total = valor_cena + propina*valor_cena
factura =f""" ****** FACTURA *****
Almuerzo\t\t\tx1\t\t\t{valor_cena}
propina\t\t\t\t{propina*100}% \t\t\t{valor_cena*propina}
TOTAL\t\t\t\t\t\t{costo_total}
"""
print(factura)