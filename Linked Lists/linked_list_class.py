class linked_list:
    
    def _init_(self,data=none):
        self.end = data
        self.size =0
        
    def getsize(self):
        return self.size
    
    def add(self,data):
        new_node = node(data.self,root)
        self.root = new_node
        self.size +=1

    def remove(self,data):
        this_node = self.end
        prev_node = none
        while this_node:
            if this_node.get_data() == data:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.end = this_node
                    self.size+=1
                    return True
            else:
                prev_node = this_node
                this_node = this_node.get_next())
            return False #data not found
    def find(self,data):
        this_node = self.end
        while this_node:
            if this_node.getdata()== data:
                return data
            else:
                self.end = this_node.get_next()
        return none
    
                
        
                
        
        
      
        
