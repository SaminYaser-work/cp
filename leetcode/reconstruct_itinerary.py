from typing import List


# Find the Euler path, use every edge (ticket) atleast once
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {i: [] for i, _ in tickets}

        for n1, n2 in tickets:
            adj[n1].append(n2)

        for n in adj:
            adj[n].sort()

        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True

            # Disconnected vertex
            if src not in adj:
                return False

            temp = adj[src][:]
            for i, n in enumerate(temp):
                adj[src].pop(i)
                res.append(n)
                if dfs(n):
                    return True
                adj[src].insert(i, n)
                res.pop()

        dfs("JFK")
        return res
