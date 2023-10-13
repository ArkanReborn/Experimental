import random

ans = input("rock, paper, or scissors?\n")

aia = random.randint(1, 3)

if aia == 1:
    ai = "rock"
elif aia == 2:
    ai = "paper"
elif aia == 3:
    ai = "scissors"

if ai == "rock" and ans == "paper":
    print('Paper beats rock you win!')
elif ai == "paper" and ans == "scissors":
    print("Scissors beats paper you win!")
elif ai == "scissors" and ans == "rock":
    print("Rock beats scissors you win!")
elif ans == "rock" and ai == "paper":
    print('Paper beats rock you lost!')
elif ans == "paper" and ai == "scissors":
    print("Scissors beats paper you lost!")
elif ans == "scissors" and ai == "rock":
    print("Rock beats scissors you lost!")
elif ans == ai:
    print(f"We both choose {ans}! Let's try again!")