class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # don't use same edge or ticket repeatedly

        # build graph
        graph = {}
        for ticket in tickets:
            start = ticket[0]
            if start not in graph:
                graph[start] = []
            graph[start].append(ticket[1])
        for key in graph:
            graph[key].sort()  # sort each airport's destinations

        result = []

        def dfs(airport):
            destinations = graph.get(airport, []) # destinations = graph[airport]
            while len(destinations) > 0: # has unused tix
                smallest_dest = destinations[0]
                smallest_dest = destinations.pop(0) # graph[airport].remove(smallest_dest)
                dfs(smallest_dest)
            result.append(airport)
        
        dfs("JFK") # always start from JFK
        result.reverse()
        return result