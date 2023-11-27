import random
import time
import sys

sys.setrecursionlimit(5000000)

tam_lista = 10000

valores_crescente = list(range(tam_lista))
valores_decrescente = list(reversed(range(tam_lista)))
valores_aleatorios = random.sample(range(tam_lista*10), tam_lista)


def partition(arr, low, high):
    global qtd_comp
    global qtd_trocas
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        qtd_comp += 1
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            qtd_trocas += 1

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    global qtd_comp
    global qtd_trocas
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

qtd_comp = 0
qtd_trocas = 0
arr = valores_decrescente
n = len(arr)

inicio = time.time()

quick_sort(arr, 0, n - 1)

fim = time.time()
tempo_execucao = fim - inicio

print("Array organizada", arr)
print("Total Comparisons:", qtd_comp)
print("Total Swaps:", qtd_trocas)
print("Tempo de execução: ", tempo_execucao, "segundos")