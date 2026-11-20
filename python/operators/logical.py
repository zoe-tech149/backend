age = 20

has_license = True

result = age >= 18 and has_license

print("Eligible to drive:", result)

x1 = True

x2 = False

x3 = x1 and x2 
print(f"x3 = {x3}")

b1 = 6
b2 = 3

b3 = (b1 * b2) > (b1 + b2)

print (f"b3 = {b3}")

a = True
b = False
c = False

result = (a or b) and not c

print(f"result = {result}")

b1 = True
b2 = True
b3 = False

b4 = b1 and b2 and (not b3)
print(f"b4 = {b4}")