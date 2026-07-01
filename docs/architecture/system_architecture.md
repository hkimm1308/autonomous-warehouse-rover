# System Architecture

## Overview

The Autonomous Warehouse Rover is designed as a two-layer robotics system:

1. **High-level autonomy layer** running on the Raspberry Pi
2. **Low-level motor control layer** running on the ESP32

The Raspberry Pi handles perception, navigation, path planning, and decision-making. The ESP32 handles real-time motor control and PID feedback. This separation keeps the robot modular and makes debugging easier.

---

## High-Level Architecture

```text
Camera / Ultrasonic Sensors
          │
          ▼
    Raspberry Pi 4
          │
          ├── Perception System
          │     └── Detects obstacles, markers, and warehouse zones
          │
          ├── Grid Mapping System
          │     └── Converts the environment into a 2D navigation grid
          │
          ├── Path Planner
          │     └── Uses A* to find a route from start to goal
          │
          ├── Navigation Controller
          │     └── Converts path coordinates into movement commands
          │
          └── Telemetry Logger
                └── Records state, sensor readings, and reroute events
          │
          ▼
 Serial / UART Communication
          │
          ▼
        ESP32
          │
          ├── PID Controller
          │     └── Maintains heading and speed stability
          │
          └── Motor Driver Interface
                └── Sends PWM signals to drive motors
          │
          ▼
       DC Motors