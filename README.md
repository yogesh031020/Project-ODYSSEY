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

## 🧠 Mathematical State Estimation & Mapping

### 1. Extended Kalman Filter (EKF) Visual-Inertial Fusion
To estimate quadcopter state $\mathbf{x}_k$ accurately in GPS-denied zones, ODYSSEY implements an **Error-State Extended Kalman Filter (ES-EKF)** fusing high-frequency IMU linear accelerations/angular velocities with lower-frequency Visual Odometry pose updates:

$$\mathbf{x}_k = \begin{bmatrix} \mathbf{p}_k & \mathbf{v}_k & \mathbf{q}_k & \mathbf{b}_{a,k} & \mathbf{b}_{g,k} \end{bmatrix}^T$$

Where:
*   $\mathbf{p}_k, \mathbf{v}_k$ are the position and velocity vectors in the map frame.
*   $\mathbf{q}_k$ is the unit quaternion representing orientation.
*   $\mathbf{b}_{a,k}, \mathbf{b}_{g,k}$ are the accelerometer and gyroscope sensor biases.

The measurement update correction matches visual features to minimize reprojection error $\mathbf{r}_{ij}$ over camera frames:

$$\mathbf{r}_{ij} = \mathbf{z}_{ij} - \pi(\mathbf{T}_{C_i}^W \cdot {^W\mathbf{p}_j})$$

### 2. Voxel Occupancy Grid Mapping (3D Octomap)
To achieve obstacle avoidance, depth data is converted to 3D point clouds and mapped into a voxelized octree. The log-odds probability $L(n)$ for a voxel $n$ being occupied is updated recursively:

$$L(n \mid z_{1:t}) = L(n \mid z_{1:t-1}) + \log \left[ \frac{P(n \mid z_t)}{1 - P(n \mid z_t)} \right] - L_0$$

Where $P(n \mid z_t)$ is the sensor model probability mapping the depth ray intersection, and $L_0$ is the prior probability.

---

## 📂 Repository Directory Layout

```directory
-Project-ODYSSEY/
├── launch/
│   └── display.launch.py                  # RViz visualizer & system topology launcher
├── models/                                # URDF quadcopter models with stereo-depth cameras
├── src/
│   ├── odyssey_autonomy.py                # High-level mission supervisor & Nav2 control loop
│   ├── odyssey_bridge.py                  # ROS 2 to simulation bridge driver
│   ├── vio_engine.py                      # Multi-sensor fusion state estimator
│   └── voxel_mapper.py                    # Voxel grid generator & point cloud processor
├── worlds/                                # Complex 3D environments (Industrial warehouse, dense forest)
├── LICENSE                                # MIT License
└── README.md                              # Main portfolio presentation guide
```

---

## 📈 Engineering Goals
- [x] **Phase 1:** Integrated ROS2-Gazebo sensor bridge with 100% telemetry sync.
- [x] **Phase 2:** Real-time 3D Occupancy Grid generation from depth data.
- [ ] **Phase 3:** < 0.5m drift in VIO-only flight missions.
- [ ] **Phase 4:** Fully autonomous dynamic obstacle avoidance.

---
**Developed by Yogesh E S**  
*Senior Aerospace Portfolio - Project #7 (The Crown Jewel)*
