import random
import time

tam_lista = 10000

valores_crescente = list(range(tam_lista))
valores_decrescente = list(reversed(range(tam_lista)))
valores_aleatorios = random.sample(range(tam_lista*10), tam_lista)


def insertionSort(arr):
    n = len(arr)
    qtd_troca = 0
    qtd_comp = 0

    for i in range(1, n):
        key = arr[i]
        j = i-1
        qtd_comp += 1
        while j >=0 and key < arr[j]:
            qtd_comp += 1
            arr[j+1] = arr[j]
            qtd_troca += 1
            j -= 1
        arr[j+1] = key

    return arr, qtd_troca, qtd_comp

inicio = time.time()

array_ordenado, qtd_troca, qtd_comp = insertionSort(valores_decrescente)

fim = time.time()
tempo_execucao = fim - inicio

print("Array after sorting:", array_ordenado)
print("Number of swaps:", qtd_troca)
print("Number of comparisons:", qtd_comp)
print("Tempo de execução: ", tempo_execucao, "segundos")