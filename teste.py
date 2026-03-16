#Média Ponderada

a = int(input("Escolha o numero a:"))
b = int(input("Escolha o numero b:"))
c = int(input("Escolha o numero c:"))
peso_a = int(input("Escolha o peso a:"))
peso_b = int(input("Escolha o peso b:"))
peso_c = int(input("Escolha o peso c:"))

media_ponderado = (a * peso_a) + (b * peso_b) + (c * peso_c) / (peso_a + peso_b + peso_c)
print(int(media_ponderado))

