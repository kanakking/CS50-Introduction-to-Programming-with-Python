u_input = input("Input: ")
vowel = ["a", "e", "i", "o" ,"u"]
output = ""
for char in u_input:
    if char.lower() not in vowel:
        output += char

print("Output:", output)
