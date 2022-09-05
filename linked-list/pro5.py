class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.value)


def createLL(LL):
    head = None
    tail = None
    for i in LL:
        if head is None:
            head = Node(i)
            tail = head
        else:
            tail.next = Node(i)
            tail = tail.next
    return head
            
def printLL(head: Node):
    s = ""
    while head is not None:
        s += str(head.data) + " "
        head = head.next
    return s
    
def SIZE(head: Node):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count

def nodeAt(head: Node, id):
    cur = head
    for i in range(id):
        cur = cur.next
    return cur

def splitLL(head: Node, count):
    before = nodeAt(head,count-1)
    split = before.next
    before.next = None
    return split
    
def bottomUp(head: Node, count, size):
    if count == 0 or count == size:
        return head
    tail = nodeAt(head,size-1)
    newHead = splitLL(head, count)
    tail.next = head
    return newHead

def appendNode(head: Node,n: Node):
    if head is None:
        return n
    cur = head
    while cur.next is not None:
        cur = cur.next
    cur.next = n
    return head

def riffle(head: Node, count):
    second = splitLL(head, count)
    newHead = None
    while head is not None or second is not None:
        if head is not None:
            remain = splitLL(head,1)
            head,remain = remain,head
            newHead = appendNode(newHead,remain)
        if second is not None:
            remain = splitLL(second,1)
            second,remain = remain,second
            newHead = appendNode(newHead,remain)
    return newHead

def deRiffle(head: Node, count, size):
    first = second = None
    while head is not None:
        if SIZE(first) < count:
            remain = splitLL(head,1)
            head,remain = remain,head
            first = appendNode(first,remain)
        if SIZE(second) < size - count:
            remain = splitLL(head,1)
            head,remain = remain,head
            second = appendNode(second,remain)
    nodeAt(first,count-1).next = second #tail
    return first
    
def scarmble(head: Node, b, r, size):
    bCount = int(size*b/100) #ปัดเศษลง
    rCount = int(size*r/100)
    head = bottomUp(head,bCount,size)
    print(f"BottomUp {b:.3f} % : {printLL(head)}")
    head = riffle(head,rCount)
    print(f"Riffle {r:.3f} % : {printLL(head)}")
    head = deRiffle(head,rCount,size)
    print(f"Deriffle {r:.3f} % : {printLL(head)}")
    head = bottomUp(head,size - bCount,size)
    print(f"Debottomup {b:.3f} % : {printLL(head)}")


inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
for i in inp2.split('|'):
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)