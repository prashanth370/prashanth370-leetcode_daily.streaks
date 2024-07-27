class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        num_letters = 26
        max_cost = 999999999
        graph = []
        for i in range(num_letters):
            row = [max_cost] * num_letters
            graph.append(row)
        for i in range(len(original)):
            u_idx = ord(original[i]) - ord('a')
            v_idx = ord(changed[i]) - ord('a')
            graph[u_idx][v_idx] = min(graph[u_idx][v_idx], cost[i])
        for i in range(num_letters):
            graph[i][i] = 0
        for k in range(num_letters):
            for i in range(num_letters):
                for j in range(num_letters):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        total_cost = 0
        for i in range(len(source)):
            s_idx = ord(source[i]) - ord('a')
            t_idx = ord(target[i]) - ord('a')
            c = graph[s_idx][t_idx]
            if c == max_cost:
                return -1
            total_cost += c
        return total_cost