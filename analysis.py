from timeit import Timer, timeit
from random import choice
from matplotlib import pyplot as plt

def bubbleSort(items):
    for i in range(len(items)-1,0,-1): # generate a range for the next step
        for j in range(i):             # note that the range i is decrementing
            if items[ j] > items[j+1]:
                items[ j], items[j+1] = items[j+1], items[ j] # swap items           

def mergeSort(items):
    #print("Splitting ",items)
    if len(items)>1:
        mid = len(items)//2
        l = items[:mid]
        r = items[mid:]
        mergeSort(l)
        mergeSort(r)
        #print("Merging ",items)
        i, j, k = 0, 0, 0
        while i < len(l) and j < len(r):
            if l[ i] <= r[ j]:
                items[ k] = l[ i]
                i += 1
            else:
                items[ k] = r[ j]
                j += 1
            k += 1
        while i < len(l):
            items[ k] = l[ i]
            i, k = i+1, k+1
        while j < len(r):
            items[ k] = r[ j]
            j, k = j+1, k+1
 
def insertionSort(items):
   for i in range(1,len(items)):
     m = items[ i]
     while i > 0 and items[ i-1] > m:
         items[ i] = items[ i-1]
         i -= 1
     items[ i] = m

list_ = list(range(0,500))      # list of numbers
d1 = [choice(list_) for i in range(10)]  # random list of size 10
d2 = [choice(list_) for i in range(20)]  # random list of size 20
d3 = [choice(list_) for i in range(50)] 
d4 = [choice(list_) for i in range(100)]  
d5 = [choice(list_) for i in range(200)]   
d6 = [choice(list_) for i in range(500)]  

# you need to add more lists of different sizes: d3, d4, d5, and d6
data = [d1, d2,d3,d4,d5,d6]  # your input
times1 = []       # times required to sort input
times2 = []
times3 = []



for i in data:
    t1 = Timer(f"bubbleSort({i})", "from __main__ import bubbleSort")
    #print("bubblesort ",t1.timeit(number=3), "milliseconds") # for debugging
    times1.append(t1.timeit(number=3)) # record the time required to sort the input


# print(t1.timeit(number=1))

# do not forget to plot your data!!!


data1 = [len(x) for x in data] # [[1,2,3], [1840238], []] - > [3, 1, 0]



plt.xlabel("size of input")               # add a label for the x axis
plt.ylabel("time")                # add a label for the y axis
plt.plot(data1, times1, c= 'lime',label ="Bubble Sort")


for i in data:
    t2 = Timer(f"mergeSort({i})", "from __main__ import mergeSort")
    #print('merge sort', t2.timeit(number=3))
    times2.append(t2.timeit(number=3))

data2 = [len(x) for x in data]



plt.xlabel("size of input")               # add a label for the x axis
plt.ylabel("time")                # add a label for the y axis
plt.plot(data2, times2, c= 'khaki',label ="Merge Sort")

for i in data:
    t3 = Timer(f"insertionSort({i})", "from __main__ import insertionSort")
    #print('insertionSort', t3.timeit(number=3))
    times3.append(t3.timeit(number=3))

data3 = [len(x) for x in data]


plt.title('Sorting Algorithm Analysis')
plt.xlabel("size of input")               # add a label for the x axis
plt.ylabel("time")                # add a label for the y axis
plt.plot(data3, times3, c= 'yellowgreen', label ="Insertion Sort" )

plt.legend(loc="upper left")
plt.show()