# -*- coding: utf-8 -*-
from teste_primos import fatoracaoIngenua, composicaoMiller, testeLucas

# Verifica se o parâmetro 'num' e primo usando os seguintes procedimentos:
# Fatoração ingênua; Teste da Composição e de Miller; e Teste de Lucas.
def ehPrimo(num):
    # Verifica se a fatoração ingênua encontrou um divisor maior que 1 para 'num'.
    if (fatoracaoIngenua(num) > 1):
        return False
    # Verifica se a Composição de Miler foi conclusiva para 'num'. 
    if(composicaoMiller(num)):
        return False
    # Verifica se o Teste de Lucas concluiu que 'num' não é primo.
    if(not testeLucas(num)):
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

# Testar se 'num' não é 2, que é o unico primo par.
if(num != 2):
    if(num % 2 == 0):
        num += 1
    while(not ehPrimo(num)): # Busca um primo a partir de 'num'.
        num += 2
print (("\n%d eh o proximo primo.") %(num))

raw_input("\nPressione uma tecla para continuar...")
