from timeit import time
from random import randrange

# Lista di partenza da ordinare
mylist = [randrange(10000) for _ in range(1000)]

# Algoritmo di ordinamento
print("lista prima:")
print(mylist)
start_time = time.time()

# Scrivere qui l'algoritmo di Bubble Sort
def bubbleSort(mylist):
    for idx in range(len(mylist)-1,0,-1):
        for i in range(idx):
            if mylist[i]>mylist[i+1]:
                temp = mylist[i]
                mylist[i] = mylist[i+1]
                mylist[i+1] = temp

mylist = [14,46,43,27,57,41,845,21,70]
bubbleSort(mylist)
print(mylist)


stop_time = time.time()
print(f"{(stop_time-start_time):.7f}")


# Stampo la lista appena calcolata
print("lista dopo:")
print(mylist)