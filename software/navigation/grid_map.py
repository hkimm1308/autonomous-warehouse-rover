# python software/navigation/grid_map.py

class GridMap:
    """
    Represents a 2D warehouse grid for robot navigation.

    Each cell is represented by a row-column coordinate:
    (row, col)

    Example:
        (0, 0) is the top-left cell.
    """
    def __init__(self, width, height, start=None, goal=None, obstacles=None):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.goal = goal
        self.start = start
        self.obstacles = set(obstacles) if obstacles is not None else set()

    def in_bounds(self, position):
        """Return True if a position is inside the grid."""
        row, col = position
        return 0 <= row < self.height and 0 <= col < self.width

    def is_obstacle(self, position):
        """Return True if a position is blocked by an obstacle."""
        return position in self.obstacles

    def is_walkable(self, position):
        """Return True if the robot can move onto this position."""
        return self.in_bounds(position) and not self.is_obstacle(position)

    def add_obstacle(self, position):
        """Add an obstacle to the grid."""
        if self.in_bounds(position):
            self.obstacles.add(position)
        else:
            raise ValueError(f"Obstacle position {position} is outside the grid.")
        
    def add_obstacles(self, positions):
        """Add multiple obstacles to the grid."""
        for position in positions:
            self.add_obstacle(position)

    def remove_obstacle(self, position):
        """Remove an obstacle from the grid."""
        self.obstacles.discard(position)

    def set_start(self, position):
        """Set the robot's starting position."""
        if self.is_walkable(position):
            self.start = position
        else:
            raise ValueError(f"Start position {position} is invalid.")

    def set_goal(self, position):
        """Set the robot's goal position."""
        if self.is_walkable(position):
            self.goal = position
        else:
            raise ValueError(f"Goal position {position} is invalid.")
        
    def is_start(self, position):
        """
        Return True if the given position is the robot's starting location.
        """
        return position == self.start

    def is_goal(self, position):
        """
        Return True if the given position is the goal location.
        """
        return position == self.goal

    def get_neighbors(self, position):
        """
        Return valid neighboring cells.

        For now, the robot can move:
        up, down, left, and right.
        """
        row, col = position

        possible_neighbors = [
            (row - 1, col),  # up
            (row + 1, col),  # down
            (row, col - 1),  # left
            (row, col + 1),  # right
        ]

        return [
            neighbor
            for neighbor in possible_neighbors
            if self.is_walkable(neighbor)
        ]

    def print_grid(self):
        """Print the grid in the terminal."""
        for row in range(self.height):
            row_cells = []

            for col in range(self.width):
                position = (row, col)

                if self.is_start(position):
                    row_cells.append("S")
                elif self.is_goal(position):
                    row_cells.append("G")
                elif position in self.obstacles:
                    row_cells.append("X")
                else:
                    row_cells.append(".")

            print(" ".join(row_cells))

    


if __name__ == "__main__":
    warehouse = GridMap(
        width=8,
        height=6,
        start=(0, 0),
        goal=(5, 7),
        obstacles={(1, 2), (1, 3), (2, 3), (4, 1), (4, 2)}
    )

    warehouse.print_grid()

    print("Neighbors of start:", warehouse.get_neighbors((0, 0)))
