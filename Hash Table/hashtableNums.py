from hashtable import HashTable
from random import randint

h = HashTable()


def run():
    for i in range(100):
        data = randint(1,100)
        h.put(data)
    print(h.data)
    
run()

        
        


