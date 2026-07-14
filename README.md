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
```

Run the step-by-step robot movement demo:

```bash
python -m software.simulation.robot_movement_simulator
```

Run the dynamic robot replanning demo:

```bash
python -m software.simulation.dynamic_robot_simulator
```

Run the test suite:

```bash
python -m pytest
```

Current test status:

```text
14 passed
```

---

## System Architecture

Current software architecture:

```text
GridMap
   │
   ▼
AStarPlanner
   │
   ▼
Robot
   │
   ▼
Simulation
   │
   ▼
Future Hardware Integration
```

Planned full-system architecture:

```text
                    Camera
                      │
                      ▼
             Raspberry Pi 4
                      │
         Computer Vision (OpenCV)
                      │
          Navigation & Path Planning
                 (A* Algorithm)
                      │
          Serial Communication
                      │
                     ESP32
                      │
               PID Motor Control
                      │
                Motor Driver
                      │
                  DC Motors
```

---

## Tech Stack

### Current Software

- Python
- Pytest
- A* Pathfinding
- Grid-Based Navigation
- Dynamic Rerouting
- Robot Movement Simulation

### Planned Software

- OpenCV
- NumPy
- PySerial
- Telemetry dashboard

### Planned Embedded Systems

- ESP32
- Raspberry Pi 4
- UART Serial Communication
- PID Motor Control

### Planned Hardware

- Raspberry Pi 4
- ESP32
- DC Gear Motors
- Motor Driver
- Ultrasonic Sensors
- Camera Module
- 3D Printed Chassis

---

## Repository Structure

```text
autonomous-warehouse-rover/

├── assets/              # Images, diagrams, logos
├── data/                # Telemetry and testing data
├── docs/                # Documentation
├── environment/         # Warehouse layouts and obstacle designs
├── firmware/            # ESP32 firmware
├── hardware/            # CAD, wiring, assembly documentation
├── media/               # Photos, videos, GIFs
├── scripts/             # Utility scripts
├── software/            # Python source code
│   ├── navigation/      # GridMap and A* path planning
│   ├── robot/           # Robot movement logic
│   └── simulation/      # Warehouse and robot simulators
└── tests/               # Unit tests
```

---

## Development Roadmap

### Phase 1 — Planning & Architecture

- [x] Repository setup
- [x] Documentation structure
- [x] Git feature-branch workflow
- [x] Initial software architecture
- [ ] Hardware selection

### Phase 2 — Navigation Simulation

- [x] GridMap environment
- [x] Static obstacle handling
- [x] A* pathfinding
- [x] Path visualization
- [x] Dynamic obstacle rerouting
- [x] Step-by-step robot movement
- [x] Mid-route replanning
- [x] Unit tests

### Phase 3 — Mobility

- [ ] Build chassis
- [ ] Motor integration
- [ ] Manual driving
- [ ] PID control

### Phase 4 — Perception

- [ ] Camera integration
- [ ] Obstacle detection
- [ ] Sensor fusion

### Phase 5 — Hardware Integration

- [ ] Raspberry Pi setup
- [ ] ESP32 firmware
- [ ] Serial communication
- [ ] Motor command pipeline

### Phase 6 — Final Demonstration

- [ ] Full autonomous warehouse run
- [ ] Demo video
- [ ] Final documentation
- [ ] Portfolio write-up

---

## Team

### Hudson Kimm

**Software Engineering**

- Navigation algorithms
- Path planning
- Robot movement simulation
- Dynamic rerouting
- Computer vision
- Embedded software
- Telemetry dashboard
- Documentation

### Matt Blong

**Mechanical & Electrical Engineering**

- Chassis design
- CAD
- Wiring
- Electronics
- Sensor integration
- Environment construction

---

## Current Progress

The project currently has a working Python-based navigation simulation. The robot can calculate a path through a warehouse grid, move step-by-step, detect when a new obstacle blocks its current route, replan from its current position, and continue to the goal.

Current validation:

```text
14 passing tests
```

Current active branch:

```text
hudson/navigation
```

---

## Future Improvements

Potential extensions include:

- SLAM-based navigation
- AprilTag or ArUco marker localization
- Robotic arm for package pickup
- Autonomous charging dock
- Multi-robot coordination
- ROS2 integration
- LiDAR mapping
- Reinforcement learning for navigation
- Real-time telemetry dashboard

---

## Gallery

Progress photos, architecture diagrams, and demonstration videos will be added throughout development.

---

## License

This project is released under the MIT License.

---

**Summer 2026**

Designed and developed collaboratively by Hudson Kimm and Matt Blong.