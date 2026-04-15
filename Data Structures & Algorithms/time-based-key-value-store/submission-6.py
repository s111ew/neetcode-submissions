class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.store:
            self.store[key] = []
        self.store[key].append({"val": value, "ts": timestamp})


    def get(self, key: str, timestamp: int) -> str:
        res = ""
        
        values = self.store.get(key, [])

        left = 0
        right = len(values) - 1
        while left <= right:
            mid = (left + right) // 2

            if values[mid]["ts"] <= timestamp:
                res = values[mid]["val"]
                left = mid + 1
            else:
                right = mid - 1
        
        return res

