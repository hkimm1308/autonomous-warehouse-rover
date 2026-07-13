from software.navigation.grid_map import GridMap
from software.navigation.pathfinding import AStarPlanner
from software.robot.robot import Robot


def print_grid_with_robot(grid, robot, path):
    path_set = set(path) if path else set()

    for row in range(grid.rows):
        row_items = []

        for col in range(grid.cols):
            position = (row, col)

            if position == robot.current_position:
                row_items.append("R")
            elif grid.is_start(position):
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


def next_position_is_blocked(grid, robot):
    remaining_path = robot.get_remaining_path()

    if len(remaining_path) < 2:
        return False

    next_position = remaining_path[1]
    return grid.is_obstacle(next_position)


def replan_path(grid, planner, robot, goal):
    new_path = planner.find_path(robot.current_position, goal)

    if new_path is None:
        return None

    robot.set_path(new_path)
    return new_path


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
    robot = Robot(start)

    path = planner.find_path(start, goal)

    if path is None:
        print("No initial path found.")
        return

    robot.set_path(path)

    print("Initial route:")
    print_grid_with_robot(warehouse, robot, robot.get_remaining_path())
    print("-" * 60)

    step = 0
    obstacle_added = False

    while not robot.has_reached_goal(goal):
        step += 1

        # Simulate a new obstacle appearing while the robot is moving.
        if step == 4 and not obstacle_added:
            new_obstacle = robot.get_remaining_path()[2]
            warehouse.add_obstacle(new_obstacle)
            obstacle_added = True

            print(f"Dynamic obstacle appeared at {new_obstacle}")
            print_grid_with_robot(warehouse, robot, robot.get_remaining_path())
            print("-" * 60)

        if next_position_is_blocked(warehouse, robot):
            print("Robot detected blocked path. Replanning...")

            new_path = replan_path(warehouse, planner, robot, goal)

            if new_path is None:
                print("No alternate path found. Robot stopped.")
                print_grid_with_robot(warehouse, robot, [])
                return

            print("New route found:")
            print_grid_with_robot(warehouse, robot, robot.get_remaining_path())
            print("-" * 60)

        moved = robot.move_next()

        if not moved:
            print("Robot cannot move further.")
            return

        print(f"Step {step}: Robot moved to {robot.current_position}")
        print_grid_with_robot(warehouse, robot, robot.get_remaining_path())
        print("-" * 60)

    print("Robot reached the goal.")


if __name__ == "__main__":
    main()