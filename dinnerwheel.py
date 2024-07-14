import argparse
from dinner_ideas import dinner_raffle
import random


def create_dinner_lottery() -> list:
    """
    Creates a list of dinner ideas, which each appear the number of times specified
    by the number of tickets defined in 'dinner_ideas.py'. Similar to a lottery system.

    Returns
    list
        List of dinnery idea strings
    """

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
    """
    Shuffles the dinner lottery list and picks one off the top.

    Parameters
    lottery : list
        A list containing the dinner ideas to choose from
    """

    # Shuffle for good measure
    random.shuffle(lottery)

    # Choose a dinner
    print(f"Today's dinner idea is {lottery.pop()}!")


def choose_multiple_dinners(lottery: list, num: int):
    """
    Shuffles the dinner lottery list and picks num off the top.

    Parameters
    lottery : list
        A list containing the dinner ideas to choose from
    num : int
        The number of winners from the dinner lottery
    """

    # Shuffle for good measure
    random.shuffle(lottery)

    # Print out the n chosen dinner ideas
    print(f"Your dinner ideas are:")
    for _ in range(num):
        print(f"\t{lottery.pop()}")


def main_terminal(num_dinners: int):
    """
    The main function for running the dinner lottery through the terminal.

    Parameters
    num_dinners : int
        The number of dinners to choose
    """

    # Create list of dinner ideas
    dinner_lottery = create_dinner_lottery()

    if 1 == num_dinners:
        # Choose dinner
        choose_single_dinner(dinner_lottery)
    else:
        choose_multiple_dinners(dinner_lottery, num_dinners)


def parse_args() -> argparse.Namespace:
    """
    Parses the arguments.

    Arguments to dinnerwheel:
        number  : 1-5 the number of dinner selections
        gui     : bool representing if we should display the results in
                  a gui or in the terminal

    Returns
    Namespace
        The namespace that corresponds to the arguments for dinnerwheel
    """

    parser = argparse.ArgumentParser(
        prog="Dinnerwheel",
        description="Will choose random dinner ideas in a lottery format",
    )

    parser.add_argument("-n", "--number", choices=range(1, 6), default=1, type=int)
    parser.add_argument("-G", "--gui", action="store_true")

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    if args.gui:
        # Display the results with a GUI wheel that spins
        None
    else:
        # Display the results in the terminal
        main_terminal(args.number)
