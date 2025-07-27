#positive numbers from list
n=list(map(int,(input().split())))
for num in n:
    if num > 0:
        print(num)
#find maximum of two numbers in python
a=int(input())
b=int(input())
print("max:",max(a,b),"min:",min(a,b))
#find length of list
n=list(map(int,input().split()))
print(len(n))
#revesing a list in python
n=list(map(int,input().split()))
reversed=n[::-1]
print(*reversed)
#find avrage(maximum -minimum) using args
def calculate_range(num):
    return max(num) - min(num)
num = list(map(int, input().split())) 
print(calculate_range(num)) 