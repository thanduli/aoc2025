from dataclasses import dataclass
from math import ceil
from math import floor

@dataclass
class turn():
    direction: str
    amount: int


class Lock():
    def __init__(self):
        self.possition = 50
        self.zero_count = 0

    def click_left(self):
        if self.possition == 0:
            self.possition = 99
        else:
            self.possition -= 1

    def click_right(self):
        if self.possition == 99:
            self.possition = 0
        else:
            self.possition += 1

    def check_is_null(self):
        if self.possition == 0:
            self.zero_count += 1

    # for task one check if null ater loop, for task 2 in loop for every click
    def make_turn(self, turn:turn):
        if turn.direction == "L":
            for i in range(turn.amount):
                self.click_left()
                self.check_is_null()
        if turn.direction == "R":
            for i in range(turn.amount):
                self.click_right()
                self.check_is_null()


def get_turns(filename: str):
    turns = []
    with open(filename) as f:
        for line in f.readlines():
            turns.append(turn(line[0], int(line[1:])))
    return turns


def main():
    turns = get_turns("input.txt")
    lock1 = Lock()
    for turn in turns:
        lock1.make_turn(turn)
    print(f"Amount of zeros: {lock1.zero_count}")


if __name__ == "__main__":
    main()
