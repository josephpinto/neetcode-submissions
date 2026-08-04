class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sorted by descending position
        times = []
        for pos, speed in sorted(zip(position,speed), reverse=True):
            times.append((target-pos)/speed)
        fleet_count = 1
        curr_fleet_time = times[0]
        
        for t in times[1:]:
            if t <= curr_fleet_time:
                # joins current fleet
                continue
            else:
                fleet_count += 1
                curr_fleet_time = t
        return fleet_count

                