vowels = "ioeyuaEYUIOA"

userInput = input()
userVowels = ""

for item in userInput:
    if item in vowels:
        userVowels += item

print(userVowels)