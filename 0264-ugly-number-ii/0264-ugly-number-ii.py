class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        
        store = [1]
        p1 = p2 = p3 = 0
        
        while len(store) < n:
            next_ugly_2 = store[p1] * 2
            next_ugly_3 = store[p2] * 3
            next_ugly_5 = store[p3] * 5
            
            next_ugly = min(next_ugly_2, next_ugly_3, next_ugly_5)
            store.append(next_ugly)
            
            if next_ugly == next_ugly_2:
                p1 += 1
            if next_ugly == next_ugly_3:
                p2 += 1
            if next_ugly == next_ugly_5:
                p3 += 1
        
        return store[-1]
