class Data:
    def __init__(self, key, data):
        self.key = key
        self.data = data

    def __str__(self):
        return "({0}, {1})".format(self.key, self.data)

class hash:

    def __init__(self,size,MaxCollision,Threshold):
        self.size = size
        self.table = [None for i in range(size)] #init table ให้ ทุกช่องเป็น None
        self.maxCollision = MaxCollision
        self.Threshold = Threshold
        self.prime = [2]
        self.checkTh = []

    def isFull(self):
        for i in self.table:
            if i is None: return False
        return True

    def addPrime(self,data):
        if data > 1:
            n = data
            while(True):
                for i in range(2,n):
                    if n-1 == i:
                        return n
                    if n % i == 0:
                        n += 1
                        break

    def rehash(self):
        self.size = self.addPrime(self.size * 2)
        self.table = [None for i in range(self.size)]

        for i in self.checkTh:
            index =  i % self.size
            realIndex , colI = index,0
            while self.table[index] is not None:
                colI+=1
                print(f"collision number {colI} at {index}")
                if colI == self.maxCollision:break
                index = (realIndex+colI**2) % self.size
            if self.table[index] is None:
                self.table[index] = i      

    def insertQuadatric(self, data):
        print(f"Add : {data}")
        if self.isFull():
            print("This table is full !!!!!!")
            exit()
        index = data % self.size
        realIndex, colI = index, 0
        while self.table[index] is not None:
            colI += 1
            print(f"collision number {colI} at {index}")
            if colI == self.maxCollision:
                print("****** Max collision - Rehash !!! ******")
                self.rehash()
                index = data % self.size
                break
            index = (realIndex + colI**2) % self.size
        self.checkTh.append(data)
        if len(self.checkTh) * 100 /self.size >= self.Threshold:
            print("****** Data over threshold - Rehash !!! ******")
            self.rehash()
            index = data % self.size
        else: self.table[index] = data

    def printTable(self):
        for i in range(self.size):
            print("#"+str(i+1)+"	",end="")
            if self.table[i] == None:print(None)
            else:print(self.table[i])
        print("----------------------------------------")

print(" ***** Rehashing *****")
k,lst = input("Enter Input : ").split("/")
sizeOfTable,MaxCollision,Threshold = map(int,k.split())
H = hash(sizeOfTable,MaxCollision,Threshold)
print("Initial Table :")
H.printTable()
for i in lst.split():
    H.insertQuadatric(int(i))
    H.printTable()
    