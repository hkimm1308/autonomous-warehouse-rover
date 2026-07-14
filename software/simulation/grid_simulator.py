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


def run_planner(grid, planner, start, goal, label):
    path = planner.find_path(start, goal)

    print(label)

    if path:
        print_grid_with_path(grid, path)
        print()
        print("Path:", path)
        print("Path length:", len(path))
    else:
        print_grid_with_path(grid, [])
        print()
        print("No path found.")

    print("-" * 60)
    return path


def add_obstacle_and_reroute(grid, planner, start, goal, obstacle, label):
    print(f"New obstacle detected at {obstacle}")
    grid.add_obstacle(obstacle)
    print()

    return run_planner(grid, planner, start, goal, label)


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

    original_path = run_planner(
        warehouse,
        planner,
        start,
        goal,
        "Scenario 1: Original warehouse route"
    )

    if original_path:
        first_reroute = add_obstacle_and_reroute(
            warehouse,
            planner,
            start,
            goal,
            obstacle=(0, 4),
            label="Scenario 2: Reroute after blocked aisle"
        )

    if first_reroute:
        second_reroute = add_obstacle_and_reroute(
            warehouse,
            planner,
            start,
            goal,
            obstacle=(3, 4),
            label="Scenario 3: Reroute after second obstacle"
        )

    print("Scenario 4: Blocking part of the lower route")
    warehouse.add_obstacles([
        (3, 5),
        (3, 6),
        (3, 7),
        (4, 7),
    ])

    final_path = run_planner(
        warehouse,
        planner,
        start,
        goal,
        "Final route check after multiple blocked aisles"
    )


if __name__ == "__main__":
    main()