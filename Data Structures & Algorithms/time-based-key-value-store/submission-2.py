class TimeMap:

    def __init__(self):
        self._map: defaultdict[str, list[tuple[str, int]]] = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._map[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        arr = self._map.get(key, [])
        res = ""

        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2 
            if arr[mid][1] <= timestamp:
                res = arr[mid][0]
                lo = mid + 1
            else:
                hi = mid - 1

        return res