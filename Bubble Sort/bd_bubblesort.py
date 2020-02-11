mylist=[6,8,3,45,7,87,11,32,44,43,22,1,56,2,9]
mylist2 = [9,8,7,6,5,4,3,2,1]


def bd_bubblesort(alist):
    start = 0
    end = len(alist)-1
    exchanged = True
    print('Unsorted list:',alist,'\n')
    while (exchanged==True):
        exchanged = False #changes flag to false when entering loop
        for i in range (start, end): #loop from left to right
            if (alist[i] > alist[i+1]):
                alist[i], alist[i+1]= alist[i+1], alist[i]
                print('Swapping',alist[i+1],'to the right with',alist[i])
                print('New List',alist,'\n')
                exchanged=True
        if (exchanged==False):
            break # if nothing changed list is sorted breaks out of loop
        exchanged = False # sets to false so it can be used in next part
        end = end-1
        for i in range(end-1, start-1,-1): # loops and compares from right to left 
            if (alist[i] > alist[i+1]):
                alist[i], alist[i+1] = alist[i+1], alist[i]
                print('Swapping',alist[i],'to the left with',alist[i+1])
                print('New List',alist,'\n')
                exchanged = True
        start = start+1 # increases starting point 
    print('Final sorted list:',alist)

bd_bubblesort(mylist)
    
    
