class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        combined_sorted_data = sorted(zip(position,speed), reverse=True)

        times = [(target-d)/v for d,v in combined_sorted_data]
        fleets = 1
        curr_fleet_time = times[0]

        for t in times[1:]:
            if t <= curr_fleet_time:
                # joins current fleet
                continue
            # no overlap, new fleet
            fleets += 1
            curr_fleet_time = t
        return fleets

