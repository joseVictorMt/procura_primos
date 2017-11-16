from teste_primos import fatoracaoIngenua, composicaoMiller, testeLucas

def ehPrimo(num): #Testa se 'num' e primo usando as tres funcoes abaixo.
    if (fatoracaoIngenua(num) > 1): #Se encontrar um fator maior que 1...
        return False
    if(composicaoMiller(num)): #Se esse teste nao for inconclusivo...
        return False
    if(not testeLucas(num)): #Se nao houver valor a de ordem N-1 em Zn...
        return False
    return True

while(True):
    try:
        num = long(input("Informe um inteiro qualquer:\n"))
        break
    except (ValueError, NameError):
        print("Valor invalido, tente novamente...")
    except (KeyboardInterrupt):
        print("Operacao cancelada pelo usuario.")
        raw_input("Pressione uma tecla para continuar...")
        exit(0)

if(num != 2): #Testar se 'num' nao e 2, que e o unico primo par.
    if(num % 2 == 0):
        num += 1
    while(not ehPrimo(num)): #Buscando um primo a partir de 'num'.
        num += 2
print (("\n%d eh o proximo primo.") %(num))

raw_input("\nPressione uma tecla para continuar...")
