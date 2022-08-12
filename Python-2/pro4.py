def odd_even(type, data, mode):
    if type == "S":
        s = ""
        for x in range(len(data)):
            p = data[x]
            if mode == "Odd":
                if (x+1) % 2 == 1:
                    s += p
            elif mode == "Even":
                if (x+1) % 2 == 0:
                    s += p
        return s
    elif type == "L":
        j = []
        data = data.split(" ")
        for x in range(len(data)):
            p = data[x]
            if mode == "Odd":
                if (x+1) % 2 == 1:
                    j.append(p)
            elif mode == "Even":
                if (x+1) % 2 == 0:
                    j.append(p)
        return j


print("*** Odd Even ***")
ip = input("Enter Input : ").split(",")
print(odd_even(ip[0], ip[1], ip[2]))
