def adi(num1, num2):
    return num1 + num2
    
def subt(num1, num2):
    return num1 - num2

def div(num1, num2):
    return num1 / num2

def multi(num1, num2):
    return num1 * num2

def main():
    operacao = input("Qual a formula que deseja?(+, -, *, ou /):")
    if (operacao != "+" and operacao != "-" and operacao != "*" and operacao != "/"):
        print("Valor invalido escolhido. Porfavor escolha outro valor.")
    else:
        num1 = float(input("Coloque o valor num1: "))
        num2 = float(input("Coloque o valor num2: "))
        if (operacao == "+"):
            print(adi(num1, num2))
        elif (operacao == "-"):
            print(subt(num1, num2))
        elif (operacao == "*"):
            print(multi(num1, num2))
        elif (operacao == "/"):
            print(div(num1, num2))

main()
