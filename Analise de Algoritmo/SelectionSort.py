import random
import time

tam_lista = 10000

valores_crescente = list(range(tam_lista))
valores_decrescente = list(reversed(range(tam_lista)))
valores_aleatorios = random.sample(range(tam_lista*10), tam_lista)

def selection_sort(lista):
    qtd_trocas = 0
    qtd_comp = 0

    for i in range(len(lista)):
        menor = i
        for j in range(i + 1, len(lista)):
            qtd_comp += 1
            if lista[j] < lista[menor]:
                menor = j

        lista[i], lista[menor] = lista[menor], lista[i]
        qtd_trocas += 1

    return lista, qtd_trocas, qtd_comp

inicio = time.time()

sorted_list, qtd_trocas, qtd_comp = selection_sort(valores_decrescente)

fim = time.time()
tempo_execucao = fim - inicio

print("Lista ordenada: ", sorted_list)
print("Trocas: ", qtd_trocas)
print("Comparações: ", qtd_comp)
print("Tempo de execução: ", tempo_execucao, "segundos")