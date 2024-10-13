user_input = input("Input: ")
vowels = ['a','e','i','o','u','A','E','I','O','U']
mod = ""
for c in user_input:
    if c not in vowels:
        mod += c

print(f"Output: {mod}")
