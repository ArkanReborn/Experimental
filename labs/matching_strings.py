uin1 = input()
uin2 = input()

ulen1 = len(uin1)
ulen2 = len(uin2)

checker = 0

if ulen1 > ulen2:
    for letter in range(ulen2):
        if uin1[letter] == uin2[letter]:
            checker += 1
    if checker > 1 or checker == 0:
        print(f"{checker} characters match")
    else:
        print(f"{checker} character matches")

elif ulen1 < ulen2:
    for letter in range(ulen1):
        if uin1[letter] == uin2[letter]:
            checker += 1
    if checker > 1 or checker == 0:
        print(f"{checker} characters match")
    else:
        print(f"{checker} character matches")

elif ulen1 == ulen2:
    for letter in range(ulen1):
        if uin1[letter] == uin2[letter]:
            checker += 1
    if checker > 1 or checker == 0:
        print(f"{checker} characters match")
    else:
        print(f"{checker} character matches")
