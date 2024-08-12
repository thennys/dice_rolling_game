import random

def rollDice(amount: int = 2) -> list[int]: 
    if amount <= 0:
        raise ValueError
    
    rolls: list[int] = []
    for i in range (1,6):
        random_roll:int = random.randint(1, 6)
        rolls.append(random_roll)
    rolls.append(random_roll)

    return rolls