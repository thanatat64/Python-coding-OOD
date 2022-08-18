

class Stack():
    def __init__(self, lst=None):
        if lst == None:
            self.items = []
        else:
            self.items = lst

    def push(self, s):
        self.items.append(s)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


print("******** Parking Lot ********")
maxCar, carLst, pro, numCar = input(
    "Enter max of car,car in soi,operation : ").split()
maxCar, numCar = int(maxCar), int(numCar)
s = Stack()
if carLst != '0':
    s.push(carLst.split(","))
else:
    s.push([])
for x in s.items:
    s.items = x  
if pro == 'arrive':
    if s.size() >= maxCar:
        print(f"car {numCar} cannot arrive : Soi Full")
    elif str(numCar) in s.items:
        print(f"car {numCar} already in soi") # case 3
    elif s.size() < maxCar and numCar not in s.items:
        s.push(str(numCar))
        print(f"car {numCar} arrive! : Add Car {numCar}")
elif pro == 'depart':
    if str(numCar) not in s.items and s.items !=[]:
        print(f"car {numCar} cannot depart : Dont Have Car {numCar}")#case 7
    elif s.items != []:
        id = s.items.index(str(numCar))
        s.items.pop(id)
        print(f"car {numCar} depart ! : Car {numCar} was remove")
    else:
        print(f"car {numCar} cannot depart : Soi Empty") # case 5 pass
print([int(i) for i in s.items])

# case 9pass
