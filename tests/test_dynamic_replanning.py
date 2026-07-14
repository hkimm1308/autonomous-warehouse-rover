from software.navigation.grid_map import GridMap
from software.navigation.pathfinding import AStarPlanner
from software.robot.robot import Robot
from software.simulation.dynamic_robot_simulator import next_position_is_blocked, replan_path


def test_next_position_is_blocked_returns_true():
    grid = GridMap(rows=3, cols=3)
    robot = Robot(start_position=(0, 0))

    path = [(0, 0), (0, 1), (0, 2)]
    robot.set_path(path)

    grid.add_obstacle((0, 1))

    assert next_position_is_blocked(grid, robot) is True


def test_next_position_is_blocked_returns_false():
    grid = GridMap(rows=3, cols=3)
    robot = Robot(start_position=(0, 0))

    path = [(0, 0), (0, 1), (0, 2)]
    robot.set_path(path)

    assert next_position_is_blocked(grid, robot) is False


def test_replan_path_finds_new_path_from_robot_position():
    grid = GridMap(rows=4, cols=4)

    start = (0, 0)
    goal = (3, 3)

    grid.set_start(start)
    grid.set_goal(goal)

    planner = AStarPlanner(grid)
    robot = Robot(start_position=start)

    original_path = planner.find_path(start, goal)
    robot.set_path(original_path)

    robot.move_next()

    new_path = replan_path(grid, planner, robot, goal)

    assert new_path is not None
    assert new_path[0] == robot.current_position
    assert new_path[-1] == goal


def test_replan_path_returns_none_when_no_route_exists():
    grid = GridMap(rows=3, cols=3)

    start = (0, 0)
    goal = (2, 2)

    grid.set_start(start)
    grid.set_goal(goal)

    grid.add_obstacles([
        (0, 1),
        (1, 0),
    ])

    planner = AStarPlanner(grid)
    robot = Robot(start_position=start)

    new_path = replan_path(grid, planner, robot, goal)

    assert new_path is None