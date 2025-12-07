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
            print(line)

    def get_indexes(self, line_number):
        index_list = []
        for index, value  in enumerate(self.data[line_number]):
            if value == "S" or value == "|":
                index_list.append(index)
        return index_list

    def update_line(self, line_number):
        update_indexes=self.get_indexes(line_number-1)
        line = self.data[line_number]
        for index in update_indexes:
            if line[index] == '^':
                line[index -1] = '|'
                line[index +1] = '|'
                self.split_count += 1
            else:
                line[index] = '|'

    def play_game(self):
        for line in range(1,len(self.data)):
            self.update_line(line)
        return self.split_count



        



m = Monyfolds('data.txt')
print(m.play_game())

