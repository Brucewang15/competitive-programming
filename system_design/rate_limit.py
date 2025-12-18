import time
from collections import deque
import threading


"""
Thinking process

"""

class RateLimiter:
    def __init__(self, rate: int, per: float):
        """
        rate: number of tokens
        per: time window in seconds
        """
        self.rate = rate
        self.per = per
        self.lock = threading.Lock()
        self.cache = {}

    def allow(self, client_id: str) -> bool:
        """
        Returns True if the request is allowed, False otherwise.
        """
        cur_time = time.monotonic()
        with self.lock:
            if client_id not in self.cache:
                self.cache[client_id] = deque([cur_time])
                return True

            for _ in range(len(self.cache[client_id])):
                if cur_time - self.cache[client_id][0] < self.per:
                    break
                self.cache[client_id].popleft()
            
            if len(self.cache[client_id]) < self.rate:
                self.cache[client_id].append(cur_time)
                return True
            return False


def main():
    rl = RateLimiter(5, 1)
    for _ in range(5):
        print(rl.allow("user"))
    time.sleep(1.2)
    for _ in range(6):
        print(rl.allow("user"))
    


        
if __name__ == "__main__":
    main()