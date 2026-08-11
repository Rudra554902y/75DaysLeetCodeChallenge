import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dis = [float("inf")] * (n + 1)
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))
        heap = [(0, k)]
        dis[k] = 0
        while heap:
            d, u = heapq.heappop(heap)
            if d != dis[u]:
                continue
            for v, nd in graph[u]:
                if d + nd < dis[v]:
                    dis[v] = d + nd
                    heapq.heappush(heap, (dis[v], v))
        mx = max(dis[1:])
        return -1 if mx == float("inf") else mx