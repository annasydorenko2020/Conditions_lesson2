# print("Hellow world!")
# print("Stay safe!")
# print("Slack-community")
# print("Discord mode")
# print("Discord mode2")
# print("Slack-community2")
# print("Telegram")
# number = 15
# print(number)
# number = 45,5
# print(number)
# print("Victor")
#
# number = int(input("Enter 3-digit number: "))
# 762
# n1 = number // 100
# n2 = number % 100//10
# n3 = number % 10
# result = n1 + n2 + n3
# print(f"n1: {n1} n2: {n2} n3: {n3}")
# print(f"Result: {result}")
# print()
# print()
# diagonal1 = int(input("Enter diagonal 1: "))
# diagonal2 = int(input("Enter diagonal 2: "))
#
# result = (diagonal1 * diagonal2)/2
# print(f"diagonal1: {diagonal1} diagonal2: {diagonal2}")
# print(f"Result: {result}")
# print()
# number = int(input("Enter 4-digit number: "))
# n1 = number//1000
# n2 = number % 1000 // 100
# n3 = number % 100 // 10
# n4 = number % 10
# result = n1 * n2 * n3 * n4
# print(f"n1: {n1} n2: {n2} n3: {n3} n4: {n4}")
# print(f"Result: {result}")

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
