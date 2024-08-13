import random

def rollDice(amount: int = 2) -> list[int]: 
    if amount <= 0:
        raise ValueError
    
    rolls: list[int] = []
    for i in range (amount):
        random_roll:int = random.randint(1, 6)
        rolls.append(random_roll)  

    return rolls


def main():
    while True:
        try:
            userInput = input("How many dice woukd you like to roll? ")

            if userInput.lower() == 'exit':
                break

            print(*rollDice (int(userInput)), sep=', ')

        except ValueError:
            print("Enter a valid number")


if __name__ == '__main__':
    main()

