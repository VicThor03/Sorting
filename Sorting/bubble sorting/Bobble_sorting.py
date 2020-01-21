from timeit import time
from random import randrange

# Lista di partenza da ordinare
mylist = [randrange(1000) for _ in range(10)]

# Algoritmo di ordinamento
print("lista prima:")
print(mylist)

# Scrivere qui l'algoritmo di Bubble Sort
def bubbleSort(mylist):
    start_time = time.time()
    for idx in range(len(mylist)-1,0,-1):
        for i in range(idx):
            if mylist[i]>mylist[i+1]:
                temp = mylist[i]
                mylist[i] = mylist[i+1]
                mylist[i+1] = temp

    stop_time = time.time()
    print(f"{(stop_time-start_time):.7f}")
bubbleSort(mylist)



# Stampo la lista appena calcolata
print("lista dopo:")
print(mylist)
assert mylist==sorted(mylist)