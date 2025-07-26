# sort a dictionary by keys
n=int(input())
data={}
for _ in range(n):
    name,score=input().split()
    data[name]=int(score)
    for name in sorted(data):
        print(f"{name}:{data[name]}")
#square of even numbers using list
n=int(input())
arr=list(map(int,input().split()))
squared=[x*x for x in arr if x%2==0]
print(*squared)
#find the maximum and minimum in a set
n=int(input())
num=set(map(int,input().split()))
print("max:",max(num),"min:",min(num))
#sum all values in a dictionary
n=int(input())
data={}
for _ in range(n):
    name, score = input().split()
    data[name] = int(score)
print(sum(data.values()))
#python program to find tuples which have all elements divisible by k from  list of tuples
n=int(input())
list=[tuple(map(int,input().split())) for _ in range(n)]
k=int(input())
for t in list:
    if all(x % k == 0 for x in t):
        print(t)