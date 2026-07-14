class Robot:
    def __init__(self, start_position):
        self.current_position = start_position
        self.path = []
        self.path_index = 0

    def set_path(self, path):
        if not path:
            self.path = []
            self.path_index = 0
            return

        self.path = path
        self.path_index = 0
        self.current_position = path[0]

    def move_next(self):
        """
        Moves the robot one step along its current path.

        Returns:
            True if the robot moved
            False if there are no more moves
        """
        if self.path_index >= len(self.path) - 1:
            return False

        self.path_index += 1
        self.current_position = self.path[self.path_index]
        return True

    def has_reached_goal(self, goal):
        return self.current_position == goal

    def get_remaining_path(self):
        return self.path[self.path_index:]