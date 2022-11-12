def sort(lst):
    lst = lst.copy()
    t = []
    while lst:
        t.append(lst.pop(minIndex(lst)))
    return t
        
def minIndex(lst):
    index = 0
    for i in range(len(lst)):
        if lst[i] < lst[index]:
            index = i
    return index

def findMedian(lst):
    lst = sort(lst)
    m1 = len(lst) // 2
    m2 = m1
    if len(lst) % 2 == 0:
        m2 = m1-1
    return (lst[m2] + lst[m1]) / 2
    

l = input("Enter Input : ").split()
if l[0] == 'EX':
    Ans = "Merge Sort"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    lst=list(map(int, l))
    ans = []
    for i in lst:
        ans.append(i)
        print(f"list = {ans} : median = {findMedian(ans)}")   


