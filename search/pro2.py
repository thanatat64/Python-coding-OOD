def GreaterValue(lst,data):
    lst = sorted(lst)
    for i in lst:
        if i > data:
            return i
    return "No First Greater Value"

inp,k = input("Enter Input : ").split("/")
lst,data = [],[]
data.extend(map(int, k.split()))
lst.extend(map(int, inp.split()))
for i in data:
    print(GreaterValue(lst,i))
    


        

