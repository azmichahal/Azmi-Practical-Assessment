"""

Implementation of the Floyd-Warshall algorithm using a recursive approach
Initializing number of nodes to 5

"""

N = 5
INF = 99999

def floyd(input_matrix):
    
    """
    Applies the Floyd-Warshall algorithm to find the shortest paths
    between all pairs of vertices in a weighted graph.

    Args:
    graph_matrix (List[List[int]]): The weighted adjacency matrix representing the graph.

    Returns:
    dist: The matrix with updated values representing the shortest distances.
    """

    # Create a copy of the input matrix to store the updated values
    dist = [row[:] for row in input_matrix]
    
    # Call the recursive function to perform the Floyd-Warshall algorithm
    recursive_floyd(input_matrix, dist, 0, 0, 0)
    
    # Return the matrix with updated values representing the shortest distances
    return dist

def recursive_floyd(input_matrix, dist, k, i, j): 
    
    """ 
    Recursively iterates over all vertices to update shortest paths.

    Args:
    - input_graph: The weighted adjacency matrix representing the graph.
    - dist       : The matrix with updated values representing the shortest distances.
    - k (int)    : Represents the current intermediate vertex being considered.
    - i (int)    : Represents the current source vertex being considered.
    - j (int)    : Represents the current destination vertex being considered.
    """

    # Base case: If the intermediate vertex has reached the last vertex, print and return
    if k == N:
        print_matrix(dist)
        return
    
    # Recursive case: If the source vertex has reached the last vertex, move to the next iteration
    elif i == N:
        recursive_floyd(input_matrix, dist, k + 1, 0, 0)
        return
    
    # Recursive case: If the destination vertex has reached the last vertex, move to the next row
    elif j == N:
        recursive_floyd(input_matrix, dist, k, i + 1, 0)
        return
    
    # Update the shortest path from vertex 'i' to vertex 'j' through intermediate vertex 'k'
    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    # Move to the next column in the current row
    recursive_floyd(input_matrix, dist, k, i, j + 1)

def print_matrix(dist):
    """
    Prints the given matrix, representing distances between vertices.

    Args:
    - dist (List[List[int]]): The matrix to be printed.

    Returns:
    None: The function only performs printing and has no return value.
    """
    # Iterate over each row in the matrix
    for i in range(N):
        # Iterate over each column in the row
        for j in range(N):
            # Print 'INF' if the distance is infinity, otherwise print the distance
            if dist[i][j] == INF:
                print(f"{('INF'):>7}", end=" ")
            else:
                print(f"{dist[i][j]:>7}", end=" ")

            # Check if it's the last column in the row, and if so, move to the next line
            if j == N-1:
                print()

if __name__ == "__main__":
    # Example input graph

    input_matrix = [
        [0, 2, INF, INF, INF],
        [INF, 0, 6, INF, INF],
        [INF, 7, 0, INF, INF],
        [INF, INF, 1, 0, 3],
        [1, 4, INF, INF, 0],
    ]

    # Run the Floyd-Warshall algorithm
    print("The Shortest Distance Matrix:")
    final_result = floyd(input_matrix)

    