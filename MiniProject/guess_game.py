import random


answer = random.randint(1, 10)

while True:
    player = int(input("Guess a number between 1 and 10: "))
    if player == answer:
        print(f"You guessed right! The number was {answer}")
        break
    elif player > answer:
        print(f"Too high!, reduce your guess ")
    elif player < answer:
        print(f"Too low!, increase your guess ")