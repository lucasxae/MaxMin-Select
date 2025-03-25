# Projeto MaxMin Select

## Descrição do Projeto

Este projeto implementa o algoritmo **MaxMin Select**, que realiza a seleção simultânea do maior e do menor elemento de uma sequência de números utilizando a abordagem de **divisão e conquista**. O algoritmo é eficiente, pois reduz o número de comparações necessárias em relação a abordagens ingênuas.


### Lógica do Algoritmo

1. **Caso Base**: Se a lista contém apenas um elemento, esse elemento é tanto o maior quanto o menor. Se a lista contém dois elementos, uma única comparação determina o maior e o menor.
2. **Divisão**: Para listas com mais de dois elementos, a lista é dividida ao meio.
3. **Conquista**: O algoritmo é chamado recursivamente para as duas metades da lista.
4. **Combinação**: Os resultados das chamadas recursivas são combinados, comparando os máximos e mínimos de cada metade para determinar o máximo e o mínimo globais.

### Implementação em Python e Explicação Linha a Linha

```python
def maxMinSelect(lista):
```
- Define a função `maxMinSelect`, que recebe uma lista como entrada.

```python
    if len(lista) == 1:
        return lista[0], lista[0]
```
- Caso base: se a lista tiver apenas um elemento, ele é retornado como o maior e o menor ao mesmo tempo.

```python
    if len(lista) == 2:
        if lista[0] > lista[1]:
            return lista[0], lista[1]
        else:
            return lista[1], lista[0]
```
- Se a lista contiver exatamente dois elementos, fazemos uma comparação direta e retornamos o maior e o menor.

```python
    else:
        meio = len(lista) // 2
```
- Para listas com mais de dois elementos, determinamos o ponto médio para dividi-la em duas partes.

```python
        max1, min1 = maxMinSelect(lista[:meio])
        max2, min2 = maxMinSelect(lista[meio:])
```
- Chamamos a função recursivamente para as duas metades da lista.
- `max1` e `min1` armazenam o maior e menor elemento da primeira metade.
- `max2` e `min2` armazenam o maior e menor elemento da segunda metade.

```python
        return max(max1, max2), min(min1, min2)
```
- Comparamos os dois máximos e pegamos o maior deles.
- Comparamos os dois mínimos e pegamos o menor deles.
- Retornamos esses valores.

```python
def main():
```
- Define a função `main`, que será o ponto de entrada do programa.

```python
    lista = [34, 7, 23, 32, 5, 62, 32, 45, 78, 21, 56, 89, 12, 67, 43, 90, 11, 3, 99, 54]
```
- Cria uma lista de números de exemplo para o teste.

```python
    maximo, minimo = maxMinSelect(lista)
```
- Chama a função `maxMinSelect` e recebe os valores máximo e mínimo encontrados.

```python
    print(f"Lista: {lista}")
    print(f"Maior elemento: {maximo}")
    print(f"Menor elemento: {minimo}")
```
- Imprime a lista original e os valores obtidos.

```python
if __name__ == "__main__":
    main()
```
- Garante que o script será executado apenas quando chamado diretamente.


## Como Executar o Projeto

### Pré-requisitos

- Python 3.13.0 ou superior.
- Nenhuma dependência adicional é necessária.

### Passos para Executar

1. Clone este repositório:
    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd MaxMin-Select
    ```

2. (Opcional) Crie e ative um ambiente virtual:
    - No Windows:
        ```bash
        python -m venv .venv
        .venv\Scripts\activate
        ```
    - No macOS/Linux:
        ```bash
        python3 -m venv .venv
        source .venv/bin/activate
        ```

3. Execute o script principal:
    ```bash
    python main.py
    ```

---

## Relatório Técnico

### Análise da Complexidade Assintótica

#### Método de Contagem de Operações

O algoritmo realiza comparações para determinar os máximos e mínimos em cada etapa. A cada divisão da lista:

- Duas chamadas recursivas são feitas em listas de tamanho `n/2`.
- Após as chamadas recursivas, duas comparações adicionais são realizadas para combinar os resultados.

A relação de recorrência que descreve o número total de comparações é:

```
T(n) = 2T(n/2) + 2, para n > 2
T(2) = 1
T(1) = 0
```

Resolvendo essa recorrência, observa-se que o número total de comparações é aproximadamente `3n/2 - 2`. Portanto, a complexidade assintótica do algoritmo é `O(n)`, indicando que o número de comparações cresce linearmente com o tamanho da entrada.
#### Aplicação do Teorema Mestre

Considere a recorrência:  

T(n) = 2T(n/2) + O(1)


1. **Identifique os valores de** \( a \), \( b \) **e** \( f(n) \):  
   - \( a = 2 \), \( b = 2 \), \( f(n) = O(1) \).

2. **Calcule** \( \log_b a \):  
   - \( \log_2 2 = 1 \).

3. **Determine o caso do Teorema Mestre**:  
   - Como \( f(n) = O(n^{\log_b a}) \), estamos no **Caso 2**.

4. **Solução assintótica**:  
   - \( T(n) = O(n) \).


---

## Exemplos de Execução

### Entrada
```python
lista = [34, 7, 23, 32, 5, 62, 32, 45, 78, 21, 56, 89, 12, 67, 43, 90, 11, 3, 99, 54]
```

### Saída
```
Lista: [34, 7, 23, 32, 5, 62, 32, 45, 78, 21, 56, 89, 12, 67, 43, 90, 11, 3, 99, 54]
Maior elemento: 99
Menor elemento: 3
```

---


