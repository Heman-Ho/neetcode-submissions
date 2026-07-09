import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create a map pos: speed 
        # Sort the list from closest pos to target to farthest
        # Traverse the list
        # Each time a car is unable to catch up with the previous fleet, it becomes it's own new fleet
        pos_to_speed = {}
        for i in range(len(position)):
            pos_to_speed[position[i]] = speed[i]

        position.sort(reverse=True)

        num_fleets = 0
        cur_fleet_dest_time = 0.0
        for pos in position:
            cur_dest_time = (target-pos) / pos_to_speed[pos]
            if cur_dest_time > cur_fleet_dest_time:
                cur_fleet_dest_time = cur_dest_time
                num_fleets += 1
        
        return num_fleets