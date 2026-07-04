class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        graph={}

        for a,b,c in roads:
            if a not in graph:
                graph[a]=[]
            if b not in graph:
                graph[b]=[]
            
            graph[a].append((b,c))
            graph[b].append((a,c))

        visited=set([1])
        q=deque([1])
        ans=999999999999999999

        while q:
            node=q.popleft()
            for n,d in graph[node]:
                ans=min(ans,d)
                if n not in visited:
                    visited.add(n)
                    q.append(n)
        return ans


        