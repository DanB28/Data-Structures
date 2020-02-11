class HashTable:
    def __init__(self):
        self.size = 129
        self.data = [None] * self.size

    def put(self,data):
      hashvalue = self.hashfunction(data)
      count = 1
      print("hashvalue for ", data, " is: ", hashvalue)

      #if slot is empty, store data
      if self.data[hashvalue] == None:
         self.data[hashvalue] = data
      else:
          #slot is not empty, so rehash until find empty slot
          print("collision when placing ",data)
          nextslot = self.rehash(hashvalue,self.size,count)
          while self.data[nextslot] != None:
            count += 1
            nextslot = self.rehash(hashvalue,self.size,count)
          
          self.data[nextslot]=data
         

    def hashfunction(self,x):
        #Takes mod of int from hash size
         
         return (x % self.size)
        
    def rehash(self,oldhash,size,count):
        #collision resolution is linear probing with "plus 1" rehash
        print("rehashing oldhash of ",oldhash)
        print("new hash = ", (oldhash + ((count)**2))%size)
        
        return (oldhash+(count)**2)%size


