print('you can also do decimal in it')
num = float(input("Enter a decimal number: "))


integer_part = int(num)
fractional_part = num - integer_part


binary_int = ""
if integer_part == 0:
    binary_int = "0"
while integer_part > 0:
    remainder = integer_part % 2
    binary_int = str(remainder) + binary_int
    integer_part = integer_part // 2


binary_frac = ""
count = 0  
while fractional_part > 0 and count < 10:
    fractional_part *= 2
    bit = int(fractional_part)
    binary_frac += str(bit)
    fractional_part -= bit
    count += 1


if binary_frac != "":
    binary = binary_int + "." + binary_frac
else:
    binary = binary_int

print("Binary:", binary)