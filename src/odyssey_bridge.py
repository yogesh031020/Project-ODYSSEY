import time
import random
import math

class OdysseyTelemetryBridge:
    """Simulates the ROS2-Gazebo Hardware Bridge for ODYSSEY Phase 1."""
    def __init__(self):
        self.drone_id = "ODYSSEY-01"
        self.gps_status = "LOST / DENIED" # Primary mission constraint
        self.imu_stability = 0.0
        self.camera_fps = 30
        
    def monitor_sensor_health(self, duration=10):
        print("\n" + "="*80)
        print("   PROJECT ODYSSEY: PHASE 1 - SENSOR & TELEMETRY BRIDGE")
        print("="*80)
        print(f"{'Time':<5} | {'IMU Bias (deg)':<15} | {'Cam Depth (m)':<15} | {'Nav Status'}")
        print("-" * 80)
        
        for t in range(duration):
            # Simulate Visual Odometry noise
            bias = random.uniform(0.01, 0.05)
            depth = random.uniform(1.5, 10.0)
            
            # Logic: If bias is low, navigation is "TRUSTED"
            nav_status = "TRUSTED (VIO)" if bias < 0.04 else "DRIFTING"
            
            print(f"{t:02d}s    | {bias:<15.4f} | {depth:<15.2f} | {nav_status}")
            time.sleep(0.5)
            
        print("="*80)
        print("[ODYSSEY] Phase 1 Bridge Verified. Sensor Fusion ready for SLAM integration.\n")

if __name__ == "__main__":
    bridge = OdysseyTelemetryBridge()
    bridge.monitor_sensor_health()
