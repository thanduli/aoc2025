from copy import copy
import enum

def read_input(file_path: str):
    with open(file_path) as f:
        data = f.read().strip()
    return data


class Comperator():
    def __init__(self, file_path: str):
        input = read_input(file_path)
        input_part_one = input.split('\n\n')[0]
        self.ranges = [(int(i.split('-')[0]), int(i.split('-')[1])) for i in input_part_one.split('\n')]
        self.counter = 0


    def clean_ranges(self):
        sub_counter = 0
        while (True):
            if self.counter == len(self.ranges):
                break
            else:
                update = self.run_sub_counter()
                if update:
                   continue 
                else:
                    self.counter += 1

    def run_sub_counter(self):
        for i in range(len(self.ranges)):
            if i == self.counter:
                continue
            if self.compare(i)== True:
                self.update_values(i)                # change logic here
                return True
        return False

    def update_values(self, subcounter: int):
        self.ranges[self.counter] = (min(self.ranges[self.counter][0], self.ranges[subcounter][0]), 
                                     max(self.ranges[self.counter][1], self.ranges[subcounter][1]))
        self.ranges.pop(subcounter)
        self.counter = 0



    def compare(self, runner: int):
        lower = self.ranges[self.counter][0]
        upper = self.ranges[self.counter][1]
        if check_if_between(lower, upper, self.ranges[runner][0]) or check_if_between(lower, upper, self.ranges[runner][1]):
            return True
        else:
            return False

    def calculate_result(self):
        sum = 0
        for r in self.ranges:
            sum += r[1] - r[0] + 1
        return sum

def main():
    c = Comperator('data.txt')
    c.clean_ranges()
    print(c.calculate_result())



def check_if_between(lower, upper, number):
    if number >= lower and number<=upper:
        return True
    else:
        return False


    


if __name__== "__main__":
    main()
