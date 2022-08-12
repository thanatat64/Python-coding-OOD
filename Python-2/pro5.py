import secrets


def bon(w):
    w = list(w)
    return (ord(max(set(w), key=w.count)) - 96) * 4
    

ans = input("Enter secret code : ")
print(bon(ans))
