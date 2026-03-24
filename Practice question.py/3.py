#SECTION C: Coding Questions 
#9. Write a program to: - Take input string - Count vowels and consonants 
text = input("Enter a string: ").lower()
vowels = "aeiou"
v_count = 0
c_count = 0

for char in text:
    if char.isalpha():
        if char in vowels:
            v_count += 1
        else:
            c_count += 1

print(f"Vowels: {v_count}, Consonants: {c_count}")
#10. Write a program to: - Read a file - Count number of lines, words and characters 
with open("sample.txt", "r") as f:
    lines = f.readlines()
    line_count = len(lines)
    word_count = 0
    char_count = 0
    
    for line in lines:
        word_count += len(line.split())
        char_count += len(line)

print(f"Lines: {line_count}, Words: {word_count}, Characters: {char_count}")
#11. Write a program: - Create a class BankAccount - Methods: deposit, withdraw, check balance 
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. Balance: {self.balance}")
        else:
            print("Insufficient funds!")

    def check_balance(self):
        print(f"Current Balance: {self.balance}")
#12. Write a program: - Accept list of numbers - Remove duplicates 
#- Sort it without using sort() 
nums = [4, 2, 4, 1, 3, 2]
unique_nums = list(set(nums))
n = len(unique_nums)
for i in range(n):
    for j in range(0, n - i - 1):
        if unique_nums[j] > unique_nums[j + 1]:
            unique_nums[j], unique_nums[j + 1] = unique_nums[j + 1], unique_nums[j]

print(f"Unique Sorted List: {unique_nums}")
#13. Write a program using lambda + map + filter: - Square only even numbers from list
nums = [1, 2, 3, 4, 5, 6]
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))
print(result)