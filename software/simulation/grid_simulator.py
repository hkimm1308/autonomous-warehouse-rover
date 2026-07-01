# python software/simulation/grid_simulator.py

from software.navigation.grid_map import GridMap


def create_sample_warehouse():
    """Create a sample warehouse grid for testing navigation."""
    warehouse = GridMap(width=8, height=6)

    warehouse.set_start((0, 0))
    warehouse.set_goal((5, 7))

    warehouse.add_obstacles([
        (1, 2),
        (1, 3),
        (2, 3),
        (4, 1),
        (4, 2),
    ])

    return warehouse


if __name__ == "__main__":
    warehouse = create_sample_warehouse()
    warehouse.print_grid()