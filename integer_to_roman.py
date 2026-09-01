rom = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
num = 3749
# num = 1
# num = 3999
conv_val = ""

for key, value in rom.items():
    if num == 0:
        break
    count = num // key
    conv_val += (count * value)
    num -= count * key

print(conv_val)
