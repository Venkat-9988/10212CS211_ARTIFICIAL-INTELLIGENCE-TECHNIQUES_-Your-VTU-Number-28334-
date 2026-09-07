
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [3, 5],
    'E': [6, 9],
    'F': [1, 2],
    'G': [0, 1]
}


pruned_branches = []



def minimax(node, alpha, beta, maximizing_player):

   
    if node not in tree:
        return node

  
    if maximizing_player:

        best_value = float('-inf')

        for i, child in enumerate(tree[node]):

            value = minimax(child, alpha, beta, False)

            best_value = max(best_value, value)

            alpha = max(alpha, best_value)

            if beta <= alpha:

                for r in tree[node][i + 1:]:
                    pruned_branches.append((node, r))

                break

        return best_value


    else:

        best_value = float('inf')

        for i, child in enumerate(tree[node]):

            value = minimax(child, alpha, beta, True)

            best_value = min(best_value, value)

            beta = min(beta, best_value)

            if beta <= alpha:

                for r in tree[node][i + 1:]:
                    pruned_branches.append((node, r))

                break

        return best_value

alpha = float('-inf')
beta = float('inf')

result = minimax('A', alpha, beta, True)

print("Mini-Max Value of Root A =", result)


best_move = None
best_value = float('-inf')

for child in tree['A']:

    value = minimax(
        child,
        float('-inf'),
        float('inf'),
        False
    )

    if value > best_value:
        best_value = value
        best_move = child

print("Best Move for Player A =", best_move)
print("Value of Best Move =", best_value)


def find_optimal_path(node, maximizing_player):

    
    if node not in tree:
        return [node]

    if maximizing_player:

        best_value = float('-inf')
        best_child = None

        for child in tree[node]:

            value = minimax(
                child,
                float('-inf'),
                float('inf'),
                False
            )

            if value > best_value:
                best_value = value
                best_child = child

    else:

        best_value = float('inf')
        best_child = None

        for child in tree[node]:

            value = minimax(
                child,
                float('-inf'),
                float('inf'),
                True
            )

            if value < best_value:
                best_value = value
                best_child = child

    return [node] + find_optimal_path(
        best_child,
        not maximizing_player
    )


path = find_optimal_path('A', True)

print("Optimal Path =", " -> ".join(map(str, path)))


print("\nPruned Branches:")

if pruned_branches:

 
    unique_branches = []

    for branch in pruned_branches:
        if branch not in unique_branches:
            unique_branches.append(branch)

    for parent, child in unique_branches:
        print(parent, "->", child)

else:
    print("No branches were pruned.")
