class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.solve(n, k, 0, [], result)
        return result 
    
    
    def solve(self, n:int, k: int, current_index: int, current_subset: List[int], result: List[List[int]]):  
        if n - current_index < k - len(current_subset):
            return 

        if current_index == n:
            if len(current_subset) == k:
                result.append(current_subset.copy())
            return

        current_subset.append(current_index + 1)
        self.solve(n, k, current_index + 1, current_subset, result)
        current_subset.pop()
        self.solve(n, k, current_index + 1, current_subset, result)
