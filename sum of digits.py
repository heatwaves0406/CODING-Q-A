n = int(input("Enter number: "))
s = 0

for digit in str(n):
    s += int(digit)

print("Sum =", s)