'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...)
escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

'''

termos = int(input("Digite um número: "))

n1, n2 = 0, 1
count = 0
lista = []
while count < termos:
    lista.append(n1)
    n1, n2 = n2, n1 + n2
    count += 1

if termos in lista:
    print("O número {} pertence a sequencia de Fibonacci".format(termos))
else:
    print("O número {} não pertence a sequencia de Fibonacci".format(termos))