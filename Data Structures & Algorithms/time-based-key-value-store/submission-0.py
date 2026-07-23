class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])
        print(self.store)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
            
        history = self.store[key]
        l = 0
        r = len(history) - 1
        res = ""
        
        # Binary search to find the closest timestamp_prev <= timestamp
        while l <= r:
            mid = (l + r) // 2
            mid_timestamp = history[mid][0]
            mid_value = history[mid][1]
            
            if mid_timestamp == timestamp:
                return mid_value # Perfect match found
            elif mid_timestamp < timestamp:
                res = mid_value  # This is a valid past value, save it as a candidate
                l = mid + 1      # Try to find a closer/larger valid timestamp to the right
            else:
                r = mid - 1      # Too far in the future, search to the left
                
        return res
        
