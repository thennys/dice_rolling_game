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
            userInput = input("How many dice would you like to roll? (type 'exit' to quit) ")

            if userInput.lower() == 'exit':
                break

            dice_amount = int(userInput)
            rolls = rollDice(dice_amount)

            total_sum = sum(rolls)
            print(*rolls)

            # print(f"Rolls: ", ', ', {rolls})
            print(f"Total Sum of rolls: {total_sum}")
        


        except ValueError:
            print("Please enter a valid number or 'exit' to quit.")


if __name__ == '__main__':
    main()

