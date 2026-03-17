# Calcular Média

#def calcular_media(notas):
#  soma = sum(notas)
#  quantidade = len(notas)
#  return soma / quantidade

#notas = [8, 9, 10, 7]
#media = calcular_media(notas)
#print(f"Média: ",media)

def calcular_media(notas):
  soma = sum(notas)
  quantidade = len(notas)
  
  if quantidade == 0:
    return 0
  return soma / quantidade

entrada_notas = input("Digite as notas separadas por vírgula (ex: 8.5, 9, 7.2): ")

notas_str = [nota.strip() for nota in entrada_notas.split(',')]

try:
  notas_do_usuario = [float(nota) for nota in notas_str if nota]
except ValueError:
  print("Erro: Certifique-se de que todas as entradas são números válidos.")
  notas_do_usuario = [] 

if notas_do_usuario:
  media = calcular_media(notas_do_usuario)
  print(f"Média das notas: {media:.2f}")
else:
  print("Nenhuma nota válida foi inserida para calcular a média.")
