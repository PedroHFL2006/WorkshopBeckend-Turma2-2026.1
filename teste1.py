# Calcular Média Ponderada

a = int(input("Escolha o numero A:"))
b = int(input("Escolha o numero B:"))
c = int(input("Escolha o numero C:"))
peso_a = int(input("Escolha o peso A:"))
peso_b = int(input("Escolha o peso B:"))
peso_c = int(input("Escolha o peso C:")) 

media_ponderado = (a * peso_a) + (b * peso_b) + (c * peso_c) / (peso_a + peso_b + peso_c)
print(int(media_ponderado)) 
