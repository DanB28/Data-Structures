
def quicksort(alist):
   print('Before Sort:',alist )
   quickSortHelper(alist,0,len(alist)-1)
   print('After Sort:',alist)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint)
       quickSortHelper(alist,splitpoint+1,last)


      
def partition(alist,first,last):
   
   med = (last-first)//2
   med = med+first
   leftmark = first+1  

   if (alist[med]-alist[last])*(alist[first]-alist[med])>=0:
      swap(alist,first,med)
      
   elif((alist[last])-alist[med])*(alist[first]-alist[last])>=0:
      swap(alist,first,last)
      print('Swaping',alist[first],alist[last])
   pivot = alist[first]
   for rightmark in range(first,last):
      if pivot > alist[rightmark]:
         swap(alist,leftmark,rightmark)
         
         leftmark = leftmark +1
   swap(alist,first,leftmark-1)
  
   return leftmark-1

def swap(alist,a,b):
   alist[a],alist[b] = alist[b],alist[a]
   print('Swaping',alist[a],' with ',alist[b])


mylist = [34,4,2,5,3,20,8,1,33,77,12,66,21]
quicksort(mylist)

