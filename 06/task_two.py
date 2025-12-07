class Calculator():
    def __init__(self, input_path:str):
        with open(input_path, 'r')as f:
            data = f.read().strip()
        lines = data.split('\n')
        self.high = len(lines)
        self.matrix= [[c for c in line]for line in lines]
        self.width = len(self.matrix[0])
        self.operator_indexes =[]
        self.operators = []
        for index, op in enumerate(self.matrix[-1]):
            if op == '+' or op=='*':
                self.operator_indexes.append(index)
                self.operators.append(op)
        self.numbers = [[] for i in range(len(self.operators))]
        number_strings = ["" for i in range(self.width)]
        for line_index , line in enumerate(self.matrix[:-1]):
            for row_index, value in enumerate(line):
                number_strings[row_index]= number_strings[row_index] + value
        self.operator_indexes.append(self.width)
        for i in range(len(self.operator_indexes)-1):
            for h in range(self.operator_indexes[i], self.operator_indexes[i+1]):
                num = number_strings[h]
                if num.strip()!= '':
                    self.numbers[i].append(int(num))




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
print(c.get_result())
