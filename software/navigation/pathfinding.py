# python software/navigation/pathfinding.py

class AStarPlanner:
    """
    Finds the shortest path through a GridMap using the A* search algorithm.
    """

    def __init__(self, grid_map):
        """
        Store the grid map that the planner will search.
        """
        self.grid_map = grid_map

    def heuristic(self, position, goal):
        """
        Estimate the distance from the current position to the goal.

        This uses Manhattan distance because the rover can currently move
        only up, down, left, and right.
        """
        current_row, current_col = position
        goal_row, goal_col = goal

        row_distance = abs(current_row - goal_row)
        col_distance = abs(current_col - goal_col)

        return row_distance + col_distance


if __name__ == "__main__":
    from software.navigation.grid_map import GridMap

    warehouse = GridMap(
        width=8,
        height=6,
        start=(0, 0),
        goal=(5, 7),
    )

    planner = AStarPlanner(warehouse)

    print("Heuristic from start to goal:", planner.heuristic(warehouse.start, warehouse.goal))