# python software/simulation/grid_simulator.py

from software.navigation.grid_map import GridMap
from software.navigation.pathfinding import AStarPlanner


def print_grid_with_path(grid, path):
    path_set = set(path) if path else set()

    for row in range(grid.rows):
        row_items = []

        for col in range(grid.cols):
            position = (row, col)

            if grid.is_start(position):
                row_items.append("S")
            elif grid.is_goal(position):
                row_items.append("G")
            elif grid.is_obstacle(position):
                row_items.append("X")
            elif position in path_set:
                row_items.append("*")
            else:
                row_items.append(".")

        print(" ".join(row_items))


def main():
    warehouse = GridMap(rows=6, cols=8)

    start = (0, 0)
    goal = (5, 7)

    warehouse.set_start(start)
    warehouse.set_goal(goal)

    warehouse.add_obstacles([
        (1, 2),
        (1, 3),
        (2, 3),
        (4, 1),
        (4, 2),
    ])

    planner = AStarPlanner(warehouse)
    path = planner.find_path(start, goal)

    print("Warehouse path:")

    if path:
        print_grid_with_path(warehouse, path)
        print()
        print("Path:", path)
        print("Path length:", len(path))
    else:
        print_grid_with_path(warehouse, [])
        print()
        print("No path found.")


if __name__ == "__main__":
    main()