# python software/navigation/grid_map.py

class GridMap:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.obstacles = set()
        self.start = None
        self.goal = None

    def in_bounds(self, position):
        row, col = position
        return 0 <= row < self.rows and 0 <= col < self.cols

    def is_obstacle(self, position):
        return position in self.obstacles

    def is_walkable(self, position):
        return self.in_bounds(position) and not self.is_obstacle(position)

    def add_obstacle(self, position):
        if self.in_bounds(position):
            self.obstacles.add(position)

    def add_obstacles(self, positions):
        for position in positions:
            self.add_obstacle(position)

    def remove_obstacle(self, position):
        self.obstacles.discard(position)

    def set_start(self, position):
        if self.is_walkable(position):
            self.start = position

    def set_goal(self, position):
        if self.is_walkable(position):
            self.goal = position

    def is_start(self, position):
        return position == self.start

    def is_goal(self, position):
        return position == self.goal

    def get_neighbors(self, position):
        row, col = position

        possible_neighbors = [
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1),
        ]

        neighbors = []

        for neighbor in possible_neighbors:
            if self.is_walkable(neighbor):
                neighbors.append(neighbor)

        return neighbors

    def print_grid(self):
        for row in range(self.rows):
            row_items = []

            for col in range(self.cols):
                position = (row, col)

                if self.is_start(position):
                    row_items.append("S")
                elif self.is_goal(position):
                    row_items.append("G")
                elif self.is_obstacle(position):
                    row_items.append("X")
                else:
                    row_items.append(".")

            print(" ".join(row_items))