# Indefinite Interactive Loop

def Positive_or_Negative():
    while True:
        answer = int(input("Please enter a number. Positive Number will continue. Negative Number will end the game. "))

        if answer > 0:
            print(answer)
        elif answer < 0:
            print("Game Over! Well Done!")
            break
        else: print("Please type a real integer")
Positive_or_Negative()
