class node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

    def hasNext(self):
        return self.next!= None

class linked_list:
    
    def __init__(self):
        self.head = None
        self.size = 0
        
    def __str__(self):
        current= self.head
        string = ""
        while current != None:
            string += str(current)+ " "
            current = current.getNext()
        return string
            
        
    def isEmpty(self):
        return self.head == None
        
    def getsize(self):
        return self.size
    
    def add(self,data):
        temp = node(data)
        temp.setNext(self.head)
        self.head = temp
        self.size+=1

    def search(self,data):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData()==data:
                found == True
            else:
                current = current.getNext()
        return found
        

    def length(self):
        current = self.head
        count = 0
        while current!= None:
            count = count + 1
            current =current.getNext()
        return count
    
        
    def append(self,data):
        current = self.head
        end = False 
        while current != None and not end:
            if current.getNext()==None:
                new_data = node(data)
                current.setNext(new_data)
                end = True
            else:
                current = current.getNext()
        self.size+=1

    def insert(self,data,pos):
        if  pos> self.size:
            print("Index out of range")
            return
        
        new_node = node(data)
        
        if self.isEmpty():
            self.add(data)

        if pos == 0:
            self.add(data)
        
        elif pos == self.size:
            self.append(data)

        else:
            current_pos =0
            prev = None
            current = self.head
            while current_pos != pos:
                prev = current
                current = current.getNext()
                current_pos +=1
            new_node.setNext(current)
            prev.setNext(new_node)

            self.size+=1

    def remove(self,data):
        current = self.head
        prev = None
        found = False
        while not found:
            if current.getData()== data:
                found = True
            else:
                prev = current
                current = current.getNext()
        if prev == None:
            self.head = current.getNext()
        else:
            prev.setNext(current.getNext())
        self.size -=1
        

    def index(self,data):
        pos =0
        current = self.head
        while current != None:
            if current.data == data:
                return pos
            current = current.getNext()
            pos+=1
            
    def pop(self):
        temp = self.head
        prev = None
        while temp!=None:
            prev = temp
            temp = temp.getNext()
        popped = prev.getData()
        self.remove(popped)
        return popped
        
        self.size -=1
        temp = self.setNext()

    def poppos(self,index):
        pos = 0
        temp = self.head
        while pos != index:
            temp = temp.getNext()
            pos+=1
        popped = temp.getData()
        self.remove(popped)
        return popped
        temp = self.setNext()
        
        
                
            
             
             
                
            
        
mylist = linked_list()
mylist.add(80)
mylist.add(50)
mylist.add(90)
mylist.add(40)
mylist.add(20)
mylist.add(60)
mylist.add(10)
mylist.add(30)
mylist.add(70)




print("My unordered Linked List:",mylist)## prints linked list 
mylist.append(130)## appends 130 to end of linked list 
mylist.append(150)## appends 150 to end of linked list
print("\nList after appends:",mylist)## prints linked list after append
mylist.insert(200,0)
mylist.insert(400,mylist.size)
mylist.insert(300,4)
print("\nlist after inserts:",mylist)## after insert

print("\nElement 200 is in position:",mylist.index(200))
print("\nElement 90 is in position:",mylist.index(90))
print("\nElement 400 is in position:",mylist.index(400))

print("\nPopping:",mylist.pop())
print("\nlist after pop()",mylist)
print("\nPopping",mylist.poppos(0))
print("\nList after pop(0)",mylist)
print("\nPopping",mylist.poppos(7))
print("List after poppos(7)",mylist)
print("\npopping",mylist.poppos(mylist.size-1))
print("List after pop(size-1)",mylist)
print("\nFinal List size:",mylist.size)


        
      
        
