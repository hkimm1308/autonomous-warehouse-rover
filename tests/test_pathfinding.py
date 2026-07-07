from software.navigation.grid_map import GridMap
from software.navigation.pathfinding import AStarPlanner


def test_astar_finds_path():
    grid = GridMap(rows=6, cols=8)

    start = (0, 0)
    goal = (5, 7)

    grid.set_start(start)
    grid.set_goal(goal)

    grid.add_obstacles([
        (1, 2),
        (1, 3),
        (2, 3),
        (4, 1),
        (4, 2),
    ])

    planner = AStarPlanner(grid)
    path = planner.find_path(start, goal)

    assert path is not None
    assert path[0] == start
    assert path[-1] == goal


def test_astar_avoids_obstacles():
    grid = GridMap(rows=4, cols=4)

    start = (0, 0)
    goal = (3, 3)

    grid.set_start(start)
    grid.set_goal(goal)

    grid.add_obstacles([
        (0, 1),
        (1, 1),
        (2, 1),
    ])

    planner = AStarPlanner(grid)
    path = planner.find_path(start, goal)

    assert path is not None

    for position in path:
        assert not grid.is_obstacle(position)


def test_astar_reroutes_after_new_obstacle():
    grid = GridMap(rows=6, cols=8)

    start = (0, 0)
    goal = (5, 7)

    grid.set_start(start)
    grid.set_goal(goal)

    grid.add_obstacles([
        (1, 2),
        (1, 3),
        (2, 3),
        (4, 1),
        (4, 2),
    ])

    planner = AStarPlanner(grid)

    original_path = planner.find_path(start, goal)
    assert original_path is not None

    new_obstacle = original_path[4]
    grid.add_obstacle(new_obstacle)

    rerouted_path = planner.find_path(start, goal)

    assert rerouted_path is not None
    assert new_obstacle not in rerouted_path
    assert rerouted_path[0] == start
    assert rerouted_path[-1] == goal


def test_astar_returns_none_when_blocked():
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
    path = planner.find_path(start, goal)

    assert path is None