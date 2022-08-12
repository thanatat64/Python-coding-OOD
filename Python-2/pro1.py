class trans:
    def deciToRoman(self, num):
        res = ""
        table = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
        for x, roman in table:
            d, m = divmod(num, x)
            res += roman * d
            num = m

        return res

    def romanToDeci(self, s):
        r_d = {'I': 1, 'V': 5, 'X': 10,
                     'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)):
            if i > 0 and r_d[s[i]] > r_d[s[i - 1]]:
                res += r_d[s[i]] - (2 * r_d[s[i - 1]])
            else:
                res += r_d[s[i]]
        return res
        


num = int(input("Enter number to translate : "))

print(trans().deciToRoman(num))
print(trans().romanToDeci(trans().deciToRoman(num)))
