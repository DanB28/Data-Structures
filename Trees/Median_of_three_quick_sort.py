from timeit import Timer

def quickSort(alist):
   #print('Before Sort:',alist )
   quickSortHelper(alist,0,len(alist)-1)
  # print('After Sort:',alist)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   
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
           #print('my new list',alist)

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp
   print('new list',alist)
   print('pivot value',pivotvalue)
   print('right mark',rightmark)


   return rightmark




def motquickSort(alist):
  # print('Before Sort:',alist )
   motquickSortHelper(alist,0,len(alist)-1)
   #print('After Sort:',alist)

def motquickSortHelper(alist,first,last):
   if first<last:

       splitpoint = motpartition(alist,first,last)

       motquickSortHelper(alist,first,splitpoint-1)
       motquickSortHelper(alist,splitpoint+1,last)


def motpartition(alist,first,last):
   
   pivotindex = median(alist,first,last,(first+last)//2)
   alist[first],alist[pivotindex] = alist[pivotindex],alist[first]
   pivotvalue = alist[first]#first

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
           
   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp
   print('new list',alist)
   print('pivot value',pivotvalue)
   print('right mark',rightmark)
   return rightmark

def median(alist,first,last,middle):
    if alist[first]<alist[last]:
        return last if alist[last]<alist[middle] else middle
    else:
        return first if alist[first]<alist[middle] else middle

def testone():
   mylist = [1,4,65,10,37,8,11,33,77,12,66,34,4]
   quickSort(mylist)

def testtwo():
   mymotlist = [1,4,65,10,37,8,11,33,77,12,66,34,4]
   motquickSort(mymotlist)
   

def Final():
   print('Quicksort:')
   t1= Timer("testone()", "from __main__ import testone")
   timeone = t1.timeit(number=5)
   print('\n\nMedian of three:')
   t2= Timer("testtwo()", "from __main__ import testtwo")
   timetwo = t2.timeit(number=5)
   
   print("\nQuickSort time ",timeone, "milliseconds")
   print("\nMedian of three QuickSort time ", timetwo, "milliseconds")

   if timeone<timetwo:
      print('\nQuicksort was faster by',timetwo - timeone,'milliseconds')
   if timetwo<timeone:
      print('\nMedian of Three Quicksort was faster by',timeone - timetwo,'Milliseconds')
      
Final()







