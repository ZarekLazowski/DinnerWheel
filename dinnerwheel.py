import argparse
from dinner_ideas import dinner_raffle
import random

def create_dinner_lottery() -> list:
    lottery_tickets = []

    # For each dinner idea...
    for dinner in dinner_raffle:
        num_tix = dinner[1]
        dinner_name = dinner[0]

        # ... create an entry in the lottery num_tix amount of times
        for _ in range(num_tix):
            lottery_tickets.append(dinner_name)
    
    return lottery_tickets

def choose_single_dinner(lottery: list):
    # Shuffle for good measure
    random.shuffle(dinner_lottery)

    # Choose a dinner
    print(f"Today's dinner idea is {dinner_lottery.pop()}!")

def choose_multiple_dinners(lottery: list, num: int):
    # Shuffle for good measure
    random.shuffle(dinner_lottery)
    
    # Print out the n chosen dinner ideas
    print(f"Your dinner ideas are:\n")
    for _ in range(num):
        print(f"{lottery.pop()}\n")

if __name__ == "__main__":
    # Create list of dinner ideas
    dinner_lottery = create_dinner_lottery()

    # Choose dinner
    choose_single_dinner(dinner_lottery)
    