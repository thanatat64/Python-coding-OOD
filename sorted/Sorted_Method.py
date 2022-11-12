def bubble(lst):
    for _ in range(len(lst)):
        for i in range(len(lst)-1):
            swaped = False
            count = 1
            while not swaped and count + i < len(lst):
                if lst[i] > lst[i+count] and lst[i] >= 0 and lst[i+count] >= 0:
                    lst[i], lst[i+count] = lst[i+count], lst[i]  # swap this line
                    swaped = True
                else:
                    count += 1
    return lst

def selection(lst):
    for last in range(len(lst)-1, 0, -1):
        biggest = lst[0]
        biggest_i = 0
        for i in range(1, last+1):
            if lst[i] > biggest:
                biggest = lst[i]
                biggest_i = i
        lst[last], lst[biggest_i] = lst[biggest_i], lst[last]
    return lst


def insertionSorted(lst):
    for i in range(1, len(lst)):
        iEle = lst[i]
        for j in range(i, -1, -1):
            if iEle < lst[j-1] and j > 0:
                lst[j] = lst[j-1]
            else:
                lst[j] = iEle
                return lst


ar = [3, 4, 7, 8, 12]
inp = list(map(int, input("Enter: ").split()))

print(f"Bubble--> {bubble(inp)}")
print(f"Selection--> {selection(inp)}")
print(f"Insertion--> {insertionSorted(inp)}")
