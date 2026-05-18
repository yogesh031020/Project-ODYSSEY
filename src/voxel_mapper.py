import numpy as np
import time

class OdysseyVoxelMapper:
    """
    Simulates a 3D Voxel Grid (OctoMap style) for Project ODYSSEY.
    This is the core of GPS-denied obstacle awareness.
    """
    def __init__(self, size=10, resolution=1.0):
        self.size = size
        self.resolution = resolution
        # Initialize an empty 10x10x10 3D grid (0: Empty, 1: Occupied)
        self.grid = np.zeros((size, size, size))
        print(f"[ODYSSEY] 3D Voxel Mapper Initialized. Resolution: {resolution}m")

    def map_environment(self):
        """Simulates depth camera hits creating a 3D obstacle map."""
        print("\n" + "="*80)
        print("   PROJECT ODYSSEY: PHASE 2 - 3D OCCUPANCY MAPPING (VOXEL GRID)")
        print("="*80)
        
        # Simulate some obstacles (e.g., a wall at X=5)
        print("[MAP] Detecting Industrial Warehouse environment...")
        for y in range(self.size):
            for z in range(self.size):
                self.grid[5, y, z] = 1 # A vertical wall at X=5
        
        print("[MAP] Wall Obstacle Detected at X=5.0m (Full Height)")
        
        # Calculate Free Space percentage
        total_voxels = self.size ** 3
        occupied_voxels = np.sum(self.grid)
        free_space = ((total_voxels - occupied_voxels) / total_voxels) * 100
        
        print(f"[MAP] Voxel Grid Density: {occupied_voxels} Occupied | {free_space:.1f}% Navigable")
        print("-" * 80)
        
        # Simulate Path Clearance Check
        drone_pos = [2, 5, 2] # Current position
        print(f"[NAV] Current Drone Position: {drone_pos}")
        
        # Look ahead along X axis
        for x in range(drone_pos[0], self.size):
            if self.grid[x, drone_pos[1], drone_pos[2]] == 1:
                dist = (x - drone_pos[0]) * self.resolution
                print(f"[ALERT] Collision Predicted in {dist}m at Voxel({x}, {drone_pos[1]}, {drone_pos[2]})")
                break
        
        print("="*80)
        print("[ODYSSEY] Phase 2 Mapping Complete. Voxel Data saved to sim/voxel_map.log\n")

    def save_log(self):
        log_path = "d:\\Drone_Projects\\Project_ODYSSEY\\sim\\voxel_map.log"
        with open(log_path, "w") as f:
            f.write("ODYSSEY PHASE 2: 3D VOXEL MAP DATA\n")
            f.write(f"Grid Size: {self.size}x{self.size}x{self.size}\n")
            f.write(f"Occupied Voxels: {int(np.sum(self.grid))}\n")
            f.write("Collision Detected: YES (Wall at X=5.0)\n")

if __name__ == "__main__":
    mapper = OdysseyVoxelMapper()
    mapper.map_environment()
    mapper.save_log()
