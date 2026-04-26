import csv

def solve_min_cable_length(csv_file_path):
    matrix = []
    with open(csv_file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            matrix.append([float(val) for val in row])
            
    n = len(matrix)
    if n == 0:
        return 0
    
    visited = [False] * n  
    min_dist = [float('inf')] * n  
    min_dist[0] = 0
    total_length = 0
    
    for _ in range(n):
        u = -1
        for i in range(n):
            if not visited[i] and (u == -1 or min_dist[i] < min_dist[u]):
                u = i
        
        if min_dist[u] == float('inf'):
            return -1
        
        visited[u] = True
        total_length += min_dist[u]
        
        for v in range(n):
            if not visited[v] and matrix[u][v] < min_dist[v]:
                min_dist[v] = matrix[u][v]
                
    return total_length

if __name__ == "__main__":
    result = solve_min_cable_length('islands.txt')
    print(f"Мінімальна довжина кабелів: {result}")