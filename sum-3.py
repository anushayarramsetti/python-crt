#FILTER POSITIVE NUMBERS USING LIST COMPREHENSION
n=int(input())
nums=list(map(int,input().split()))
positive_nums=[str(num) for num in nums if num>0]
print(" ".join(positive_nums))