from timeit import time
from random import randrange

# Mi riscrivo una funzione che trova il minimo di una lista


def mymin(list):
    m_idx = 0
    m = list[0]
    for n_idx, n in enumerate(list):
        
        if n < m:
            m = n
            m_idx = n_idx
    return m, m_idx


# Lista di partenza da ordinare
mylist = [randrange(1000) for _ in range(10)]


# Algoritmo di ordinamento
print(mylist)
start_time = time.time()
for idx in range(len(mylist)):
    m, m_idx = mymin(mylist[idx::])
    print(f"m: {m}, m_idx: {m_idx}")
    swap = mylist[idx]
    mylist[idx] = m
    mylist[m_idx] = swap

stop_time = time.time()
print(f"{(stop_time-start_time):.7f}")


# Stampo la lista appena calcolata
print(mylist)

# alla fine voglio che siano soddisfatte le seguenti condizioni
# assert sorted_list[0] == 7
# assert sorted_list[1] == 15
# assert sorted_list[2] == 99
# assert sorted_list[3] == 200
