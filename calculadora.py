def salvar_historico(texto):
  with open("historico.txt", "a") as arquivo:
    arquivo.write(texto + "\n")

def adi(num1, num2):
    return num1 + num2

def subt(num1, num2):
    return num1 - num2

def multi(num1, num2):
    return num1 * num2

def divi(num1, num2):
    return num1 / num2

def expo(num1, num2):
    return num1 ** num2

def main():
  operacao = input("Qual a operação desejada? (+, -, *, /, **):")

  if operacao not in ["+", "-", "*", "/", "**"]: # "!="
    print("Valor Inválido")
  else:
    num1 = float(input("Coloque o valor num1: "))
    num2 = float(input("Coloque o valor num2: "))

    if operacao == "+":
      resultado = adi(num1, num2)
    elif operacao == "-":
      resultado = subt(num1, num2)
    elif operacao == "*":
      resultado = multi(num1, num2)
    elif operacao == "/":
      resultado = divi(num1, num2)
    elif operacao == "**":
      resultado = expo(num1, num2)

    print(f"Resultado: {resultado}")

    linha_historico = f"{num1} {operacao} {num2} = {resultado}"
    salvar_historico(linha_historico)

main()