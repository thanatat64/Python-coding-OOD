def mini(nums):
    if len(nums) == 1:
        return nums[0]
    
    m = mini(nums[1:])
    if m < nums[0]:
        return m
    else:
        return nums[0]



inp = list(map(int,input("Enter Input : ").split()))
print(f"Min : {mini(inp)}")