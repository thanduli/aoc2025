class Monyfolds():
    def __init__(self, inputpath):
        self.split_count = 0
        with open(inputpath, 'r') as f:
            self.data = []
            for line in f.readlines():
                if line != "":
                    self.data.append([c for c in line.strip()])

    def print_tree(self):
        for line in self.data:
            print(line, len(line))

    def get_indexes(self, line_number):
        index_list = []
        for index, value  in enumerate(self.data[line_number]):
            if value == "S" or value == "|" or type(value)==int:
                index_list.append(index)
        return index_list

    def update_line(self, line_number):
        update_indexes=self.get_indexes(line_number-1)
        line = self.data[line_number]
        for index in update_indexes:
            if type(self.data[line_number-1][index]) == int:
                old_value = self.data[line_number-1][index]
            else:
                old_value = 1
            if line[index] == '^':
                self.update_value(line_number, index-1,old_value)
                self.update_value(line_number, index+1, old_value)
                self.split_count += 1
            else:
                self.update_value(line_number, index, old_value)

    def update_value(self, line_number, index, old_value):
        value = self.data[line_number][index]
        if value == '.':
            self.data[line_number][index] = old_value
        else:
            self.data[line_number][index] = old_value + value

    def play_game(self):
        for line in range(1,len(self.data)):
            self.update_line(line)
        return sum([i for i in self.data[-1] if type(i) == int])



        



m = Monyfolds('data.txt')
print(m.play_game())

