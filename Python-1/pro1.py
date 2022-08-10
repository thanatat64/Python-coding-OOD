print("*** Rabbit & Turtle ***")
ip = input("Enter Input : ").split(" ")
ip = [float(ip[0]),float(ip[1]),float(ip[2]),float(ip[3])]
ans = "{:.2f}".format(ip[0] / (ip[2]- ip[1]) * ip[3])
print(ans)
