# casino game
import random

def play():
    symbols = ['🍒', ' 🍇', '🍉', '7️⃣']
    winner = ['7️⃣', '7️⃣', '7️⃣']

    result = random.choices(symbols, k=3)
    while True:
        print(f'{result[0]} | {result[1]} | {result[2]}')
        if result == winner:
            print ('Jackpot!!')
        else:
            print('Thanks for playing!')

        Answer = input("y/n: ")

        if Answer == 'n':
            break


play()

