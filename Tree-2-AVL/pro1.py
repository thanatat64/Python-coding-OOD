class Node:
    def __init__(self, data, left: 'Node' = None, right: 'Node' = None, freq=None):
        self.data = data
        self.left = left
        self.right = right
        if freq is None:
            self.freq = left.freq + right.freq
        else:
            self.freq = freq

    def print(self, level=0):
        if self is None:
            return
        Node.print(self.right, level + 1)
        print('     ' * level, self.data)
        Node.print(self.left, level + 1)

    def __repr__(self) -> str:
        return self.data + "_" + str(self.freq)

def char_frequency(string):
    freq = {}
    for ch in string:
        freq[ch] = freq.get(ch, 0) + 1
    return freq


def huffman_code(root: Node, path=[], dic: dict = {}):
    if root is None:
        return dic

    if root.right is not None:
        dic = {**dic, **huffman_code(root.right, path + ['1'], dic)} # merge dict

    if root.left is not None:
        dic = {**dic, **huffman_code(root.left, path + ['0'], dic)}

    if root.left is None and root.right is None:
        dic = {**dic, root.data:"".join(path)}

    return dic


def huffman_encode(string: str, code: dict):
    return "".join([code[ch] for ch in string])


def char_priority(ch):
    return 0 if ch == '*' else ord(ch)
    

inp = input("Enter Input : ")
ch_freq = char_frequency(inp)
huff = [Node(key, freq=ch_freq[key]) for key in ch_freq]

while len(huff) > 1:
    huff.sort(key=lambda n: char_priority(n.data))
    huff.sort(key=lambda n: n.freq)
    huff.append(Node("*", huff.pop(0), huff.pop(0)))

ch_code = huffman_code(huff[0])
print(ch_code)
huff[0].print()
print(f"Encoded! : {huffman_encode(inp, ch_code)}")
