class SinglyLinkedList:     
    class Node :                    
        def __init__(self, data, next = None) :
            self.data = data
            if next is None :
                self.next = None
            else :
                self.next = next
        def __str__(self):
            return self.data
    def __init__(self):                
            self.head = None
            self.tail = None
            self.size = 0
            
    def __str__(self):
        s=''
        p = self.head
        while p != None :
            if p!=self.tail:
                s += str(p.data) + ' '
            else:
                s += str(p.data)
            p = p.next
        return s
          
    def __len__(self) :               
        return self.size         
            
    def isEmpty(self) :               
        return self.size == 0      

    def push(self,data):         
        if self.head is None :
          p = self.Node(data)
          self.head = p
          self.tail = p
          self.size += 1
        else :                        
          self.addTail(data)

    def addTail(self,data) :
        q = self.tail
        p = self.Node(data)
        q.next = p
        self.tail = p
        self.size += 1
    def removeTail(self) :
        if self.size > 0 :
          q = self.nodeAt(len(self)-2)
          self.tail = q
          q.next = None
          self.size -= 1
    def nodeAt(self,i) :             
        p = self.head
        for j in range(0,i) :
            p = p.next
        return p
    def merge(self,ll):
        while(not ll.isEmpty()):
            p=ll.tail
            self.push(p)
            ll.removeTail()
        return self
inp = input('Enter Input (L1,L2) : ').split(' ')
L1=SinglyLinkedList()
L2=SinglyLinkedList()
inL1=inp[0].split('->')
inL2=inp[1].split('->')
print('L1    : ',end='')
for a in inL1:
    print(a,end=' ')
    L1.push(a)
print('')
print('L2    : ',end='')
for a in inL2:
    print(a,end=' ')
    L2.push(a)
print('')
print ('Merge : '+str(L1.merge(L2)))