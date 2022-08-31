class Queue:
    def __init__(self, lst=None):
        if lst == None:
            self.items = []
        else:
            self.items = lst

    def enQueue(self, s):
        self.items.append(s)

    def deQueue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def getQ(self):
        return self.items

    def str(self):
        s = []
        for e in self.getQ():
            s.append(e[0][1] + ":" + e[1][1]) 
        return ", ".join(s)
    
    def str2(self):
        s = []
        for e in self.getQ():
            s.append(str(e[0][0]) + ":" + str(e[1][0]))
        return ", ".join(s)

Activity = [
    [0, "Eat"],
    [1, "Game"],
    [2, "Learn"],
    [3, "Movie"]
]
Place = [
    [0, "Res."],
    [1, "ClassR."],
    [2, "SuperM."],
    [3, "Home"]
]

lst = input("Enter Input : ").split(",")
qMe, qHer = Queue(), Queue()
for x in lst:
    l = x.split(" ")
    a = list(map(int,l[0].split(":")))
    b = list(map(int,l[1].split(":")))
    qMe.enQueue([Activity[a[0]],Place[a[1]]])
    qHer.enQueue([Activity[b[0]],Place[b[1]]])
print("My   Queue =",qMe.str2())
print("Your Queue =",qHer.str2())
print("My   Activity:Location =",qMe.str())
print("Your Activity:Location =",qHer.str())
score = 0
while  not qMe.isEmpty() and not qHer.isEmpty():
    if qMe.items[0][0] == qHer.items[0][0] and qMe.items[0][1] != qHer.items[0][1]: score += 1
    elif qMe.items[0][0] != qHer.items[0][0] and qMe.items[0][1] == qHer.items[0][1]: score += 2
    elif qMe.items[0][0] == qHer.items[0][0] and qMe.items[0][1] == qHer.items[0][1]: score += 4
    elif qMe.items[0][0] != qHer.items[0][0] and qMe.items[0][1] != qHer.items[0][1]: score -= 5
    qMe.deQueue()
    qHer.deQueue()
if score >= 7: print(f"Yes! You're my love! : Score is {score}.")
elif score < 7 and score > 0: print(f"Umm.. It's complicated relationship! : Score is {score}.")
elif score < 0 : print(f"No! We're just friends. : Score is {score}.")