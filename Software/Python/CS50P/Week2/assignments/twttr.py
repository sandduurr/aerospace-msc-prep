word = input("tweet your tweet ")
vowels = "AEIOUaeiou"
result = ""

for letter in word:
    if letter not in vowels:
        result += letter


print(result)