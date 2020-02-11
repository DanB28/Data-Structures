class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0


    def percUp(self,i):
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2

    def insert(self,k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)
      for item in self.heapList:
          print(item)
      return self.heapList

    def percDown(self,i):
      while (i * 2) <= self.currentSize:
          mc = self.minChild(i)
          if self.heapList[i] > self.heapList[mc]:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc

    def minChild(self,i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2] < self.heapList[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def delMin(self):
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percDown(1)
      return retval


    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1
        for item in self.heapList:
            print(str(item))
        return self.heapList

    def changePriority(self,name,newPriority):

        for item in self.heapList:
            temp = self.heapList[1:]
            if temp == name:
                print(item)
                temp[0]= newPriority
                self.percup()
                
        self.buildHeap(self.heapList)
        print(self.heapList)
        return self.heapList    


        
mylist = [(12,'H'),(9,'F'),(20,'B'),(6,'Z'),(16,'X'),(4,'C'),
          (14,'E'),(13,'W'),(15,'K'),(11,'S'),(5,'A'),(25,'J'),(7,'Q')]

myheap = BinHeap()
myheap.buildHeap(mylist)
print('\n')
myheap.changePriority('F',0)   
#myheap.insert((23,'P'))   




        
