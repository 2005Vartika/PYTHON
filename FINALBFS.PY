def take_bst_input():
    graph = {}
    n = int(input("Enter the number of nodes in the BST: "))
    
    for _ in range(n):
        # Input for the node value (key)
        key = input("Enter the node value: ")
        
        # Input for the left child, None if no left child
        left = input(f"Enter left child of {key} (or 'None' if no left child): ")
        left = None if left.lower() == 'none' else left
        
        # Input for the right child, None if no right child
        right = input(f"Enter right child of {key} (or 'None' if no right child): ")
        right = None if right.lower() == 'none' else right
        
        # Store the node and its children in the dictionary
        graph[key] = [left, right]
    
    return graph

visited = []  # List to keep track of visited nodes.
queue = []    # Initialize a queue

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0) 
        print(s, end=" ") 

        # For each neighbor of the node
        for neighbour in graph.get(s):  # Handle nodes that might not have children
            if neighbour and neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Driver Code

# Get input from the user
graph = take_bst_input()

# Print the dictionary
print("\nThe BST dictionary you entered is:")
print(graph)

# Get root node from the user for BFS
node = input("Enter the root node: ")

# Ensure the node exists in the graph
if node in graph:
    bfs(visited, graph, node)
else:
    print(f"Error: The node {node} is not a valid root in the graph.")
