import random
import time

tam_lista = 100000

valores_crescente = list(range(tam_lista))
valores_decrescente = list(reversed(range(tam_lista)))
valores_aleatorios = random.sample(range(tam_lista*10), tam_lista)

def merge_sort(arr):
    global comparisons
    global swap
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            comparisons += 1
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            swap += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            swap += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            swap += 1


comparisons = 0
swap = 0
arr = valores_decrescente

inicio = time.time()

merge_sort(arr)

fim = time.time()
tempo_execucao = fim - inicio

print(f"Array ordenado: {arr}")
print(f"Total de comparações: {comparisons}")
print(f"Total de trocas: {swap}")
print("Tempo de execução: ", tempo_execucao, "segundos")