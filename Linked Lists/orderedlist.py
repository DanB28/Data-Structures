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

class ordered_list:
    
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

    def search(self,data):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData()==data:
                found = True
            else:
                if current.getData()>data:
                    stop = True
                else:
                    current = current.getNext()
            return found
    
    def add(self,data):
        current = self.head
        prev = None
        stop = False
        while current!=None and not stop:
            if current.getData()>data:
                stop = True
            else:
                prev = current
                current = current.getNext()
        temp = node(data)
        if prev ==None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            prev.setNext(temp)
        self.size+=1

    def length(self):
        current = self.head
        count = 0
        while current!= None:
            count = count + 1
            current =current.getNext()
        return count
    
    def getsize(self):
        return self.size
        
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
myorlist = ordered_list()
def run(orlist):

    orlist.add(10)
    orlist.add(20)
    orlist.add(30)
    orlist.add(40)
    orlist.add(50)
    orlist.add(60)
    orlist.add(70)
    orlist.add(80)
    orlist.add(90)

    print("My ordered list",orlist)
    orlist.remove(20)
    print("My list after remove(20)",orlist)
    orlist.remove(90)
    print("My list after remove(90)",orlist)
    orlist.remove(10)
    print("My list after remove(10)",orlist)
    orlist.add(10)
    orlist.add(90)
    orlist.add(20)

    print("Element 10 is in list position:",orlist.index(10))
    print("Element 30 is in list position:",orlist.index(30))
    print("Element 60 is in list position:",orlist.index(60))
    print("Element 90 is in list position:",orlist.index(90))

    print("popping:",orlist.pop())
    print("List after pop()",orlist)
    print("popping:",orlist.poppos(0))
    print("List after poppos(0)",orlist)
    print("popping:",orlist.poppos(4))
    print("List after poppos(4)",orlist)
    print("popping",orlist.poppos(orlist.size-1))
    print("List after pop(size-1)",orlist)
    print("Final List size:",orlist.size)

run(myorlist)

            
