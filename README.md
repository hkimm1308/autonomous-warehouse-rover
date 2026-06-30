# Autonomous Warehouse Rover

> A collaborative robotics project focused on designing and building an autonomous warehouse robot capable of navigating a simulated fulfillment environment using computer vision, real-time path planning, and embedded control.

![Status](https://img.shields.io/badge/status-In%20Development-blue)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![ESP32](https://img.shields.io/badge/ESP32-Embedded-red)
![Raspberry%20Pi](https://img.shields.io/badge/Raspberry%20Pi-Robot%20Brain-C51A4A)

---

## Project Overview

Modern warehouses rely heavily on autonomous mobile robots to transport inventory efficiently and safely through dynamic environments. This project recreates a simplified warehouse automation system by combining robotics, computer vision, embedded systems, and software engineering.

Our objective is to build a fully autonomous rover capable of navigating a simulated warehouse environment while avoiding obstacles, rerouting around blocked paths, and completing delivery tasks without human intervention.

This project is intended to demonstrate practical engineering skills across multiple disciplines, including robotics, embedded programming, computer vision, path planning, and system integration.

---

## Project Objectives

- Design and build a custom autonomous rover
- Navigate a simulated warehouse environment
- Detect and avoid static obstacles
- Dynamically reroute around blocked paths
- Implement computer vision using OpenCV
- Control motors using closed-loop PID control
- Build a telemetry dashboard for live monitoring
- Produce a complete engineering portfolio documenting the design process

---

## System Architecture

```
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

*A graphical architecture diagram will be added as development progresses.*

---

## Tech Stack

### Software

- Python
- OpenCV
- NumPy
- PySerial

### Embedded Systems

- ESP32
- Raspberry Pi 4
- UART Serial Communication

### Algorithms

- A* Pathfinding
- PID Motor Control
- Dynamic Rerouting
- Obstacle Detection
- Grid-Based Navigation

### Hardware

- Raspberry Pi 4
- ESP32
- DC Gear Motors
- Motor Driver
- Ultrasonic Sensors
- Camera Module
- 3D Printed Chassis

---

## Repository Structure

```
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
└── tests/               # Unit tests
```

---

## Development Roadmap

### Phase 1 — Planning

- [x] Repository setup
- [x] Documentation structure
- [ ] Hardware selection
- [ ] Software architecture

### Phase 2 — Mobility

- [ ] Build chassis
- [ ] Motor integration
- [ ] Manual driving
- [ ] PID control

### Phase 3 — Perception

- [ ] Camera integration
- [ ] Obstacle detection
- [ ] Sensor fusion

### Phase 4 — Autonomous Navigation

- [ ] A* implementation
- [ ] Autonomous waypoint navigation
- [ ] Path optimization

### Phase 5 — Dynamic Environment

- [ ] Moving obstacle detection
- [ ] Dynamic rerouting
- [ ] Live telemetry dashboard

### Phase 6 — Final Demonstration

- [ ] Full autonomous warehouse run
- [ ] Demo video
- [ ] Final documentation

---

## Team

### Hudson Kimm

**Software Engineering**

- Navigation algorithms
- Computer vision
- Embedded software
- Telemetry dashboard
- Documentation

### Matt Kimm

**Mechanical & Electrical Engineering**

- Chassis design
- CAD
- Wiring
- Electronics
- Sensor integration
- Environment construction

---

## Current Progress

**Current Phase**

Planning & Architecture

### Completed

- Repository initialized
- Documentation structure created
- Development environment configured

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

---

## Gallery

Progress photos, architecture diagrams, and demonstration videos will be added throughout development.

---

## License

This project is released under the MIT License.

---

**Summer 2026**

Designed and developed collaboratively by Hudson Kimm and Matt Kimm.
