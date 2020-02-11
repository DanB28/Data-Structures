class HashTable:
    def __init__(self):
        self.size = 13
        self.data = [None] * self.size

    def put(self,data):
      hashvalue = self.hashfunction(data)
      print("hashvalue for ", data, " is: ", hashvalue)

      #if slot is empty, store data
      if self.data[hashvalue] == None:
         self.data[hashvalue] = data
      else:
          #slot is not empty, so rehash until find empty slot
          print("collision when placing ",data)
          nextslot = self.rehash(hashvalue,self.size)
          while self.data[nextslot] != None:
            nextslot = self.h2(data)

          
          self.data[nextslot]=data
         

    def hashfunction(self,data):
        sum=0
        #Takes ordinal of first char of string
        for pos in range(len(data)):
            sum = sum+ord(data[pos])
        return (sum % self.size)
    
    def h2(self,data):
        sum=0
        for pos in range(len(data)):
            sum = sum +ord(data[pos])*10
        return (sum % self.size)    
        
    def rehash(self,oldhash,size):
        #collision resolution is linear probing with "plus 1" rehash
        print("rehashing oldhash of ",oldhash)
        print("new hash=", (oldhash+1)%size)
        return (oldhash+1)% size

h = HashTable()


h.put('brecker')
h.put('corea')
h.put('davis')
h.put('hancock')
h.put('harris')
h.put('marsalis')
h.put('parker')

print(h.data)


