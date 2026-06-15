class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        k = 4 
        perimetre = sum(matchsticks)

        if perimetre % k != 0:
            return False
        
        required_length = perimetre // k 
        visited = [0] * len(matchsticks)
        return self.solve(matchsticks, k, 0, visited, required_length, required_length)
    
    def solve(self, matchsticks: List[int], k: int, current_index: int, visited: List[int], 
                    target_length: int, req_length: int):
        if k == 0:
            return True 
        
        if target_length == 0:
            return self.solve(matchsticks, k-1, 0, visited, req_length, req_length)
        
        for index in range(current_index, len(matchsticks)):
            if visited[index] == 0 and target_length >= matchsticks[index]:
                visited[index] = 1
                if self.solve(matchsticks, k, index + 1, visited, target_length - matchsticks[index], req_length):
                    return True 
                visited[index] = 0 
        
        return False
        