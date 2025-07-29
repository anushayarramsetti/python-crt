# program to check amstrong number
n=int(input())
original=n
digits=len(str(n))
total=0
while n>0:
    digit=n%10
    total+=digit**digits
    n//=10
print("true" if total==original else "false")
#program to check if a given number is a perfect numbers
n=int(input())
sum_divisors=0
for i in range(1, n):
    if n % i == 0:
        sum_divisors += i
if sum_divisors == n:
    print("perfect")
else:
    print("not perfect")
# automophic number
n = int(input())
square = n * n
if str(square).endswith(str(n)):
    print("true")
else:
    print("false")
# program to count the occurrences of each chaacter
n=int(input())
s = input()
print("character occurrences:")
counted = set()
for char in s:
    if char not in counted:
        print(char, ":", s.count(char))
        counted.add(char)
# reverse a  string
n=int(input())
s= input()
print("reversed string:", s[::-1])