class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        def dfs(node):
            visited[node] = True

            nodes = 1
            edge_count = len(graph[node])

            for nei in graph[node]:
                if not visited[nei]:
                    n_nodes, n_edges = dfs(nei)
                    nodes += n_nodes
                    edge_count += n_edges

            return nodes, edge_count

        ans = 0

        for i in range(n):
            if not visited[i]:
                nodes, edge_count = dfs(i)

                edge_count //= 2

                if edge_count == nodes * (nodes - 1) // 2:
                    ans += 1

        return ans