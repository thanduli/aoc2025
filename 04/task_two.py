from copy import deepcopy


class Playfield():
    def __init__(self):
        with open('data.txt', 'r') as f:
            data=f.read()
        self.matrix = []
        for line in data.strip().split('\n'):
            self.matrix.append([c for c in line])
        self.new_matrix = deepcopy(self.matrix)
        self.width = len(self.matrix[0])
        self.high = len(self.matrix)
        print(self.matrix)

    def get_field(self,x,y):
        if x<0 or y<0:
            return ""
        try:
            return self.matrix[x][y]
        except:
            return ""
    
    def get_neighbors(self, x, y):
        return[(x-1,y-1), (x,y-1), (x+1,y-1),
                (x-1,y), (x+1,y),
                (x-1,y+1), (x,y+1), (x+1,y+1)
               ]

    def update_matrix(self, x, y):
        self.new_matrix[x][y] = "."


    def run_fields(self):
        sum = 0
        for y in range(self.high):
            for x in range(self.width):
                neighbors = self.get_neighbors(x,y)
                neighbors_valus = [self.get_field(n[0],n[1]) for n in neighbors]
                n_count = len([n for n in neighbors_valus if n == '@'])
                if self.get_field(x,y)== '@' and n_count < 4:
                    sum += 1
                    self.update_matrix(x,y)
        self.matrix = self.new_matrix
        return sum




p = Playfield()
total = 0
while(True):
    val = p.run_fields()
    if val == 0:
        break
    print(val)
    total += val


print(total)
