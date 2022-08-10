print(" *** Wind classification ***")
ans = float(input("Enter wind speed (km/h) : "))
if ans >= 209:
    print("Wind classification is Super Typhoon.")
elif ans > 102 and ans < 208.99:
    print("Wind classification is Typhoon.")
elif ans > 56 and ans < 101.99:
    print("Wind classification is Tropical Storm.")
elif ans > 52 and ans < 55.99:
    print("Wind classification is Depression.")
elif ans > 0 and ans < 51.99:
    print("Wind classification is Breeze.")
