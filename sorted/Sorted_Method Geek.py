def bubble(lst):
    size = len(lst)
    for i in range(size):
        for j in range(0,size-i-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    return lst

def selection(lst):
    for i in range(len(lst)):
    # Find the minimum element in remaining
    # unsorted array
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[min_idx] > lst[j]:
                min_idx = j        
        # Swap the found minimum element with
        # the first element       
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst


# Python program for implementation of Insertion Sort
 
# Function to do insertion sort
def insertionSorted(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def shellSort(arr):
    n = len(arr)
    gap=n//2
    while gap>0:
        j=gap
        while j<n:
            i=j-gap # This will keep help in maintain gap value
            while i>=0:
                if arr[i+gap]>arr[i]:
                    break
                else:
                    arr[i+gap],arr[i]=arr[i],arr[i+gap]
                i=i-gap # To check left side also
            j+=1
        gap=gap//2
    return arr

def shellSort2(arr):
    n = len(arr)
    gap = n//2
    while gap > 0:
        for i in range(gap,n):
            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = arr[i]
            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            while  j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap
            # put temp (the original a[i]) in its correct location
            arr[j] = temp
        gap //= 2
    return arr

def mergeSort(arr):
    if len(arr) > 1:
         # Finding the mid of the array
        mid = len(arr)//2
        # Dividing the array elements
        L = arr[:mid]
        # into 2 halves
        R = arr[mid:]
        # Sorting the first half
        mergeSort(L)
        # Sorting the second half
        mergeSort(R) 
        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def quickSort(lst):
    return [] if not lst else quickSort([i for i in lst[1:] if i < lst[0]]) + [lst[0]] + quickSort([i for i in lst[1:] if i >= lst[0]])

ar = [3, 4, 7, 8, 12]
inp = list(map(int, input("Enter: ").split()))

# print(f"Bubble--> {bubble(inp)}")
# print(f"Selection--> {selection(inp)}")
# print(f"Insertion--> {insertionSorted(inp)}")
# print(f"Shell--> {shellSort(inp)}")
# print(f"Shell2--> {shellSort2(inp)}")
# print(f"Merge--> {mergeSort(inp)}")
print(f"Quick--> {quickSort(inp)}")