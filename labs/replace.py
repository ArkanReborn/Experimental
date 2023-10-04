word = input()
password = ''

changes = {
    "i" : "1",
    "a" : "@",
    "m" : "M",
    "B" : "8",
    "s" : "$"
}

for letter in changes:
    while letter in word:
        word = word.replace(letter, changes[letter])
print(word, end='!')
print() 