import numbers
import operator
import re
from functools import reduce
class Calculator():
    def __init__(self, input_path:str):
        with open(input_path, 'r')as f:
            data = f.read().strip()
        lines = data.split('\n')
        self.high = len(lines)
        self.matrix= [re.split("\s+",line.strip()) for line in lines]
        self.width = len(self.matrix[0])
        self.numbers = [[] for i in range(self.width)]
        self.operators= []


    def get_terms(self):
        for line_number in range(self.high):
            for row_number in range(self.width):
                current_value = self.matrix[line_number][row_number]
                if line_number == self.high-1:
                    self.operators.append(current_value)
                else:
                    self.numbers[row_number].append(int(current_value))

    def get_result(self):
        total = 0
        for i in range(len(self.operators)):
            if self.operators[i]== '+':
                res = sum(self.numbers[i])
            else:
                res= self.multiplication(self.numbers[i])
            total += res
        return total


    def multiplication(self, list):
        ret = list[0]
        for i in list[1:]:
            ret = ret * i
        return ret




c = Calculator("data.txt")
c.get_terms()
print(c.operators)
print(c.get_result())
