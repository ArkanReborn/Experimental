user_score = 0
simon_pattern = input()
user_pattern = input()

for letter in range(len(simon_pattern)):
    if simon_pattern[letter] == user_pattern[letter]:
        user_score += 1
    else:
        break
print(f"User score: {user_score}")
