# Autonomous Warehouse Rover

> A collaborative robotics project focused on designing and building an autonomous warehouse robot capable of navigating a simulated fulfillment environment using path planning, dynamic rerouting, computer vision, and embedded control.

![Status](https://img.shields.io/badge/status-In%20Development-blue)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Tests](https://img.shields.io/badge/tests-14%20passing-brightgreen)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![ESP32](https://img.shields.io/badge/ESP32-Embedded-red)
![Raspberry%20Pi](https://img.shields.io/badge/Raspberry%20Pi-Robot%20Brain-C51A4A)

---

## Project Overview

Modern warehouses rely heavily on autonomous mobile robots to transport inventory efficiently and safely through dynamic environments. This project recreates a simplified warehouse automation system by combining robotics, path planning, computer vision, embedded systems, and software engineering.

The current software stack simulates a warehouse environment where a robot can calculate the shortest valid route, avoid obstacles, move step-by-step through the grid, detect newly blocked paths, and dynamically replan its route using A* search.

The long-term objective is to connect this navigation system to a physical rover using a Raspberry Pi, ESP32, sensors, motor control, and computer vision.

---

## Current Features

- Grid-based warehouse environment
- Static obstacle placement
- A* shortest-path planning
- Manhattan-distance heuristic
- Path visualization in the terminal
- Dynamic obstacle rerouting
- Step-by-step robot movement simulation
- Mid-route replanning when a new obstacle blocks the path
- Unit tests for pathfinding, robot movement, and dynamic replanning
- Git feature-branch workflow for navigation development

---

## Demo Commands

Run the multi-scenario warehouse rerouting demo:

```bash
python -m software.simulation.grid_simulator
