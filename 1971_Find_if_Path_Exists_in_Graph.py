class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        mappings = collections.defaultdict(list)
        for u, v in edges:
            mappings[u].append(v)
            mappings[v].append(u)

        def dfs(vertex, visited):
            if vertex == destination:
                return True
            visited.add(vertex)
            for neighbor in mappings[vertex]:
                if neighbor not in visited:
                    if dfs(neighbor, visited):
                        return True
            return False

        visited = set()
        return dfs(source, visited)
