# FIND MAXIMUM NUMBER USING ARR
def find_maximum(*args):
    return max(args)
n=list(map(int, input().split()))
print(find_maximum(*n))
#count of digits of numbers using recursive function
def count_digits(n):
    if n < 10:
        return 1
    else:
        return 1 + count_digits(n // 10)
n = int(input())
print(count_digits(n))
# character ascii values
n=input()
ascii_map={char:ord(char) for char in n}
print(ascii_map)
# frequency count
n=input()
freq_map={}
for char in n:
    if char not in freq_map:
        freq_map[char] = 1
    else:
        freq_map[char] += 1
output=", ".join(f"{char}={freq_map[char]}" for char in freq_map)
print("{" + output + "}")
#module mapping
n=int(input())
numbers=list(map(int,input().split()))
module_map={}
for num in numbers:
    module_map[num] = num % 3
output=", ".join(f"{k}={v}" for k, v in module_map.items())
print("{" + output + "}")
#even length words
n=int(input())
words=input().split()
even_length_dict={word: len(word) for word in words if len(word) % 2 == 0}
output=", ".join(f"{k}={v}" for k, v in even_length_dict.items())
print("{" + output + "}")
#upper case mapping
n=int(input())
word_map={}
for _ in range(n):
    word=input().strip()
    word_map[word]= word.upper()
output=", ".join(f"{key}={value}" for key, value in word_map.items())
print("{" + output + "}")
#square dictionary
n=int(input()) 
result={}
for i in range(1, n + 1):
    result[i] = i * i
output=", ".join(f"{k}={v}" for k, v in result.items())
print("{" + output + "}")