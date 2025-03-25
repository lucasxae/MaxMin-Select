# Desenvolver um programa em Python que implemente o algoritmo de seleção
# simultânea do maior e do menor elementos (MaxMin Select) de uma sequência
# de números, utilizando a abordagem de divisão e conquista. O projeto deverá ser
# entregue por meio de um link para o repositório do GitHub no CANVAS
#Sobre o algoritmo:
# O algoritmo de seleção simultânea (MaxMin Select) pode ser implementado de
#forma recursiva, utilizando a técnica de divisão e conquista. O problema é
#dividido em subproblemas menores que são resolvidos recursivamente, e seus
#resultados são combinados para encontrar o maior e o menor elementos com
#eficiência. Esse método reduz o número de comparações necessárias em
#comparação com uma abordagem ingênua.

def maxMinSelect(lista):
    if len(lista) == 1:
        return lista[0], lista[0]
    if len(lista) == 2:
        if lista[0] > lista[1]:
            return lista[0], lista[1]
        else:
            return lista[1], lista[0]
    else:
        meio = len(lista) // 2
        max1, min1 = maxMinSelect(lista[:meio])
        max2, min2 = maxMinSelect(lista[meio:])
        return max(max1, max2), min(min1, min2)
    
def main():
    lista = [34, 7, 23, 32, 5, 62, 32, 45, 78, 21, 56, 89, 12, 67, 43, 90, 11, 3, 99, 54]
    maximo, minimo = maxMinSelect(lista)
    print(f"Lista: {lista}")
    print(f"Maior elemento: {maximo}")
    print(f"Menor elemento: {minimo}")

if __name__ == "__main__":
    main()