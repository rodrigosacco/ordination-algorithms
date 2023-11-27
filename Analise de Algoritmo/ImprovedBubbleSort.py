import random
import time

tam_lista = 10000

valores_crescente = list(range(tam_lista))
valores_decrescente = list(reversed(range(tam_lista)))
valores_aleatorios = random.sample(range(tam_lista*10), tam_lista)


def improvedBubbleSort(arr):
    n = len(arr)
    qtd_trocas = 0
    qtd_comp = 0

    for i in range(n):
        trocas = False
        for j in range(0, n-i-1):
            qtd_comp += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                qtd_trocas += 1
                trocas = True
        if not trocas:
            break

    return qtd_trocas, qtd_comp, arr

inicio = time.time()

qtd_trocas, qtd_comp, array_ordenado = improvedBubbleSort(valores_decrescente)

fim = time.time()
tempo_execucao = fim - inicio

print("Number of swaps:", qtd_trocas)
print("Number of comparisons:", qtd_comp)
print("Tempo de execução: ", tempo_execucao, "segundos")