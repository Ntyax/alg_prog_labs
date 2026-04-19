import heapq

def solve_server_placement(n, clients, edges):

    adj = {i: [] for i in range(1, n + 1)}
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    min_max_latency = float('inf')

    for candidate_server in range(1, n + 1):
        if candidate_server in clients:
            continue
        
        distances = {i: float('inf') for i in range(1, n + 1)}
        distances[candidate_server] = 0
        pq = [(0, candidate_server)]
        
        while pq:
            curr_dist, u = heapq.heappop(pq)
            
            if curr_dist > distances[u]:
                continue
                
            for v, weight in adj[u]:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    heapq.heappush(pq, (distances[v], v))
        
        current_max_latency = 0
        for client in clients:
            current_max_latency = max(current_max_latency, distances[client])

        min_max_latency = min(min_max_latency, current_max_latency)

    return min_max_latency