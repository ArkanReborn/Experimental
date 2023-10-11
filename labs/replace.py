word = input("Please enter your password: \n")
password = ''

changes = {
    "i" : "1",
    "a" : "@",
    "m" : "M",
    "B" : "8",
    "s" : "$",
    "o" : "0"
}

for letter in changes:
    while letter in word:
        word = word.replace(letter, changes[letter])
print(f'Your new password is: {word}', end='!')
print() 