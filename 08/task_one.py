import numpy as np
import copy

class DistanceChecker():
    def __init__(self, input_path):
        self.points = []
        self.distances = [] # distances between all vectors one dimensional
        self.mappings = [] # corresponding indexes
        self.groups = [] # groupings of neighbors

        input = []
        with open (input_path, 'r') as f:
            for line in f.readlines():
                vec = np.array([i for i in line.split(',')])
                self.points.append(vec)

    def get_distance(self, vector1, vector2):
        return np.linalg.norm(vector1, vector2)

    def set_distances(self):
        len_points = len(self.points)
        list_of_list_of_distances = []
        list_of_list_of_mappings= []
        current_check = 0
        for current_check in range(len_points - 1):
            current_mappings = []
            for comp in range(current_check + 1, len_points):
                current_mappings.append((current_check,comp))
                # add vectors
            list_of_list_of_mappings.append(current_mappings)


    def sort_distances(self):
        # sorte the lists 
        pass

    def check_if_in_group(self, pair):
        
        pass


    def handle_minimal_pair(self, pair):
        pass

d = DistanceChecker('example.txt')
d.set_distances()
