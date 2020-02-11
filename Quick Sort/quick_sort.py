from timeit import Timer

def quickSort(alist):
   print('Before Sort:',alist )
   quickSortHelper(alist,0,len(alist)-1)
   print('After Sort:',alist)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   
   pivotindex = median(alist,first,last,(first+last)//2)
   alist[first],alist[pivotindex] = alist[pivotindex],alist[first]
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp
           print('my new list',alist)

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp
   print('new list',alist)
   print('p',pivotvalue)
   print('rm',rightmark)


   return rightmark

def median(alist,first,last,middle):
    if alist[first]<alist[last]:
        return last if alist[last]<alist[middle] else middle
    else:
        return first if alist[first]<alist[middle] else middle

mylist = [1,4,65,10,37,8,11,33,77,12,66,34,4]

quickSort(mylist)





