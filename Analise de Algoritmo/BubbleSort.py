import random
import time

tam_lista = 100000

valores_crescente = list(range(tam_lista))
valores_decrescente = list(reversed(range(tam_lista)))
valores_aleatorios = random.sample(range(tam_lista*10), tam_lista)


def bubbleSort(arr):
    n = len(arr)

    qtd_trocas = 0
    qtd_comp = 0

    # Realiza o loop apropriado vezes
    for i in range(n):
        # Cria uma flag para verificar se ocorreu troca ou não
        troca = False

        # Percorre o array da direita para a esquerda, 
        # comparando cada elemento com o próximo
        for j in range(0, n-i-1):
            qtd_comp += 1
            # Se o elemento atual for maior que o próximo, troca-os
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                troca = True
                qtd_trocas += 1

        # Se nenhuma troca ocorreu no loop interno, o array já está ordenado
        # e podemos sair do loop
        if troca == False:
            break
    return arr, qtd_trocas, qtd_comp


inicio = time.time()

arr_ordenado, qtd_trocas, qtd_comp = bubbleSort(valores_aleatorios)

fim = time.time()
tempo_execucao = fim - inicio

print("Array ordenado:", arr_ordenado)
print("Quantidade de trocas:",qtd_trocas)
print("Quantidade de comparações:", qtd_comp)
print("Tempo de execução: ", tempo_execucao, "segundos")