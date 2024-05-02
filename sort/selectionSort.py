def selectionSort(array):
    for i in range(len(array)):
        min = i
        for j in range(i+1,len(array)):
            if (array[j]<array[min]):
                min = j
        (array[min],array[i]) = (array[i],array[min])

data =[24,34,1]
selectionSort(data)
print(data)