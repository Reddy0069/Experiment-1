
x = 15
y = 6

# Relational Operators
print("Comparison Operators")
print("Is x greater:", x > y)
print("Is x smaller:", x < y)
print("Is x greater or equal:", x >= y)
print("Is x smaller or equal:", x <= y)
print("Are both equal:", x == y)
print("Are values different:", x != y)

# Arithmetic Operators
print("Mathematical Operators")
print("Sum:", x + y)
print("Difference:", x - y)
print("Product:", x * y)
print("Quotient:", x / y)
print("Integer Division:", x // y)

# Bitwise Operators
print("Bitwise Operations")
print("AND:", x & y)
print("XOR:", x ^ y)
print("NOT:", ~x)
print("Left Shift:", x << y)
print("Right Shift:", x >> y)

# Logical Operators
print("Logical Operations")
print((x > y) and (y > x))
print((x < y) or (y < x))
print(not x)

# Assignment Operators
print("Assignment Operations")
num = 12
print("Initial:", num)

num += 5
print("After addition:", num)

num -= 3
print("After subtraction:", num)

num *= 2
print("After multiplication:", num)

num /= 2
print("After division:", num)

num //= 2
print("After floor division:", num)

num %= 4
print("After modulus:", num)

num **= 2
print("After power:", num)

# Identity Operators
print("Identity Operations")
p = 25
q = 30
r = p

print(p is q)
print(p is not q)

# Membership Operators
print("Membership Operations")
colors = ["red", "blue", "green"]

print("yellow" not in colors)
print("blue" in colors)
