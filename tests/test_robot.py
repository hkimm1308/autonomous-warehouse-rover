from software.robot.robot import Robot


def test_robot_starts_at_start_position():
    robot = Robot(start_position=(0, 0))

    assert robot.current_position == (0, 0)
    assert robot.path == []
    assert robot.path_index == 0


def test_robot_sets_path():
    robot = Robot(start_position=(0, 0))

    path = [(0, 0), (0, 1), (0, 2)]
    robot.set_path(path)

    assert robot.path == path
    assert robot.path_index == 0
    assert robot.current_position == (0, 0)


def test_robot_moves_next():
    robot = Robot(start_position=(0, 0))

    path = [(0, 0), (0, 1), (0, 2)]
    robot.set_path(path)

    moved = robot.move_next()

    assert moved is True
    assert robot.current_position == (0, 1)
    assert robot.path_index == 1


def test_robot_stops_at_end_of_path():
    robot = Robot(start_position=(0, 0))

    path = [(0, 0), (0, 1)]
    robot.set_path(path)

    first_move = robot.move_next()
    second_move = robot.move_next()

    assert first_move is True
    assert second_move is False
    assert robot.current_position == (0, 1)


def test_robot_detects_goal_reached():
    robot = Robot(start_position=(0, 0))

    path = [(0, 0), (0, 1), (0, 2)]
    robot.set_path(path)

    robot.move_next()
    robot.move_next()

    assert robot.has_reached_goal((0, 2)) is True


def test_robot_gets_remaining_path():
    robot = Robot(start_position=(0, 0))

    path = [(0, 0), (0, 1), (0, 2), (0, 3)]
    robot.set_path(path)

    robot.move_next()

    assert robot.get_remaining_path() == [(0, 1), (0, 2), (0, 3)]