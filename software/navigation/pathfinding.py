import heapq


class AStarPlanner:
    def __init__(self, grid_map):
        self.grid_map = grid_map

    def heuristic(self, current, goal):
        """
        Manhattan distance heuristic for 4-direction grid movement.
        """
        current_row, current_col = current
        goal_row, goal_col = goal

        return abs(current_row - goal_row) + abs(current_col - goal_col)

    def reconstruct_path(self, came_from, current):
        """
        Rebuilds the final path by walking backward from goal to start.
        """
        path = [current]

        while current in came_from:
            current = came_from[current]
            path.append(current)

        path.reverse()
        return path

    def find_path(self, start, goal):
        """
        Runs A* search from start to goal.

        Returns:
            list of (row, col) coordinates if a path exists
            None if no path exists
        """
        open_set = []
        heapq.heappush(open_set, (0, start))

        came_from = {}

        g_score = {}
        g_score[start] = 0

        visited = set()

        while open_set:
            current_priority, current = heapq.heappop(open_set)

            if current == goal:
                return self.reconstruct_path(came_from, current)

            if current in visited:
                continue

            visited.add(current)

            for neighbor in self.grid_map.get_neighbors(current):
                tentative_g_score = g_score[current] + 1

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score

                    f_score = tentative_g_score + self.heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score, neighbor))

        return None