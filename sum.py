# CHECK IF ALL VOWELS EXIST IN A STRING
s=input().split()
vowels={'a','e','i','o','u'}
if vowels.issubset(set(s)):
    print("true")
else:
    print("flase")