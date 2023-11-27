import random
import time

tam_lista = 100000

valores_crescente = list(range(tam_lista))
valores_decrescente = list(reversed(range(tam_lista)))
valores_aleatorios = random.sample(range(tam_lista*10), tam_lista)


def heapify(arr, n, i, qtd_trocas, qtd_comp):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    qtd_comp += 1
    if left < n and arr[i] < arr[left]:
        largest = left

    qtd_comp += 1
    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        qtd_trocas += 1
        qtd_trocas, qtd_comp = heapify(arr, n, largest, qtd_trocas, qtd_comp)
    return qtd_trocas, qtd_comp

def heapSort(arr):
    n = len(arr)
    qtd_trocas = 0
    qtd_comp = 0

    for i in range(n, -1, -1):
        qtd_trocas, qtd_comp = heapify(arr, n, i, qtd_trocas, qtd_comp)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        qtd_trocas += 1
        qtd_trocas, qtd_comp = heapify(arr, i, 0, qtd_trocas, qtd_comp)
    return arr, qtd_trocas, qtd_comp


inicio = time.time()

sorted_arr, qtd_trocas, qtd_comp = heapSort(valores_decrescente)

fim = time.time()
tempo_execucao = fim - inicio

print("Array ordenado: ", sorted_arr)
print("Numero de trocas: ", qtd_trocas)
print("Numero de comparações: ", qtd_comp)
print("Tempo de execução: ", tempo_execucao, "segundos")