# Project ODYSSEY: GPS-Denied 3D Vision Autonomy 🛰️❌ 👁️✅

![Status](https://img.shields.io/badge/Status-Research--Phase-orange)
![Domain](https://img.shields.io/badge/Domain-Computer--Vision--Robotics-blue)
![Complexity](https://img.shields.io/badge/Complexity-Expert-red)

**Project ODYSSEY** is an advanced vision-based navigation framework designed for UAV operations in GPS-denied environments (indoors, forests, urban canyons). It leverages **Visual-Inertial Odometry (VIO)** and **3D SLAM** to enable fully autonomous flight where traditional satellite navigation fails.

---

## 🚀 The Challenge
Standard drones rely on GPS to know their position. Project ODYSSEY solves the "Lost Drone" problem by using a **Stereo Depth Camera** and **IMU Fusion** to build a map of the environment and calculate its own position relative to obstacles in real-time.

## 🧠 Core Technologies
- **Middleware:** ROS 2 Humble / Jazzy
- **Simulation:** Gazebo Harmonic (Ignition)
- **Visual SLAM:** ORB-SLAM3 / RTAB-Map
- **Perception:** OpenCV / Point Cloud Library (PCL)
- **Path Planning:** Nav2 (Navigation 2 Stack)

## 📂 Repository Structure
- `src/`: Custom ROS2 nodes for sensor fusion and vision processing.
- `models/`: URDF/SDF descriptions of the quadcopter with stereo-vision sensors.
- `worlds/`: Complex Gazebo environments (Forest, Industrial Warehouse).
- `launch/`: Python launch files for the complete autonomy stack.

---

## 📈 Engineering Goals
- [ ] **Phase 1:** Integrated ROS2-Gazebo sensor bridge with 100% telemetry sync.
- [ ] **Phase 2:** Real-time 3D Occupancy Grid generation from depth data.
- [ ] **Phase 3:** < 0.5m drift in VIO-only flight missions.
- [ ] **Phase 4:** Fully autonomous dynamic obstacle avoidance.

---
**Developed by Yogesh E S**  
*Senior Aerospace Portfolio - Project #7 (The Crown Jewel)*
