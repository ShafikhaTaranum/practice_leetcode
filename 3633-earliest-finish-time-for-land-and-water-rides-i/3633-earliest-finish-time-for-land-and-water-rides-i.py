class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        min_finish_time = float('inf')
        n = len(landStartTime)
        m = len(waterStartTime)
        
        for i in range(n):
            for j in range(m):
                # Case 1: Land Ride -> Water Ride
                land_finish = landStartTime[i] + landDuration[i]
                water_start = max(land_finish, waterStartTime[j])
                total_finish_1 = water_start + waterDuration[j]
                
                # Case 2: Water Ride -> Land Ride
                water_finish = waterStartTime[j] + waterDuration[j]
                land_start = max(water_finish, landStartTime[i])
                total_finish_2 = land_start + landDuration[i]
                
                min_finish_time = min(min_finish_time, total_finish_1, total_finish_2)
                
        return min_finish_time
        