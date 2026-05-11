"""
Lab 6: Breadth-First Search Implementation
Finds shortest path (by number of edges) in unweighted graph.
"""
from typing import List, Dict, Optional
from collections import deque
from graph import Graph

def bfs_find_path(graph: Graph, start: str, end: str) -> Optional[List[str]]:
    """
    Find shortest path from start to end using BFS.
    
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    
    Returns:
        List of vertices forming the path, or None if no path exists
    """
    # Check if start or end is not in graph
    if start not in graph.vertices or end not in graph.vertices:
        return None

    # Initialize the queue with (start, [start]) and visited set
    queue = deque([(start, [start])])
    visited = {start}

    # While queue is not empty
    while queue:
        current_vertex, path = queue.popleft()

        # If current vertex is end, return path
        if current_vertex == end:
            return path

        # For each neighbor of current, if not visited, add to queue and visited
        for neighbor in graph.get_neighbors(current_vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    # Return None if no path exists
    return None

def bfs_all_reachable(graph: Graph, start: str) -> Dict[str, int]:
    """
    Find all vertices reachable from start and their distances.
    
    Returns:
        Dict mapping vertex -> distance from start
    """
    # Check if start is not in graph
    if start not in graph.vertices:
        return {}

    # Initialize distances dict with start at distance 0
    distances = {start: 0}
    queue = deque([start])

    # Process the queue
    while queue:
        current_vertex = queue.popleft()

        # For each neighbor of current_vertex
        for neighbor in graph.get_neighbors(current_vertex):
            if neighbor not in distances:
                # Set distance and add to queue
                distances[neighbor] = distances[current_vertex] + 1
                queue.append(neighbor)

    return distances

def bfs_is_connected(graph: Graph, v1: str, v2: str) -> bool:
    """
    Check if path exists between two vertices.
    Returns True if a path exists, False otherwise.
    """
    # Use bfs_find_path to check if path exists
    path: Optional[List[str]] = bfs_find_path(graph, v1, v2)
    
    # Return True if a path exists, False otherwise
    return path is not None

def bfs_find_path(graph: Graph, start: str, end: str) -> Optional[List[str]]:
    """
    Find shortest path from start to end using BFS.
    
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    
    Returns:
        List of vertices forming the path, or None if no path exists
    """
    # Check if start or end is not in graph
    if start not in graph.vertices or end not in graph.vertices:
        return None

    # Initialize the queue with (start, [start]) and visited set
    queue = deque([(start, [start])])
    visited = {start}

    # While queue is not empty
    while queue:
        current_vertex, path = queue.popleft()

        # If current vertex is end, return path
        if current_vertex == end:
            return path

        # For each neighbor of current, if not visited, add to queue and visited
        for neighbor in graph.get_neighbors(current_vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    # Return None if no path exists
    return None


def bfs_is_connected(graph: Graph, v1: str, v2: str) -> bool:
    """
    Check if path exists between two vertices.
    Returns True if a path exists, False otherwise.
    """
    # Use bfs_find_path to check if path exists
    path: Optional[List[str]] = bfs_find_path(graph, v1, v2)
    
    # Return True if a path exists, False otherwise
    return path is not None
