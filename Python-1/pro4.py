print("*** Fun with Drawing ***")
num=int(input("Enter input : "))
box = ((num-1)*4)+1
halfbox = box/2
for i in range(box):
    for j in range(box):
        up = i % 2 != 1 and j >= i and j <= box-i-1 and i < halfbox
        down = i % 2 != 1 and i >= j and j >= box-i-1 and i > halfbox
        left = j % 2 != 1 and j <= i and i <= box-j-1 and j < halfbox
        right = j % 2 != 1  and i <= j and  i >= box-j-1 and  j > halfbox
        if up or down or left or right:
            print("#", end = "")
        else:
            print(".", end = "")
    print()
    
