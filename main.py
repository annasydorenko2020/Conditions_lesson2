#Task1
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))


if a > b and a > c:
   print(a)
elif b > a and b > c:
   print(b)
elif c > a and c > b:
   print(c)
elif a == b and b > c:
   print(b)
elif a == b and b < c:
   print(c)
elif c == b and c > a:
   print(c)
elif c == b and c < a:
   print(a)
elif a == c and c > b:
   print(a)
elif a == c and c < b:
   print(b)
else:
   print(a)

if a < b and a < c:
   print(a)
elif b < a and b < c:
   print(b)
elif c < a and c < b:
   print(c)
elif a == b and b < c:
   print(b)

elif c == b and c < a:
   print(c)

elif a == c and c < b:
   print(c)

else:
   print(b)

result = (a + b + c)/3
print(f"Result: {result}")

#Task2
number = int(input("Enter distance in meters: "))
n1 = number*0.000621371
n2 = number/0.0254
n3 = number/0.9114
print(f"Miles: {n1}\nInches: {n2}\nYards: {n3}")
