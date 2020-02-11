class node:
    def __init__(self,initdata):
        self.data = initdata
        self.next_node = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next_node

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext_node):
        self.next_node = newnext_node
