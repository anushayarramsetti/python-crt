#program to check wheather a string is a palindrome
n=input()
if n==n[::-1]:
    print("palindrome")
else:
    print("not palindrome")

#second largest element in the list
n = int(input())
arr=list(map(int, input().split()))
new_arr=[]
for num in arr:
    if num not in new_arr:
        new_arr.append(num)
    if len(new_arr) < 2:
        print(-1)
    else:
        new_arr.sort()
        print(new_arr[-2])
#python remove duplicates from tuple
n = int(input())
nums= tuple(map(int, input().split()))
print(*nums)
#exception handling predict the output using eh
try:
    age= int(input("Enter your age: "))
    if age < 18:
        raise ValueError;
    else:
        print("You are is valid")
except ValueError:
    print("the age is not valid")
#product of array except self(leet code problem)
class Solution(object):
    def productExceptSelf(self, nums):
        n=len(nums)
        result = [1] * n
        left = 1
        for i in range(n):
            result[i] *= left
            left *= nums[i]
        right = 1
        for i in range(n-1, -1, -1):
            result[i] *= right
            right *= nums[i]
        return result