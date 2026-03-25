#Find the largest element in a list.
def find_largest(lst):
    max_val = lst[0]
    for x in lst:
        if x > max_val:
            max_val = x
    return max_val
#Check if a number is even or odd.
num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
#Reverse a string (without slicing). 
def reverse_str(s):
    rev = ""
    for char in s:
        rev = char + rev
    return rev
#Count vowels in a string. 
s = "hello world"
count = 0

for char in s.lower():
    if char in "aeiou":
        count += 1

print("Vowels:", count)
#Find the sum of digits of a number. 
num = 1234
total = 0

while num > 0:
    total += num % 10
    num //= 10

print("Sum:", total)
#Check if a string is a palindrome. 
s = "madam"
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
#Print Fibonacci series up to N terms. 
n = 10
a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
#Swap two variables without a third variable. 
a = 5
b = 10

a, b = b, a

print(a, b)
#Count words in a sentence. 
s = "Hello world from Python"
words = s.split()
print("Word count:", len(words))
#Find minimum and maximum in a list 
lst = [4, 2, 9, 1, 7]
minimum = maximum = lst[0]

for num in lst:
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

print("Min:", minimum, "Max:", maximum)
#Find the second largest number in a list. 
lst = [10, 20, 4, 45, 99]
largest = second = float('-inf')

for num in lst:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest:", second)
#Remove duplicates from a list (without set). 
lst = [1, 2, 2, 3, 4, 4]
result = []

for num in lst:
    if num not in result:
        result.append(num)

print(result)
#Count frequency of elements in a list. 
lst = [1, 2, 2, 3, 3, 3]
freq = {}

for num in lst:
    freq[num] = freq.get(num, 0) + 1

print(freq)
#Merge two sorted lists.
a = [1, 3, 5]
b = [2, 4, 6]
merged = []
i = j = 0

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        merged.append(a[i])
        i += 1
    else:
        merged.append(b[j])
        j += 1

merged.extend(a[i:])
merged.extend(b[j:])

print(merged) 
#Find the intersection of two lists. 
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

intersection = []

for num in a:
    if num in b and num not in intersection:
        intersection.append(num)

print(intersection)
#Rotate a list by k positions. 
lst = [1, 2, 3, 4, 5]
k = 2

k = k % len(lst)
rotated = lst[-k:] + lst[:-k]

print(rotated)
#Check if two strings are anagrams. 
s1 = "listen"
s2 = "silent"

if sorted(s1) == sorted(s2):
    print("Anagrams")
else:
    print("Not Anagrams")
#Find the first non-repeating character. 
s = "aabbcde"

for char in s:
    if s.count(char) == 1:
        print("First non-repeating:", char)
        break
#Flatten a nested list. 
nested = [[1, 2], [3, 4], [5]]
flat = []

for sub in nested:
    for item in sub:
        flat.append(item)

print(flat)
#Find all pairs with a given sum. 
lst = [1, 2, 3, 4, 5]
target = 6

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == target:
            print(lst[i], lst[j])
#Print a right triangle pattern. 
n = 5
for i in range(1, n + 1):
    print("*" * i)
#Print a pyramid pattern.    
n = 5
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
#Print all prime numbers in a range. 
start = 1
end = 20

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)    
#Check if a number is Armstrong.
num = 153
order = len(str(num))
temp = num
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** order
    temp //= 10

if total == num:
    print("Armstrong")
else:
    print("Not Armstrong")
